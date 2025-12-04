# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""

from models.student import Student
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class StudentDao(Dao[Student]):
    def create(self, student: Student) -> int:
        """Crée en BD l'entité Course correspondant au cours course

        :param course: à créer sous forme d'entité Course en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        ...
        return 0

    def read(self, id_student: int) -> Optional[Student]:
        """Renvoit le cours correspondant à l'entité dont l'id est id_course
           (ou None s'il n'a pu être trouvé)"""
        student: Optional[Student]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM person INNER JOIN student on student.id_person = person.id_person WHERE student_nbr=%s"
            cursor.execute(sql, (id_student,))
            record = cursor.fetchone()
        if record is not None:
            student = Student(record['first_name'], record['last_name'], record['age'])
            student.id = record['student_nbr']
        else:
            student = None

        return student

    def read_all(self) -> list[Student]:
        """
        Renvoit tous les Teachers
        :return:
        """
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM person INNER JOIN student on student.id_person = person.id_person"
            cursor.execute(sql)
            records = cursor.fetchall()

        students: list[Student] = []

        for record in records:
            student = Student(
                first_name=record["first_name"],
                last_name=record["last_name"],
                age=record["age"],
            )
            student.id = record["student_nbr"]
            students.append(student)

        return students
    
    def update(self, student: Student) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre

        :param course: cours déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...
        return True

    def delete(self, student: Student) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
        return True
