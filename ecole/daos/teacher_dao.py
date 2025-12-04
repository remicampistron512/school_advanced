# -*- coding: utf-8 -*-

"""
Classe Dao[Teacher]
"""

from models.teacher import Teacher
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class TeacherDao(Dao[Teacher]):
    def create(self, teacher: Teacher) -> int:
        """Crée en BD l'entité Teacher correspondant au Teacher Teacher

        :param teacher: à créer sous forme d'entité Teacher en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        ...
        return 0

    def read(self, id_teacher: int) -> Optional[Teacher]:
        """Renvoie le Teacher correspondant à l'entité dont l'id est id_teacher
           (ou None s'il n'a pu être trouvé)"""
        teacher: Optional[Teacher]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM person INNER JOIN teacher on teacher.id_person = person.id_person WHERE id_teacher=%s"
            cursor.execute(sql, (id_teacher,))
            record = cursor.fetchone()
        if record is not None:
            teacher = Teacher(record['first_name'], record['last_name'], record['age'],record['hiring_date'])
            teacher.id = record['id_teacher']
        else:
            teacher = None

        return teacher


    def read_all(self) ->  list[Teacher]:
        """
        Renvoie tous les Teachers
        :return:
        """
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM person INNER JOIN teacher on teacher.id_person = person.id_person"
            cursor.execute(sql)
            records = cursor.fetchall()

        teachers: list[Teacher] = []

        for record in records:
            teacher = Teacher(
                first_name=record["first_name"],
                last_name=record["last_name"],
                age=record["age"],
                hiring_date=record["hiring_date"],
            )
            teacher.id = record["id_teacher"]
            teachers.append(teacher)

        return teachers



    def update(self, teacher: Teacher) -> bool:
        """Met à jour en BD l'entité Teacher correspondant à teacher, pour y correspondre

        :param teacher: teacher  déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...
        return True

    def delete(self, teacher: Teacher) -> bool:
        """Supprime en BD l'entité Teacher correspondant à teacher

        :param teacher: teacher  dont l'entité Teacher correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
        return True
