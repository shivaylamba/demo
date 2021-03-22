from usertypes import User
from getpass import getpass
import time
from definedroles import Roles

if __name__ == '__main__':
    user = User()
    user_name_value = "admin"
    while(True):
        print("######     Main Menu   ########")
        print("Hello Welcome to the RBAC System! You are logged in  as "+user_name_value + '\n')
        if(user_name_value == "admin"):
            val = input(
                " Press 1 to login as another user \n Press 2 for creating New User \n  ")
            if(val == '1'):
                user_name_value_temp = input("Enter Username:")
                password = getpass("Enter Password for " +
                                   user_name_value_temp + ": ")
                if(user.check_user_pass(user_name_value_temp, password) == 0):
                    user_name_value = user_name_value_temp

            if(val == '2'):
                new_user = input("Enter Username:")
                new_passwd = getpass("Enter Password for " + new_user + ": ")
                if(user.add_user_details(new_user, new_passwd) == 0):
                    roles_quantity = int(input(
                        "Enter the number of roles to assign to user"))
                    roles = []
                    while(roles_quantity != 0):
                        role_input = input("Enter roles:")
                        roles.append(role_input)
                        roles_quantity = roles_quantity - 1
                    user.assign_roles_users(new_user, roles)

        else:
            val = input(
                "Press 1 to login as another user \nPress 2 for view roles \n Press 3 for access resource \n ")
            if(val == '1'):
                username = input("Enter Username:\n")
                password = getpass("Enter Password for" + username + ": ")
                user.check_user_pass(username, password)
            if(val == '2'):
                user.get_roles_users(user_name_value)
            if(val == '3'):
                print("Enter resource and action details\n")
                resource = input("Enter resource:- \n")
                action = input("Enter Action:- \n")
                user.has_access(user_name_value, resource, action)
        exit_var = input("To continue press 'y' or to end the program press 'no' \n")
        if(exit_var == 'no'):
            break
