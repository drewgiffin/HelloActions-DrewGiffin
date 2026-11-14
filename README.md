# Lab 11: Hello GitHub Actions

A small Python project for learning the basics of GitHub Actions.

hello.py prints a greeting using the name in the WHO_TO_GREET environment variable, and falls back to "GitHub Actions Student" if it is not set. The workflow in .github/workflows/hello.yml runs the script on GitHub's servers whenever code is pushed to main, or manually from the Actions tab, and shows the output in the workflow log.

## Questions

What is the purpose of the on section?
The on section defines which events trigger the workflow.

What does workflow_dispatch do?
workflow_dispatch enables the workflow to be run manually.

What does runs-on specify?
runs-on specifies which type of machine the job runs on. 

Why is actions/checkout needed?
The runner starts without the code, so it must copy the correct commit.

What does the language setup action do?
The language setup action installs and configures a specific version of the language that will be used in the workflow.

What is the difference between compiling and running the program?
Compiling turns the source code into an executable, running the program is using this executable.

Where can you see the program output?
You can see the program output in the github actions section of this repository.

What is the difference between a workflow, a job, and a step?
A workflow can perform multiple jobs at once, a job may have one or more steps constituting it, a step is a single command or action within a job.
