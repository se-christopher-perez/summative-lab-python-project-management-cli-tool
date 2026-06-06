from models import User, Project, Task

dude = User.create_new_user("Dude", "dude@email.com")
print(dude)
print(User.all_users_list())

cli = Project.create_new_project("cli", "Learn Python", "6/5/2026")
print(cli)
print(Project.all_projects_list())

task = Task.create_new_task("Create cli", "Work In Progress", "6/20/2026")
print(task)
print(Task.all_tasks_list())