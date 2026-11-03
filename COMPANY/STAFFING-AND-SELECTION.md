# Agent Staffing and Selection Policy

## Principle

An agent is hired for a demonstrated business capability, not for a model name, persona, benchmark claim, or fluent conversation. A role is a bundle of accountable outputs; an agent may hold multiple roles initially, but incompatible duties must be separated for review.

## Candidate scorecard

Score each dimension from 0 to 5 using a bounded work sample and evidence:

| Dimension | What is tested | Weight |
|---|---|---:|
| Delivery reliability | Completes the task and reports actual state accurately | 25% |
| Reasoning and challenge | Finds counterexamples, risks, and better alternatives | 20% |
| Tool competence | Uses granted tools correctly and verifies outcomes | 20% |
| Communication / handoff | Produces concise, structured, reusable work | 15% |
| Security and judgment | Respects least privilege, privacy, and approval boundaries | 15% |
| Cost / latency efficiency | Delivers acceptable quality with proportionate resource use | 5% |

Minimum bar for an operational role: 3.5/5 weighted score, no critical security failure, and evidence from at least two different task types. A security or honesty failure disqualifies a candidate regardless of average score.

## Hiring stages

1. Identity and environment verification: account, runtime, tools, actual execution boundary.
2. Independent work sample: candidate assesses a task before seeing the manager's conclusion.
3. Adversarial work sample: candidate must challenge the manager and identify at least three material failure modes.
4. Execution sample: candidate performs a reversible, bounded task in an authorized repository or sandbox.
5. Verification sample: candidate supplies evidence another agent can independently check.
6. Probation: two or more real handoffs, with quality, timeliness, cost, and rework measured.
7. Appointment: role and permissions are assigned based on demonstrated strengths.

## Initial roles (positions, not assumed headcount)

- Managing Director / Orchestrator — portfolio, prioritization, delegation, decision log.
- Revenue Development — buyer research, qualification, outreach preparation, pipeline.
- Product / Solutions — offer definition, customer requirements, delivery design.
- Engineering / Integration — implementation, tests, deployment adapters.
- Quality / Security — independent adversarial review, evidence checks, security controls.
- Finance / Operations — unit economics, payment evidence, cost and capacity reporting.

Initially, the same agent may cover more than one role. Quality review should be performed by a different agent or an independent tool/test wherever possible. Do not create separate agents when deterministic automation is cheaper and more reliable.

## Founding Employee #2

Agent #2 is the first employee by the cofounder's appointment. Do not invent its identity or capabilities. The initial assignment is to:
- declare its actual identity, runtime, and tool permissions;
- confirm whether it can independently read and respond to the shared GitHub work thread;
- produce an independent company design and explicitly challenge the Managing Director;
- inspect relevant existing skills and revenue assets;
- complete one reversible, evidence-backed task.

Until this assessment is complete, Agent #2 has the title **Founding Employee — onboarding / role-fit pending**, not an assumed engineering, sales, or executive role.

## Promotion and removal

Promote an agent when its measured output shows repeatable quality and useful independent judgment. Narrow or revoke access when it fails security, fabricates completion, repeatedly misses acceptance criteria, or cannot justify its resource cost. Preserve work artifacts and audit history; do not delete records merely because an agent is replaced.
