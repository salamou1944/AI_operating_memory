# Evolution Frontier — Evidence-Gated Self-Improvement Contract

Status: engineering design / executable target
Date: 2026-09-19
Scope: Elite / ARMY-14 / MONY / EASY integration without cross-project state leakage

## 1. Objective

Turn repository evolution from a one-shot coding action into an evidence-gated loop:

Observe -> Research -> Discover Gap -> Hypothesize -> Generate Mutations -> Sandbox -> Attack -> Verify -> Learn -> Promote -> Deploy -> Observe

A mutation is never promoted because an agent says it is better. Promotion requires reproducible evidence.

## 2. Non-negotiable invariants

- Project state is isolated by an explicit project identifier.
- Code, tests, credentials, deployment configuration and persistent state have separate ownership boundaries.
- Mutation and verification are independent roles.
- Baselines are immutable for an experiment.
- Failed experiments become searchable negative knowledge.
- A passing functional test is insufficient when latency, cost, reliability, security, or regression evidence is required.
- Provider-dependent evidence is explicitly marked provider-dependent.
- Revenue is never inferred from synthetic tests, URL reachability, provider health, or generated artifacts.
- Production promotion is fail-closed when required evidence is missing.
- Every promoted mutation has an evidence bundle and content hash.

## 3. Experiment record

Each experiment must contain:

experiment_id
project_id
target_component
baseline_revision
hypothesis
candidate_mutations[]
sandbox_id
test_suite
adversarial_suite
metrics
regressions
verification_runs[]
decision
evidence_hash
created_at
completed_at

## 4. Promotion gate

PROMOTE only when:

1. baseline is known;
2. mutation is reproducible;
3. required deterministic tests pass;
4. adversarial checks pass;
5. no protected regression is detected;
6. required security checks pass;
7. cost/latency/reliability budgets remain within policy;
8. independent verification succeeds;
9. evidence bundle is complete and hashable;
10. project boundary validation succeeds.

Otherwise: REJECT or HOLD. Never silently promote.

## 5. Roles

Researcher: finds external/internal evidence and proposes hypotheses.
Discoverer: identifies capability gaps from repository state and benchmarks.
Mutator: produces candidate changes.
Executor: runs candidates in isolated environments.
Attacker: attempts to falsify the claimed improvement.
Verifier: independently evaluates the result against the baseline.
Historian: records successes, failures and evidence.
Promoter: applies only evidence-approved changes.
Observer: monitors post-deployment behavior and feeds new observations back into discovery.

No single role should both create and independently certify its own mutation.

## 6. Anti-regression model

Every experiment compares baseline vs candidate on a multidimensional vector:

functional correctness
test coverage / hidden-test behavior
security
reliability
latency
resource cost
maintainability
compatibility
project-boundary integrity

A candidate can be rejected even when functional tests pass if it causes an unacceptable regression in another protected dimension.

## 7. Long-horizon memory

Negative results are first-class records.

Before generating a new mutation, the system must search prior experiments for:
- equivalent hypotheses;
- failed approaches;
- known regressions;
- provider limitations;
- previously accepted patterns.

Repeated failure should change experiment selection rather than merely increase retry count.

## 8. Cross-project firewall

Allowed project identifiers are explicit:

EASY
MONY
ELITE
ARMY-14
EVOLUTION-LAB
AGENT-SKILLS

A task must declare its project before reading project-specific state. State from another project is reference-only unless an explicit integration contract permits it.

## 9. Evidence quality levels

L0 — idea only
L1 — code exists
L2 — deterministic local/repository tests
L3 — independent verification
L4 — repeated/adversarial verification
L5 — deployed observation with production evidence

Claims must state their evidence level. L1 is never presented as L3-L5.

## 10. Definition of the frontier

The system reaches the target frontier when it can autonomously discover at least one previously unlisted capability gap, generate multiple materially different candidates, evaluate them against an immutable baseline, attempt to break the best candidate, independently verify the surviving candidate, preserve the losing evidence, and produce a reproducible promotion record without crossing project boundaries.

This document is a contract, not a completion claim.
