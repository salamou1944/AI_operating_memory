import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_company_control", ROOT / "scripts" / "validate_company_control.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

def event(event_id, state, event_type, actor="agent-001", owner="agent-002", **extra):
    value = {
        "event_id": event_id, "task_id": "task-test", "timestamp_utc": "2026-11-03T20:00:00Z",
        "actor_id": actor, "event_type": event_type, "state": state, "objective": "Test task",
        "owner_id": owner, "risk": "low", "approval_gate": "none", "acceptance_criteria": ["works"],
        "evidence_refs": ["https://github.com/example/repo/commit/0123456789012345678901234567890123456789"],
        "memory_event_ids": [],
    }
    value.update(extra)
    return value

class CompanyControlValidationTests(unittest.TestCase):
    def errors(self, *items):
        return MODULE.validate_events(list(enumerate(items, 1)))

    def test_valid_initial_event_and_transition(self):
        self.assertEqual([], self.errors(
            event("e1", "proposed", "created"),
            event("e2", "ready", "transition"),
        ))

    def test_rejects_unknown_schema_fields(self):
        errors = self.errors(event("e1", "proposed", "created", unexpected="bad"))
        self.assertTrue(any("unknown fields" in error for error in errors))

    def test_rejects_illegal_transition(self):
        errors = self.errors(
            event("e1", "proposed", "created"),
            event("e2", "done", "transition"),
        )
        self.assertTrue(any("illegal task transition" in error for error in errors))

    def test_done_requires_independent_verification(self):
        errors = self.errors(
            event("e1", "proposed", "created"),
            event("e2", "ready", "transition"),
            event("e3", "assigned", "transition"),
            event("e4", "in_progress", "transition"),
            event("e5", "review", "transition"),
            event("e6", "done", "transition", actor="agent-001"),
        )
        self.assertTrue(any("independent verification" in error for error in errors))

    def test_owner_cannot_self_verify(self):
        errors = self.errors(
            event("e1", "proposed", "created"),
            event("e2", "ready", "transition"),
            event("e3", "assigned", "transition"),
            event("e4", "in_progress", "transition"),
            event("e5", "review", "transition"),
            event("e6", "review", "verification", actor="agent-002"),
            event("e7", "done", "transition", actor="agent-001"),
        )
        self.assertTrue(any("independent verification" in error for error in errors))


    def test_stale_verification_does_not_authorize_later_done(self):
        errors = self.errors(
            event("e1", "proposed", "created"),
            event("e2", "ready", "transition"),
            event("e3", "assigned", "transition"),
            event("e4", "in_progress", "transition"),
            event("e5", "review", "transition"),
            event("e6", "review", "verification", actor="agent-001"),
            event("e7", "in_progress", "transition"),
            event("e8", "review", "transition"),
            event("e9", "done", "transition", actor="agent-001"),
        )
        self.assertTrue(any("independent verification" in error for error in errors))

    def test_accepts_independent_verification_before_done(self):
        self.assertEqual([], self.errors(
            event("e1", "proposed", "created"),
            event("e2", "ready", "transition"),
            event("e3", "assigned", "transition"),
            event("e4", "in_progress", "transition"),
            event("e5", "review", "transition"),
            event("e6", "review", "verification", actor="agent-001"),
            event("e7", "done", "transition", actor="agent-001"),
        ))

if __name__ == "__main__":
    unittest.main()
