class User:

    all_users = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.all_users.append(self)

    @classmethod
    def create_new_user(cls, name, email):
        return cls(name, email)
    
    @classmethod
    def all_users_list(cls):
        return cls.all_users

class Project:

    all_projects = []

    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        Project.all_projects.append(self)

    @classmethod
    def create_new_project(cls, title, description, due_date):
        return cls(title, description, due_date)
    
    @classmethod
    def all_projects_list(cls):
        return cls.all_projects

class Task:

    all_tasks = []

    def __init__(self, title, status, assigned_to):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        Task.all_tasks.append(self)

    @classmethod
    def create_new_task(cls, title, status, assigned_to):
        return cls(title, status, assigned_to)
    
    @classmethod
    def all_tasks_list(cls):
        return cls.all_tasks
