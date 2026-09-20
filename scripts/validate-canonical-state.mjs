import { readFile } from 'node:fs/promises';

const path = 'PROJECT-STATE-MONY-CANONICAL.json';
const raw = await readFile(path, 'utf8');
let state;
const failures = [];
try { state = JSON.parse(raw); } catch { console.log(JSON.stringify({status:'FAILED',canonicalFile:path,failures:['invalid_json']},null,2)); process.exit(1); }
const required = ['version','state_revision','project','updated_at','objective','status','active_workstream','blocked_by','next_actions','evidence','commit_sha'];
for (const key of required) if (!(key in state)) failures.push('missing:'+key);
if (state.project !== 'MONY') failures.push('project_must_be_MONY');
if (!Number.isInteger(state.version) || state.version < 1) failures.push('invalid_version');
if (typeof state.state_revision !== 'string' || !state.state_revision) failures.push('invalid_state_revision');
if (typeof state.updated_at !== 'string' || Number.isNaN(Date.parse(state.updated_at))) failures.push('invalid_updated_at');
for (const key of ['objective','status','active_workstream','commit_sha']) if (typeof state[key] !== 'string' || !state[key]) failures.push('invalid:'+key);
if (!/^[a-f0-9]{40}$/.test(state.commit_sha)) failures.push('invalid_commit_sha');
for (const key of ['blocked_by','next_actions','evidence']) if (!Array.isArray(state[key])) failures.push('invalid_array:'+key);
if (Array.isArray(state.evidence)) {
  const hashes = new Set();
  for (const [i,e] of state.evidence.entries()) {
    if (!e || typeof e !== 'object') { failures.push('evidence_not_object:'+i); continue; }
    for (const key of ['source_name','source_url','observed_at','retrieved_at','claim','evidence_hash','status']) if (typeof e[key] !== 'string' || !e[key]) failures.push('evidence_missing_'+key+':'+i);
    if (typeof e.source_url === 'string' && !/^https:\/\//.test(e.source_url)) failures.push('evidence_source_url_not_https:'+i);
    if (typeof e.observed_at === 'string' && Number.isNaN(Date.parse(e.observed_at))) failures.push('evidence_invalid_observed_at:'+i);
    if (typeof e.retrieved_at === 'string' && Number.isNaN(Date.parse(e.retrieved_at))) failures.push('evidence_invalid_retrieved_at:'+i);
    if (typeof e.evidence_hash === 'string' && !/^sha256:[a-f0-9]{64}$/.test(e.evidence_hash)) failures.push('evidence_invalid_hash:'+i);
    if (e.provider_event_id !== null && e.provider_event_id !== undefined && typeof e.provider_event_id !== 'string') failures.push('evidence_invalid_provider_event_id:'+i);
    if (hashes.has(e.evidence_hash)) failures.push('duplicate_evidence_hash:'+i); hashes.add(e.evidence_hash);
  }
}
if (state.status === 'COMPLETED' && state.evidence.length === 0) failures.push('completed_state_requires_evidence');
console.log(JSON.stringify({status:failures.length?'FAILED':'PASSED',canonicalFile:path,failures,evidenceCount:Array.isArray(state.evidence)?state.evidence.length:0},null,2));
if (failures.length) process.exit(1);
