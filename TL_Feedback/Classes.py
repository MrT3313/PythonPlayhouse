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
    def __init__(self, name, studentFeedback = [], tl_ratings = [], student_avg_tlrating = 'n/a', startDate = None, endDate = None):
        self.name = name
        self.studentFeedback = []
        self.tl_ratings = []
        self.student_avg_tlrating = student_avg_tlrating
        self.startDate = startDate
        self.endDate = endDate

    def check_dates(self):
        if self.startDate is not None and self.endDate is not None:
            return False if self.startDate >= self.endDate else True
        else: 
            return True

    def get_student_AVG_rating(self):
        if len(self.tl_ratings) is not 0:
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
        output += f'AVG TL Rating: {self.student_avg_tlrating}\n'
        
        output += f'START DATE: {self.startDate}\n'
        output += f'END DATE: {self.endDate}\n'

        # if self.startDate != None:
        #     output += f'START DATE: {self.startDate}\n'
        # if self.endDate != None:
        #     output += f'END DATE: {self.endDate}\n'

        return output
    def __repr__(self):
        output = ['name', 
            'studentFeedback', 
            'tl_ratings', 
            'student_avg_tlrating',
            'startDate',
            'endDate'
        ]
        return output