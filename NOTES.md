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

## API data-integrity note

One requirements fetch (2026-11-24 ~16:59 WIB) returned a different
competition's data ("The Robot Vacuum's Best Excuse"); two re-fetches
returned the correct Fortune in a Pot requirements, and the downloaded
kit tarball's RULES.txt + competition.yaml (all 8 file hashes verified
against kit.json) confirm the fortune rules. The competition endpoint
once returned another competition's `rules` block the same way.
Treat single API responses as untrusted; re-fetch and cross-check
against the kit before building.
