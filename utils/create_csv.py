import csv

from rich import print
from models import User, Project, Task

def save_data():

    userData = "user_data.csv"

    try:

        with open(f"data/{userData}", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["ID", "Name", "Email"])
            for user in User.all_users:
                writer.writerow([user.id, user.name, user.email])

        print(f"[green]✅ {userData} Saved[/green]")

    except FileNotFoundError:
        print("[red]❌ file not found[/red]")

    projectData = "project_data.csv"

    try:

        with open(f"data/{projectData}", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["ID", "Title", "Description", "Due_date"])
            for project in Project.all_projects:
                writer.writerow([project.id, project.title, project.description, project.due_date])

        print(f"[green]✅ {projectData} Saved[/green]")

    except FileNotFoundError:
        print("[red]❌ file not found[/red]")

    taskData = "task_data.csv"

    try:

        with open(f"data/{taskData}", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["ID", "Title", "Status", "Assigned_to"])
            for task in Task.all_tasks:
                writer.writerow([task.id, task.title, task.status, task.assigned_to])

        print(f"[green]✅ {taskData} Saved[/green]")

    except FileNotFoundError:
        print("[red]❌ file not found[/red]")

def load_data():
    try:
            
        with open(f"data/user_data.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                User.create_new_user(row["Name"], row["Email"])

    except FileNotFoundError:
        print("[red]❌ file not found[/red]")

    try:
            
        with open(f"data/project_data.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Project.create_new_project(row["Title"], row["Description"], row["Due_date"])

    except FileNotFoundError:
        print("[red]❌ file not found[/red]")

    try:
            
        with open(f"data/task_data.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Task.create_new_task(row["Title"], row["Status"], row["Assigned_to"])

    except FileNotFoundError:
        print("[red]❌ file not found[/red]")

    # save_data()
    # load_data()