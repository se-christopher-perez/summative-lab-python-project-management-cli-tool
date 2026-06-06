import csv
from models import User, Project, Task

if __name__ == "__main__":

    dude = User.create_new_user("Dude", "dude@email.com")

    cli = Project.create_new_project("cli", "Learn Python", "6/5/2026")

    task = Task.create_new_task("Create cli", "Work In Progress", "6/20/2026")

    filename = "user_data.csv"

    try:

        with open(f"data/{filename}", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["ID", "Name", "Email"])
            for user in User.all_users:
                writer.writerow([user.id, user.name, user.email])

            writer.writerow(["ID", "Title", "Description", "Due_date"])
            for project in Project.all_projects:
                writer.writerow([project.id, project.title, project.description, project.due_date])

            writer.writerow(["ID", "Title", "Status", "Assigned_to"])
            for task in Task.all_tasks:
                writer.writerow([task.id, task.title, task.status, task.assigned_to])

        print(f"✅ {filename} Saved")

    except FileNotFoundError:
        print("❌ file not found")