import csv

from rich import print
from models import User, Project, Task

if __name__ == "__main__":

    def save_data():

        dude = User.create_new_user("Dude", "dude@email.com")

        cli = Project.create_new_project("cli", "Learn Python", "6/5/2026")

        task = Task.create_new_task("Create cli", "Work In Progress", "6/20/2026")

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

    # def load_data():
    #     try:

    #         with open("data/user_data.csv", "r") as file:
    #             reader = csv.reader(file)

    #             for row in reader:
    #                 id, name, email

    #     except FileNotFoundError:
    #         print("[red]❌ file not found[/red]")

    save_data()