import time
from definedroles import Roles


class User():
    def __init__(self):
        self._users = [{'username': "admin", 'password': "admin"}, {
            'username': "user1", 'password': "user1"}]
        self._roles = {'key': []}
        pass

    def add_user_details(self, username, password):
        if not any(usernames['username'] == username for usernames in self._users):
            self._users.append({'username': username, 'password': password})
            time.sleep(1)
            print("Congrats User Created Successfully")
            return 0
        else:
            print("User already exists Please create another user")
            return 1

    def check_user_pass(self, username, password):
        dict = {'username': username, 'password': password}
        if dict not in self._users:
            print("Userid or password incorrect Please try again")
            return 1
        else:
            return 0

    def assign_roles_users(self, username, roles):
        self._roles[username] = roles
        print("Inserted successfully")
        print(username)
        print(self._roles.get(username))

    def get_roles_users(self, username):
        print(username)
        print(self._roles.get(username))

    def has_access(self, username, resourse, action):
        init_roles = Roles()
        get_roles = init_roles.get_roles()
        dict = {'resource': resourse, 'action': action}
        print(dict)
        x = False
        for roles in self._roles.get(username):
            if roles in get_roles:
                if dict in get_roles.get(roles):
                    print("You can access this resource")
                    x = True
                    break
        if not x:
            print("You cannot access this resource")
