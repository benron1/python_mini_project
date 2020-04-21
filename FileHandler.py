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
                if row.get("id") == data[0]:
                    raise Exception("This ID already exists")

            with open(file_name, 'a+', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow(data)

        except Exception as error:
            print("There is an error :" + str(error))

    def remove_from_csv(self, file_name, id):
        try:
            f = open(file_name, 'r+')
            file_content = list(csv.reader(f))
            counter = 0

            for row in file_content:
                counter += 1
                if row[0] == id:
                    file_content.remove(row)
                    break

                with open(file_name, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(file_content)
                    return counter

            if counter == len(file_content):
                print('No ID found')

        except Exception as error:
            print("There is an error :" + str(error))

    def update_csv(self, file_name,id,row):
        try:
            self.remove_from_csv(file_name,id)
            self.append_to_csv(file_name, row)

        except Exception as error:
            print("There is an error :" + str(error))



data_input = ['21', 'Tom', 'Jones', 'password', 'student', 100, 'teacher']

file = File_handler()
# file.append_to_csv("/Users/Ben/Documents/dev/Python_mini_project/user.csv", data_input)
# file.load_from_csv("/Users/Ben/Documents/dev/Python_mini_project/user.csv")
# file.remove_from_csv("/Users/Ben/Documents/dev/Python_mini_project/user.csv", "9")
file.update_csv("/Users/Ben/Documents/dev/Python_mini_project/user.csv", "21", data_input)

