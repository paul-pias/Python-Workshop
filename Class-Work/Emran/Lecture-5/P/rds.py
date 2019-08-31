class Admin:
    global all_info
    all_info = {}


    def __init__(self, uname, id):
        self.name = uname
        self.id = id

    def add_info(self, stu_name, stu_id, sem_name, courses):
        """Adds the info of a student added by the admin
        Input: 'Name of a student' : stu_name (str)
               'Student ID' : stu_id (int)
               'Semester name' : sem_name (str)
               'Number of courses' : courses (list)

        Output: Returns a dictionary containing information for every student by the admin"""

        self.stu_name=stu_name
        self.stu_id=stu_id
        self.stu_name=sem_name
        self.courses=courses

        stu_info={}

        if stu_id not in stu_info:
            stu_info.update(
                {"Student name" : stu_name,
                 "Semester name" : sem_name,
                 "Courses" : courses
                }
            )
        else:
            print("Student is already added")
        all_info.update(stu_info)

    def info(self):
        return all_info
    