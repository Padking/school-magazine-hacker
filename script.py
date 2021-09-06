import argparse
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


def create_parser():
    description = (
        'Исправляет оценки, '
        'удаляет замечания, '
        'создаёт похвалу.'
    )
    help_to_full_name_argument = 'Фамилия и имя друга, например, Фролов Иван'
    help_to_subject_argument = 'Название предмета для похвалы, например, Математика'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('full_name', help=help_to_full_name_argument, nargs=2)
    parser.add_argument('subject', help=help_to_subject_argument, nargs=1)

    return parser


def get_schoolkid(full_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
    except Schoolkid.DoesNotExist:
        invalid_full_name_msg = (
            'Ошибка! '
            f"Проверьте фамилию и имя '{full_name}' на правописание"
        )
        return invalid_full_name_msg
    except Schoolkid.MultipleObjectsReturned:
        invalid_full_name_msg = (
            'Ошибка! '
            f"Точно применять скрипт для него: '{full_name}'?"
        )
        return invalid_full_name_msg

    return schoolkid


def fix_marks(schoolkid):
    updated_marks_count = (schoolkid.mark_set.filter(points__in=[2, 3])
                           .update(points=5))

    return f'Кол-во обновлённых оценок в БД: {updated_marks_count}'


def remove_chastisements(schoolkid):
    chastisements_by_schoolkid = schoolkid.chastisement_set.all()
    deleted_chastisements = chastisements_by_schoolkid.delete()

    return f'Следующие замечания удалены из БД: {deleted_chastisements}'


def create_commendation(schoolkid, subjects_name):
    commendations_contents = [
        'Я поражён!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!'
    ]

    commendation_content = random.choice(commendations_contents)

    lessons_of_concrete_classroom = (Lesson.objects
                                     .filter(year_of_study=6,
                                             group_letter='А'))
    lessons_of_concrete_classroom_by_subject = (lessons_of_concrete_classroom
                                                .filter(subject__title=subjects_name))

    if not lessons_of_concrete_classroom_by_subject:
        return 'Ошибка! Проверьте название предмета'

    first_comer_lesson = (lessons_of_concrete_classroom_by_subject
                          .order_by('?').first())

    commendation = Commendation.objects.create(text=commendation_content,
                                               created=first_comer_lesson.date,
                                               schoolkid=schoolkid,
                                               subject=first_comer_lesson.subject,
                                               teacher=first_comer_lesson.teacher)

    success_created_commendation_msg = (
        f'Создана похвала {commendation} по предмету: '
        f'{subjects_name} {first_comer_lesson.date}'
    )
    return success_created_commendation_msg


def main():
    parser = create_parser()
    args = parser.parse_args()
    full_name, subject = ' '.join(args.full_name), *args.subject

    schoolkid = get_schoolkid(full_name)

    if isinstance(schoolkid, Schoolkid):
        print(fix_marks(schoolkid))
        print(remove_chastisements(schoolkid))
        print(create_commendation(schoolkid, subject))
    else:
        print(schoolkid)  # Сообщение об ошибке


if __name__ == '__main__':
    main()
