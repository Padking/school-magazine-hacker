"""Содержит дополнительные возможности в виде:
- функции исправления плохих оценок Фролова Ивана,
- функции удаления замечаний Голубева Феофана

"""

import os

import django


def fix_marks(schoolkid):
    exhaust = schoolkid.mark_set.filter(points__in=[2, 3]).update(points=5)

    return f'Number of rows matched: {exhaust}'


def remove_chastisements(schoolkid):
    chastisements_by_pupil = schoolkid.chastisement_set.all()
    exhaust = chastisements_by_pupil.delete()

    return f'About deleted entries: {exhaust}'


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    django.setup()

    from datacenter.models import Schoolkid

    feofan_pupil = Schoolkid.objects.filter(full_name__contains='Голубев Феофан').first()

    remove_chastisements(feofan_pupil)

if __name__ == '__main__':
    main()
