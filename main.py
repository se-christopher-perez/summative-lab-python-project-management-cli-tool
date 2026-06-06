import argparse
from models import Person, User, Project, Task

# gal = Person("Gal", "gal@email.com")
# print(gal)

# dude = User.create_new_user("Dude", "dude@email.com")
# print(dude)
# print(User.all_users_list())
# print(dude.email)
# print(dude.id)

# cli = Project.create_new_project("cli", "Learn Python", "6/5/2026")
# print(cli)
# print(Project.all_projects_list())
# print(cli.description)

# task = Task.create_new_task("Create cli", "Work In Progress", "6/20/2026")
# print(task)
# print(Task.all_tasks_list())
# print(task.status)

def add_user(args):
    user = User.create_new_user(args.name, args.email)
    print(user)

def list_users(args):
    if not User.all_users:
        print("No users")
        return
    for user in User.all_users:
        print(user)

def add_project(args):
    project = Project.create_new_project(args.title, args.description, args.due_date)
    print(project)

def list_projects(args):
    if not Project.all_projects:
        print("No projects")
        return
    for project in Project.all_projects:
        print(project)

def add_task(args):
    task = Task.create_new_task(args.title, args.status, args.assigned_to)
    print(task)

def list_tasks(args):
    if not Task.all_tasks:
        print("No tasks")
        return
    for task in Task.all_tasks:
        print(task)

def complete_task(args):
    for task in Task.all_tasks:
        if task.title == args.title:
            task.status = "Complete"
            print("Task Completed")
            return
    print("No task found")

def main():
    pass

if __name__ == "__main__":
    main()