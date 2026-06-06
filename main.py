import argparse
from models import Person, User, Project, Task
from utils.create_csv import save_data, load_data

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

# task = Task.create_new_task("Create cli", "Work In Progress", "Dude")
# print(task)
# print(Task.all_tasks_list())
# print(task.status)

def add_user(args):
    user = User.create_new_user(args.name, args.email)
    print(user)
    save_data()

def list_users(args):
    if not User.all_users:
        print("No users")
        return
    for user in User.all_users:
        print(user)

def add_project(args):
    project = Project.create_new_project(args.title, args.description, args.due_date)
    print(project)
    save_data()

def list_projects(args):
    if not Project.all_projects:
        print("No projects")
        return
    for project in Project.all_projects:
        print(project)

def add_task(args):
    task = Task.create_new_task(args.title, args.status, args.assigned_to)
    print(task)
    save_data()

def list_tasks(args):
    if not Task.all_tasks:
        print("No tasks")
        return
    for task in Task.all_tasks:
        print(task)

def complete_task(args):
    for task in Task.all_tasks:
        if task.title == args.title:
            task.status = "Completed"
            print("Task Completed")
            save_data()
            return
    print("No task found")

def main():
    load_data()

    parser = argparse.ArgumentParser(description="User, Project, Task CLI")
    subparsers = parser.add_subparsers()

    add_user_parser = subparsers.add_parser("add-user")
    add_user_parser.add_argument("name")
    add_user_parser.add_argument("email")
    add_user_parser.set_defaults(func=add_user)

    list_users_parser = subparsers.add_parser("list-users")
    list_users_parser.set_defaults(func=list_users)

    add_project_parser = subparsers.add_parser("add-project")
    add_project_parser.add_argument("title")
    add_project_parser.add_argument("description")
    add_project_parser.add_argument("due_date")
    add_project_parser.set_defaults(func=add_project)

    list_projects_parser = subparsers.add_parser("list-projects")
    list_projects_parser.set_defaults(func=list_projects)

    add_task_parser = subparsers.add_parser("add-task")
    add_task_parser.add_argument("title")
    add_task_parser.add_argument("status")
    add_task_parser.add_argument("assigned_to")
    add_task_parser.set_defaults(func=add_task)

    list_tasks_parser = subparsers.add_parser("list-tasks")
    list_tasks_parser.set_defaults(func=list_tasks)

    complete_task_parser = subparsers.add_parser("complete-task")
    complete_task_parser.add_argument("title")
    complete_task_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()