# log-report — Fixed Terminal-Bench Task

This repository contains a repaired Terminal-Bench 2 (Harbor) task: `dynamo/log-report`.

## What I fixed

- `task.toml`: converted to TB2 format (`[[tasks]]`), set artifact path to `/app/report.json`, added `tasks.agent`, `tasks.verifier`, and `tasks.environment` entries.
- `environment/Dockerfile`: pinned to `python:3.11.9-slim-bookworm`, installed test deps, and copies `solution/` and `tests/` into the image.
- Removed leaked reference implementation from the agent image.
- `instruction.md`: added explicit numbered success criteria and JSON output schema.
- `tests/test.sh`: writes verifier outputs to `/logs/verifier/reward.txt` and `/logs/verifier/ctrf.json`.
- `tests/test_outputs.py`: added JSON validation and type checks for all required fields.
- `solution/solve.sh`: fixed to run `/app/solve.py` and made executable in Dockerfile.

## How to run locally (with Harbor installed)

From the `log-report` directory:

```bash
# Run the oracle (reference solution) — should PASS and record reward=1
harbor run -p . -a oracle

# Run the nop agent — should FAIL and record reward=0
harbor run -p . --agent nop
```

Inspect job artifacts after runs under `jobs/` directories. Harbor writes verifier outputs to `/logs/verifier/` inside the environment and copies them to job folders.

## Files changed

- `task.toml`
- `instruction.md`
- `environment/Dockerfile`
- `tests/test.sh`
- `tests/test_outputs.py`
- `solution/solve.sh` (path fix)

## Commit & push (example)

If you want to push to the SSH remote for `khemrajpr92`:

```powershell
# ensure README added
git add README.md
git commit -m "Add README; document fixes and run instructions"
# set or verify origin points to the intended repo
git remote set-url origin git@github.com:khemrajpr92/log-report-oracle-agent.git
git branch -M main
git push -u origin main
```

Or push via HTTPS (ensure you are authenticated as the correct user):

```powershell
git remote set-url origin https://github.com/khemrajpr92/log-report-oracle-agent.git
git push -u origin main
```

If you receive permission errors, authenticate with GitHub CLI or configure SSH keys for the `khemrajpr92` account.

## Notes

- Make the GitHub repo private after you confirm the tests and before submitting
- If you want, I can also generate a small PR body you can paste into GitHub when creating the pull request.

