# Capability Runtime

This directory turns the capability registry into an executable, policy-gated runtime.

## Modes

- `safe`: normal automation capabilities.
- `lab`: executable security capabilities only against explicitly declared local/lab targets.
- `review`: produces a plan and required approvals without executing.

Dangerous capabilities are **not** exposed as unrestricted host commands. The runtime requires:
1. an explicit capability ID;
2. a declared target/scope;
3. lab mode for security-sensitive capabilities;
4. a policy decision before execution;
5. an audit record.

This follows the principle of separating the full capability universe from the subset currently allowed to execute. OpenAI's current agent guidance likewise recommends separating all available tools from the subset allowed for a particular run. See: https://developers.openai.com/api/docs/guides/latest-model
