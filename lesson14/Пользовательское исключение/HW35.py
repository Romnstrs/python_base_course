class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, age:{self.age}, gender:{self.gender}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, {self.record_book}'


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise Exception("Достигнуто максимумальное количество студентов в группе ")


    def delete_student(self, last_name):
        res = self.find_student(last_name)
        self.group.discard(res)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name== last_name :
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += f'{str(student)}\n'
        return f'Number:{self.number}\n{all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', '1')
st2 = Student('Female', 25, 'Liza', 'Taylor', '2')
st3 = Student("Male", 22, "Roman", "Strus", "3")
st4 = Student("Male", 22, "Roma", "Strus", "4")
st5 = Student("Male", 22, "Rom", "Strus", "5")
st6 = Student("Male", 22, "Ro", "Strus", "6")
st7 = Student("Male", 22, "R", "Strus", "7")
st8 = Student("Male", 22, "Roman", "Strus", "8")
st9 = Student("Male", 22, "Roman", "Stru", "9")
st10 = Student("Male", 22, "Roman", "Str", "10")
st11 = Student("Male", 22, "Roman", "St", "11")

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
try:
    gr.add_student(st11)
except Exception as e:
    print(e)
print(gr)
print(gr.find_student('Jobs'))
print(gr.find_student('Jobs2'))
gr.delete_student('Jobs')
gr.delete_student('Jobs2')
print(gr)