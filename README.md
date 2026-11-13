# Lab 11: Hello GitHub Actions

A small Python project for learning the basics of GitHub Actions.

hello.py prints a greeting using the name in the WHO_TO_GREET environment variable, and falls back to "GitHub Actions Student" if it is not set. The workflow in .github/workflows/hello.yml runs the script on GitHub's servers whenever code is pushed to main, or manually from the Actions tab, and shows the output in the workflow log.
