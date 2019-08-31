from rds import Admin
admin_person = Admin("Novish", 250) 
admin_person.add_info("Anik", 1410542042, "FALL'14", ["CSE115","MAT116","ENG102"])
admin_person.add_info("Sujit", 1420412042, "SUM'14", ["CSE115","MAT116","ENG102"])
print(admin_person.info())
student_info = admin_person.info()
message = ""
class Student:
    def __init__(self, user_name, user_pass):
        self.user_name = user_name
        self.user_pass = user_pass
    def login(self,student_id, user_pass):
        if student_id in student_info and self.user_name == student_id and self.user_pass == user_pass:
            message = "You have logged in successfully \n"
            print(message + "Your Info is : " + str(Admin.info(Admin)[self.user_name]))
        else:
            print(self.user_name, student_id, self.user_pass, user_pass)
            message = "Invalid user_name or password"
            print(message + " Please enter valid login credential")
        return message