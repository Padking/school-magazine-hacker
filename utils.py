"""Вызывает функцию исправления оценок Ивана."""

import os

import django


def fix_marks(schoolkid):
    exhaust = schoolkid.mark_set.filter(points__in=[2, 3]).update(points=5)

    return f'Number of rows matched: {exhaust}'


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    django.setup()

    from datacenter.models import Schoolkid

    ivan_pupil = Schoolkid.objects.filter(full_name__contains='Фролов Иван').first()

    fix_marks(ivan_pupil)


if __name__ == '__main__':
    main()
