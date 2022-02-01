#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Initiator of the model and the selected functions
'''
from student import Student
from subject import Subject
from classroom import Classroom


def test_1():
    '''
    Case_use 2 - 3: Average and not graded.
    '''

    # Sadly a subject can't be registered if it doesn't exist
    S1.add_course('Algo')
    # S1.add_course('bio', 12)
    print('For student 1: ')
    print(S1.avg_grade_student())  # Case 2
    print(S1.not_graded())  # Case 3
    print(S1.get_grades())
    print('For student 2: ')
    print(S2.get_grades())
    print(S2.not_graded())
    print(S2.avg_grade_student())


def test_2():
    '''
    Case_Use 1, calculating average of each subject on its own.
    '''

    print(Maths.all_subj_grades())
    print(Maths.avg_subj_grade())
    print(Biol.avg_subj_grade())
    print(Chimie.avg_subj_grade())  # 2 subs but only one grade
    print(Geography.avg_subj_grade())  # Grades not available.


def test_3():
    '''
    Set a class room to maths
    Willing to change a classroom? Need authentication
    '''
    Maths.set_classroom(salle_info_1)
    Maths.set_classroom(salle_info_2)


def test_4():
    '''
    Tying to modify a note on a subject that a student hasn't been enrolled to
    '''
    S1.set_note(Maths, 20)
    S1.set_note(Geography, 20)
    print(S1.get_grades())


'''
Let's begin the test by supposing we have 4 different subjects.
(Maths, Biol, Chimie, Geography) and 2 students.
It's not obgligatory that all students have taken all the subjects.
'''
if __name__ == '__main__':
    Maths = Subject('Maths')
    Biol = Subject('Biologie')
    Chimie = Subject('Chimie')
    Geography = Subject('Geography')
    salle_info_1 = Classroom('B_0_11', '50')
    salle_info_2 = Classroom('B_0_10', '40')
    S1 = Student('Freeman', 'Morgan', '0611144333', 'mg@gmail.com', 2018)
    S2 = Student('Green', 'John', '0513932869', 'jg@gmail.com', 2020)
    S1.add_course(Maths, 10)
    S1.add_course(Chimie, 20)
    S2.add_course(Maths, 20)
    S2.add_course(Biol, 12)
    S2.add_course(Chimie)
    test_1()
    test_2()
    # test_3()
    test_4()
