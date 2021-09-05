import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from datacenter.models import (
    Commendation,
    Lesson,
    Schoolkid
)


def get_schoolkid(last_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=last_name)
    except Schoolkid.DoesNotExist as e:
        msg = (
            'Ошибка! '
            f"Проверьте фамилию и имя '{last_name}' на правописание"
        )
        raise ValueError(msg) from e
    except Schoolkid.MultipleObjectsReturned as e:
        msg = (
            'Ошибка! '
            f"Точно применять скрипт для него: '{last_name}'?"
        )
        raise ValueError(msg) from e

    return schoolkid


def fix_marks(schoolkid):
    updated_marks_count = (schoolkid.mark_set.filter(points__in=[2, 3])
                           .update(points=5))

    return f'Кол-во обновлённых оценок в БД: {updated_marks_count}'


def remove_chastisements(schoolkid):
    chastisements_by_schoolkid = schoolkid.chastisement_set.all()
    deleted_chastisements_count = chastisements_by_schoolkid.delete()

    return f'Следующие замечания удалены из БД: {deleted_chastisements_count}'


def create_commendation(last_name, subjects_name):
    commendations_contents = [
        'Я поражён!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!'
    ]

    commendation_content = random.choice(commendations_contents)

    schoolkid = get_schoolkid(last_name)
    lessons_of_concrete_classroom = (Lesson.objects
                                     .filter(year_of_study=6,
                                             group_letter='А'))
    lessons_of_concrete_classroom_by_subject = (lessons_of_concrete_classroom
                                                .filter(subject__title=subjects_name))

    if not lessons_of_concrete_classroom_by_subject:
        raise ValueError('Ошибка! Проверьте название предмета')

    first_comer_lesson = (lessons_of_concrete_classroom_by_subject
                          .order_by('?').first())

    commendation = Commendation.objects.create(text=commendation_content,
                                               created=first_comer_lesson.date,
                                               schoolkid=schoolkid,
                                               subject=first_comer_lesson.subject,
                                               teacher=first_comer_lesson.teacher)

    msg = (
        f'Создана похвала {commendation} по предмету: '
        f'{subjects_name} {first_comer_lesson.date}'
    )
    return msg


def main():

    last_name = 'Фролов Иван'
    subject = 'Музыка'

    schoolkid = get_schoolkid(last_name)

    print(fix_marks(schoolkid))
    print(remove_chastisements(schoolkid))
    print(create_commendation(last_name, subject))


if __name__ == '__main__':
    main()
