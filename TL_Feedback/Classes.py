# CLASSES

# 1 # Feedback
class Feedback:
    def __init__(self, date, student, writtenFeedback, grade):
        self.date = date 
        self.student = student 
        self.writtenFeedback = writtenFeedback
        self.grade = grade
    def __str__(self):
        output = f'-*- FEEDBACK CLASS -*-\n'
        output += f'Date: {self.date}\n'
        output += f'Student: {self.student}\n'
        output += f'Written Feedback: {self.writtenFeedback}\n'
        output += f'TL Grade: {self.grade}  '

        return output
    def __repr__(self):
        return str(self)

# 2 # Student
class Student:
    def __init__(self, name, studentFeedback = [], tl_ratings = [], student_avg_tlrating = 'n/a'):
        self.name = name
        self.studentFeedback = studentFeedback
        self.tl_ratings = tl_ratings
        self.student_avg_tlrating = student_avg_tlrating
    def get_student_AVG_rating(self):
        if len(self.tl_ratings) != 0:
            count = 0
            for i in self.tl_ratings:
                count += int(i)

            self.student_avg_tlrating = count / len(self.tl_ratings)
            return self.student_avg_tlrating

    def __str__(self):
        output = f'-*- STUDENT CLASS -*-\n'
        output += f'Name: {self.name}\n'
        output += f'Student Feedback: {self.studentFeedback} \n {len(self.studentFeedback)} entries\n'
        output += f'TL Ratings: {self.tl_ratings} \n {len(self.tl_ratings)} entries \n'
        output += f'AVG TL Rating: {self.student_avg_tlrating}'

        return output
    def __repr__(self):
        return str(self)