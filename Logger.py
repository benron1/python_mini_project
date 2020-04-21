import os
import datetime


class Logger:

        def __init__(self, path_to_log_file, log_file_name):
            self.folder_path = path_to_log_file
            self.file_name = log_file_name
            self.full_path = "{}//{}".format(self.folder_path, self.file_name)

        def create_log_entry(self,msg):
            if not os.path.exists(self.folder_path):
                os.makedirs(self.folder_path)

            try:
                f = open(self.full_path, "a+")

            except OSError as e:
                if e.strerror == "No such file or directory exists":
                    f.close()
                    f.open(self.full_path,"w")
                else:
                    print("error:", e.strerror)
            except Exception as e:
                print("Error: Unknown error occured.")
            else:
                date = datetime.datetime.now()
                try:
                    f.write(date.strftime("%y/%m/%Y, %H:%M:%S ") + "{}\n".format(msg))

                except Exception as e:
                    print(e)
                    print("Error: Could not write to file.")
                else:
                    print("Successful")
                f.close()


loging = Logger("logs", "log_file.txt")
loging.create_log_entry("Exercise 5")