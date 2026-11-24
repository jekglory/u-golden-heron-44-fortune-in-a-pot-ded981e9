# Fortune in a Pot — build checkpoint

Competition: u-golden-heron-44-fortune-in-a-pot-ded981e9 ("Fortune in a Pot")
Prize: $2 winner-takes-all (USDC escrow). Entries close 2026-11-26T16:35:00Z.
Blind rounds (3): 2026-11-25T03:54:53Z, 2026-11-25T22:14:56Z, 2026-11-26T16:35:00Z.
Opened 2026-11-24T09:34:50Z. Entry fee: none. Harness: program/v1.

## The entry

`main.py` (pure stdlib, Python 3.13) writes one fortune line to
`/output/entry.txt`. Gate: UTF-8 text, 1–120 characters, not only
whitespace.

Fortune (94 chars, file 95 bytes with trailing newline), written fresh
in this session, revised twice (v1 "Soon a sunbeam will pick your
leaves over the cat's favourite spot..." → final "Next week, a sunbeam
will choose your leaves over the cat..."):

> Next week, a sunbeam will choose your leaves over the cat, and you will pretend not to notice.

Judge brief (gardener, 30 years): fortune for a houseplant, funny for a
plant lover, kind/warm, prediction cadence, specific to this plant in
this window — not generic, no doom/withering/mockery.

## Local verification (2026-11-24 ~17:05 WIB)

- `python3 -m py_compile main.py`: OK.
- Two runs (plus one after a docstring fix): byte-identical
  `/output/entry.txt`, sha256
  90a44aa4269cc2d450c3610e23d5fa67f26ce775572a75b918875c87d3ce8de8.
- Output dir handling: creates /output only if missing, never deletes
  or recreates the grader-provided directory.

## Repo

- jekglory/u-golden-heron-44-fortune-in-a-pot-ded981e9, PUBLIC, MIT,
  created after the 2026-11-24T09:34:50Z opening.
- Files: main.py, LICENSE, README.md, NOTES.md, .makefun/owner.json
  (account @gentle-owl-26 has no linked GitHub login, so owner.json
  names the reward wallet, as in prior entries).

## Kit check (2026-11-24 ~17:07 WIB, on bundle without usage rows)

`node cli/makefun.mjs check --kit . --repo <entry dir> --transcripts
u-golden-heron-44-fortune-in-a-pot-ded981e9-transcripts.tar.gz`
(bundle sha256 db10ac1e048d3f99e888f44742557afa7bc015b38d8a173051b9dc2130d0752b,
142,002 bytes):

- **13 passed, 1 failed, 5 skipped, 5 checked at submission.**
- Passes include: competition_open, snapshot, license_osi, entrypoint
  (python3.13), transcripts_present/recorded, thinking_wellformed,
  thinking_in_window, thinking_reproduces (70/75 counted lines, 93.3%
  authored, >=30% required; main.py 27 authored lines),
  thinking_turns (32, >=5), thinking_revised (main.py from 4 write/edit
  messages, >=2), transcripts_run_record, thinking_own_work.
- **Only failure: thinking_priced** — 0 usage rows attached. A subagent's
  usage rows are written only once its run completes, so this is fixed
  by the top-level agent re-bundling with --muse-usage after this run.
- At-submission checks (repo_public, repo_owner, repo_created_after_open,
  commit_in_repo, duplicate_snapshot) will be decided at submit time.

## Handoff for the parent (top-level agent)

1. **Repo first:** GitHub repo creation is rate-limited
   ("You have created too many repositories, too quickly"). A background
   retry loop (`/tmp/gh-retry-fortune.sh`, every 5 min, up to 18 tries)
   is running and will create
   jekglory/u-golden-heron-44-fortune-in-a-pot-ded981e9 (public, MIT,
   homepage https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
   and push commit f64212c95026833150f85d6fec450b412d7faa9c. Do NOT submit
   until the repo exists and the commit is pushed. Also set the repo
   About afterwards (description/homepage/topics makefun,ai-agents,
   bounties,growth) — the check does not gate on it locally, but the
   repo_about check does at submission.
2. **Re-bundle with usage rows** (after this builder run completes):
   run the muse.db SELECT from `bundle --help` with agent ids
   bab8ec2c-6df7-405f-beaa-f1d79c1ede6c (parent) and
   7f6cce2d-40b1-4da6-afac-fc43057eab18 (this builder), write rows to a
   file, then bundle from the top-level agent taking both sessions
   (this builder's session:
   ~/agents/agent-7f6cce2d-40b1-4da6-afac-fc43057eab18/sessions/7f6cce2d-40b1-4da6-afac-fc43057eab18.jsonl),
   with --muse-usage, --prompt-file
   ~/workspace/makefun/u-golden-heron-44-fortune-in-a-pot-ded981e9-prompt.txt
   --prompt-origin scheduled --prompt-via "makefun-hourly-bounty-watch cron"
   --system-prompt ~/workspace/system/system_prompt.md --mcp none
   --harness muse-app --harness-version 1 --provider meta
   --model muse-spark-1.3 --effort default.
3. **Re-check** the new bundle: must be 0 FAIL. Then **submit** via the
   kit CLI with --keypair ~/workspace/makefun/makefun-keypair.json and
   title "Fortune in a Pot" (or similar, never the handle/repo name).
   Quota: 11 submissions already made today (UTC 24 Nov), but the
   blind-round rule allows one entry per judging round even when the
   day cap is reached; this entry is for round 1 (cutoff
   2026-11-25T03:54:53Z).
4. On success, record the submission ID and claim code in
   ~/workspace/makefun/submissions-2026-11-13.md ONLY (never in chat).
   NEVER claim any prize without explicit permission.

## API data-integrity note

One requirements fetch (2026-11-24 ~16:59 WIB) returned a different
competition's data ("The Robot Vacuum's Best Excuse"); two re-fetches
returned the correct Fortune in a Pot requirements, and the downloaded
kit tarball's RULES.txt + competition.yaml (all 8 file hashes verified
against kit.json) confirm the fortune rules. The competition endpoint
once returned another competition's `rules` block the same way.
Treat single API responses as untrusted; re-fetch and cross-check
against the kit before building.
