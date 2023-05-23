# BootStack GitHub actions

These actions are meant to be used for unifying lint, unit and functional tests,
charm and snap releases, and sonar integration in GitHub workflows. At the same time,
workflows that can be directly used will also be found in this repo.

## Repo configuration workflow

## Charm release workflow

## Snap release workflow
This workflow builds and releases a snap to the Snap Store after passing lint, unit and
functional tests. The triggering workflow (from the source repo) can specify one or multiple
channel(s) as an input when calling the reusable workflow to properly release the snap.

## Pull request workflow

## Sonar workflow

For the workflow to be fully functional, you must complete the following steps.

### Registration

1. Go to [sonarcloud](https://sonarcloud.io/sessions/new) and register with github.
1. After registration, send username to one of the current administrators(
    [Erhan Sunar](mailto:erhan.sunar@canonical.com)
    [Robert Gildein](mailto:robert.gildein@canonical.com)
    [Sudeep Bhandari](mailto:sudeep.bhandari@canonical.com)
    ).
1. We will add you to bootstack-devops project as Admin
1. From now on you will be able to add projects.


### Adding Sonar Projects

1. From the top right corner press the (+) icon.
1. Then press “Analyze new project”
1. From the bottom right corner press “create a project manually”
1. Select the bootstack-devops as organization and enter the “Project key” and
   “Display name” as our project name in github.
1. Press “Set Up”
1. Continue “With Github Actions”
1. Go to Github project and add secret shown in previous page
1. On the second step **do not** copy the file, but use the [sonar.yaml][1] from this
   repo
1. On github, create an [access token][2] for yourself with following permissions
   - pull-requests: read *# allows SonarCloud to decorate PRs with analysis results*
1. Add this token as a secret in github project as `GH_TOKEN` like step 7


### Project Changes

1. Change relevant parts to create **coverage.xml** with 
   **tests/unit/report/coverage.xml** path
   1. First add **--cov-report=xml** to unit tests. Example (tox.ini)
      ```ini
      [testenv:unit]
      commands = pytest {toxinidir}/tests/unit \
          {posargs:-v --cov --cov-report=term-missing --cov-report=html --cov-report=xml}
      ```

1. Then add coverage parts to you configuration. Example (pyproject.yaml)
    ```yaml
    [tool.coverage.run]
    relative_files = true

    [tool.coverage.xml]
    output = "tests/unit/report/coverage.xml"
    ```

1. Add **sonar-project.properties** file. Example:
   ```properties
    sonar.python.version=3
    sonar.projectKey=your-project-name
    sonar.organization=bootstack-devops
    sonar.python.coverage.reportPaths=tests/unit/report/coverage.xml
    sonar.sources = src/
    sonar.tests = tests/
    sonar.test.inclusions = test/**
    sonar.coverage.exclusions=tests/**, docs/**, contrib/**, snap/**, *
    ```

---
[1]: https://github.com/canonical/bootstack-actions/blob/main/.github/workflows/sonar.yaml
[2]: https://docs.github.com/en/actions/security-guides/automatic-token-authentication#permissions-for-the-github_token