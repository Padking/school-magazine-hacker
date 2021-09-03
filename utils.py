"""Содержит дополнительные возможности в виде:

- функции исправления плохих оценок Фролова Ивана,
- функции удаления замечаний Голубева Феофана,
- функции создания похвалы от учителя

"""

import os
import random

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from datacenter.models import Commendation, \
                              Lesson, \
                              Schoolkid


def fix_marks(schoolkid):
    exhaust = schoolkid.mark_set.filter(points__in=[2, 3]).update(points=5)

    return f'Number of rows matched: {exhaust}'


def remove_chastisements(schoolkid):
    chastisements_by_pupil = schoolkid.chastisement_set.all()
    exhaust = chastisements_by_pupil.delete()

    return f'About deleted entries: {exhaust}'


def create_commendation(first_and_last_name, subjects_name):
    commendations_contents = [
        'Я поражён!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!'
    ]

    commendation_content = random.choice(commendations_contents)

    ivan_pupil = Schoolkid.objects.filter(full_name__contains=first_and_last_name).first()

    lessons_of_concrete_classroom = Lesson.objects.filter(year_of_study=6, group_letter='А')
    lessons_of_concrete_classroom_by_subject = lessons_of_concrete_classroom.filter(subject__title=subjects_name)

    first_comer_lesson = lessons_of_concrete_classroom_by_subject.order_by('?').first()

    commendation = Commendation.objects.create(
        text=commendation_content,
        created=first_comer_lesson.date,
        schoolkid=ivan_pupil,
        subject=first_comer_lesson.subject,
        teacher=first_comer_lesson.teacher
    )

    return f'Created commendation for {ivan_pupil.full_name} by {subjects_name} to {first_comer_lesson.date}'


def main():

    first_and_last_name = 'Фролов Иван'
    subject = "Музыка"

    create_commendation(first_and_last_name, subject)


if __name__ == '__main__':
    main()
