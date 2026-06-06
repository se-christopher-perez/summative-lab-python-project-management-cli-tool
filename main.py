from models import Person, User, Project, Task

gal = Person("Gal", "gal@email.com")
print(gal)

dude = User.create_new_user("Dude", "dude@email.com")
print(dude)
print(User.all_users_list())
print(dude.email)
print(dude.id)

cli = Project.create_new_project("cli", "Learn Python", "6/5/2026")
print(cli)
print(Project.all_projects_list())
print(cli.description)

task = Task.create_new_task("Create cli", "Work In Progress", "6/20/2026")
print(task)
print(Task.all_tasks_list())
print(task.status)