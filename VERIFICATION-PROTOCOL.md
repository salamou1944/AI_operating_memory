# Verification Protocol

For every material task:

- `PLANNED`: intended but not executed.
- `EXECUTED`: tool action succeeded.
- `VERIFIED`: independent read/test confirms the result.
- `BLOCKED`: external dependency or permission prevents completion.
- `FAILED`: execution occurred but the intended result was not achieved.

Required loop:

`inspect -> act -> observe -> verify -> record -> report`

For code changes, verify the changed file and run the narrowest available test/workflow. For infrastructure changes, verify configuration and deployment status. For external actions, verify the returned provider evidence. Never convert `EXECUTED` into `VERIFIED` without a separate observation.
