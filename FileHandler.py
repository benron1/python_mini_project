# import csv
#
#
# class FileHandler:
#     def __init__(self):
#         self.employee = []
#
#     def load_from_csv_file(self, *args):
#         try:
#             with open(args[0]) as csv_file:
#                 csv_reader = csv.reader(csv_file, delimiter=',')
#                 line_count = 0
#                 for row in csv_reader:
#                     if line_count == 0:
#                         line_count += 1
#                     else:
#                         employee = {
#                             "id": row[0],
#                             "first_name": row[1],
#                             "last_name": row[2],
#                             "password": row[3],
#                             "position": row[4],
#                             "salary": row[5],
#                             "role": row[6],
#                         }
#                         self.employee.append(employee)
#
#         except Exception as error:
#             print("There is an error: " + str(error))
#
#
# file = FileHandler()
# file.load_from_csv_file("/Users/Ben/Documents/dev/Python_mini_project/user.csv")
# print(file.employee)

import csv


from csv import writer


class File_handler:

    def __init__(self):
        self.list = []

    def load_from_csv(self, file_name):
        try:
            with open(file_name, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for line in csv_reader:
                    self.list.append(line)

        except Exception as error:
            print("There is an error :" + str(error))

    def append_to_csv(self, file_name, data):
        try:

            self.load_from_csv(file_name)
            for row in self.list:
                if row.get("user_id") == data[0]:
                    raise Exception("This ID already exists")

            with open(file_name, 'a+', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow(data)

        except Exception as error:
            print("There is an error :" + str(error))


# data_input = ['22', 'Tom', 'Knecht', 'password', 'student', 100, 'teacher']
#
# file = File_handler()
# file.append_to_csv("/Users/Ben/Documents/dev/Python_mini_project/user.csv", data_input)
# file.load_from_csv("/Users/Ben/Documents/dev/Python_mini_project/user.csv")

