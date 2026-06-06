class User:

    all_users = []
    unique_id = 0

    def __init__(self, name, email):
        User.unique_id += 1
        self.id = User.unique_id
        self.name = name
        self.email = email
        User.all_users.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError("Name must be a string")
        self._name = value

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if type(value) is not str:
            raise TypeError("Email must be a string")
        self._email = value

    @classmethod
    def create_new_user(cls, name, email):
        return cls(name, email)
    
    @classmethod
    def all_users_list(cls):
        return cls.all_users
    
    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}"

class Project:

    all_projects = []
    unique_id = 0

    def __init__(self, title, description, due_date):
        Project.unique_id += 1
        self.id = Project.unique_id
        self.title = title
        self.description = description
        self.due_date = due_date
        Project.all_projects.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if type(value) is not str:
            raise TypeError("Title must be a string")
        self._title = value

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if type(value) is not str:
            raise TypeError("description must be a string")
        self._description = value

    @property
    def due_date(self):
        return self._due_date
    
    @due_date.setter
    def due_date(self, value):
        if type(value) is not str:
            raise TypeError("Due date must be a string")
        self._due_date = value

    @classmethod
    def create_new_project(cls, title, description, due_date):
        return cls(title, description, due_date)
    
    @classmethod
    def all_projects_list(cls):
        return cls.all_projects
    
    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}"

class Task:

    all_tasks = []
    unique_id = 0

    def __init__(self, title, status, assigned_to):
        Task.unique_id += 1
        self.id = Task.unique_id
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        Task.all_tasks.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if type(value) is not str:
            raise TypeError("Title must be a string")
        self._title = value

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        if type(value) is not str:
            raise TypeError("Status must be a string")
        self._status = value

    @property
    def assigned_to(self):
        return self._assigned_to
    
    @assigned_to.setter
    def assigned_to(self, value):
        if type(value) is not str:
            raise TypeError("Assigned to must be a string")
        self._assigned_to = value

    @classmethod
    def create_new_task(cls, title, status, assigned_to):
        return cls(title, status, assigned_to)
    
    @classmethod
    def all_tasks_list(cls):
        return cls.all_tasks
    
    def __str__(self):
        return f"Title: {self.title}\nStatus: {self.status}\nAssigned to: {self.assigned_to}"
