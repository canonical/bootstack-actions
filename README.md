# BootStack GitHub actions

These actions are meant to be used for unifying lint, unit and functional tests,
and charm and snap releases in GitHub workflows. At the same time,
workflows that can be directly used will also be found in this repo.

## Repo configuration workflow

## Charm release workflow

## Snap release workflow
This workflow builds and releases a snap to the Snap Store after passing lint, unit and
functional tests. The triggering workflow (from the source repo) can specify one or multiple
channel(s) as an input when calling the reusable workflow to properly release the snap.
