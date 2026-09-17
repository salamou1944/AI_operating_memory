import { readFile } from 'node:fs/promises';

const path = 'PROJECT-STATE-MONY-CANONICAL.json';
const raw = await readFile(path, 'utf8');
const state = JSON.parse(raw);
const required = ['version','project','state','last_verified_at','commit_sha','active_goal','completed_tasks','failed_tasks','known_risks','evidence','next_action'];
const failures = required.filter((key) => !(key in state)).map((key) => `missing:${key}`);
if (state.project !== 'MONY') failures.push('project_must_be_MONY');
if (!Array.isArray(state.completed_tasks) || !Array.isArray(state.failed_tasks) || !Array.isArray(state.known_risks) || !Array.isArray(state.evidence)) failures.push('invalid_array_field');
if (!state.evidence.every((e) => e && e.source && e.status && e.observed_at)) failures.push('evidence_missing_source_status_or_timestamp');
if (state.state === 'completed' && (!state.commit_sha || state.evidence.length === 0)) failures.push('completed_state_requires_exact_commit_and_evidence');
console.log(JSON.stringify({ status: failures.length ? 'FAILED' : 'PASSED', canonicalFile: path, failures }, null, 2));
if (failures.length) process.exit(1);
