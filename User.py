from FileHandler import File_handler


class User:

    def __init__(self):
        self.handler = File_handler()

    def user_auth(self, name, password):
        try:
            self.handler.load_from_csv("/Users/Ben/Documents/dev/Python_mini_project/user.csv")

            access = False
            user_role = ' '

            for row in self.handler.list:
                if name == row['first_name'] and password == row['password']:
                    access = True
                    user_role = str(row['role'])
                    break

            if access:
                print('Access Granted')
                print(f'Your role is {user_role}')
                return access

            else:
                print('Access Denied')
                return access

        except Exception as error:
            print("There is an error :" + str(error))


User.__init__(User)
User.user_auth(User, 'amir', '12345678')
