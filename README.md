# summative-lab-python-project-management-cli-tool
# Project Management CLI

## Setup
pip install -r requirements.txt

## Commands
- python main.py add-user "Name" "email@email.com"
- python main.py list-users
- python main.py add-project "Title" "Description" "Due Date"
- python main.py list-projects
- python main.py add-task "Title" "Status" "Assigned To"
- python main.py list-tasks
- python main.py complete-task "Title"

## Python Project Management CLI Tool 

- Create and manage users, projects, and tasks.
- Display and search projects assigned to specific users.
- Use file IO to persist data locally.
- Use pip to manage external packages (e.g., for pretty printing, date formatting, or input validation).
- Structure code using modules, classes, and object relationships.
- Document, test, and debug your solution.

## The Scenario: Create a Command-Line Project Management Tool, The system must support:

- Create and list users via the command line.
- Add projects to specific users and display their associated projects.
- Assign tasks to projects and mark them as complete.
- Edit and persist project/task data using file I/O.
- Navigate the tool with clear, user-friendly CLI commands.
- Manage data relationships like one-to-many (users to projects) and many-to-many (projects to tasks with contributors).
- Create and manage users, projects, and tasks.

## Tools and Resources
- Python 3.10+
- VS Code (or IDE of your choice)
- Git + GitHub
- Python Standard Library (argparse, os, json, etc.
- Optional: External packages such as rich or python-dateutil