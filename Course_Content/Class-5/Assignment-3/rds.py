all_student_info = {}
class Admin:
    def __init__(self,admin_person, admin_id):
        self.admin_person = admin_person
        self.admin_id = admin_id
    def add_info(self, student_name,student_id, semester_name, courses):
        """Adds the info of a student added by the admin person 
        Input : 'Name of a student' : student_name (str)
                'Student ID' : student_id (int)
                'Semester Name' : semester_name (str)
                'Number of courses' : courses (list)
        
        Output : Returns a Dictionary containing Information for every student added by the admin person
        """
        self.student_name = student_name
        self.student_id = student_id
        student_info = {}
        self.semester_name = semester_name
        self.courses = courses
        if student_id not in student_info:
            student_info.update({student_id : {"Student Name" : student_name,"Semester Name" : semester_name,"Courses" : courses}})

        else:
            print("Student is already added")   
        all_student_info.update(student_info)
        return student_info
    
    def update_cgpa(self,student_id, grades):
        """Updates the info of a student added by the admin person 
        Input : 'Student ID' : student_id (int)
                'Grades of that student' : grades (list)
        
        Output : Returns a Dictionary with the updated Information for every student added by the admin person
        """
              /// Your Code Goes Here      
    def info(self):
        
        return all_student_info