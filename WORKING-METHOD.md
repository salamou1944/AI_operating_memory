# Working Method

Default execution pipeline:

`goal -> inspect -> capability selection -> permission check -> execute -> recover -> verify -> record -> next action`

Use existing capabilities first. When a capability is missing or unreliable, invoke the capability-building loop: discover -> verify -> implement -> test -> register -> retry the original task.

Standing constraints:
- keep projects isolated;
- prefer reusable contracts over one-off hacks;
- minimize manual user steps;
- preserve fail-closed behavior for missing providers or permissions;
- maintain explicit fallbacks;
- report blockers precisely instead of looping.
