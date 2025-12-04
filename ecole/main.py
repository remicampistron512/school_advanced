#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une école
"""

from business.school import School
from models.student import Student


def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans notre école
--------------------------""")

    school: School = School()

    # initialisation d'un ensemble de cours, enseignants et élèves composant l'école
    school.init_static()

    # affichage de la liste des cours, leur enseignant et leurs élèves
    school.display_courses_list()

    print("----- AFFICHAGE DE COURS PAR LEUR ID -----")
    print(school.get_course_by_id(7))
    print ("")
    print("----- AFFICHAGE D'ÉTUDIANTS PAR LEUR ID ----- ")
    print(school.get_student_by_id(1))
    print("")
    print("----- AFFICHAGE DE PROFESSEUR PAR LEUR ID ----- ")
    print(school.get_teacher_by_id(4))
    print("")
    print("----- AFFICHAGE DE L'ADRESSE PAR LEUR ID ------")
    print(school.get_address_by_id(1))
    print("")

    print("----- AFFICHAGE DE TOUS LES PROFESSEURS-----")
    teachers = school.get_all_teachers()
    for teacher in teachers:
        print(teacher)
    print("")

    print("----- AFFICHAGE DE TOUS LES ÉTUDIANTS-----")
    students = school.get_all_students()

    for student in students:
        print(student)

    print("")

    print("----- AFFICHAGE DE TOUS LES COURS-----")
    courses = school.get_all_courses()

    for course in courses:
        print(course)
    print("")





    '''student1 = Student("charles", "xavier", 18)

    if school.create_student(student1):
        print("Étudiant créé")
    else:
        print("Échec de la creation de l'étudiant")'''

    student_to_modify =  school.get_student_by_id(1)
    student_to_modify.age = 77
    school.update_student(student_to_modify)

    # school.delete_student(18)

if __name__ == '__main__':
    main()
