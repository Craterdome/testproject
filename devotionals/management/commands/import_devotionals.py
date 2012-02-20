import datetime
import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import safe

from devotionals.models import Devotional

class Command(BaseCommand):
    args = '<file_path, file_path...>'
    help = 'Imports devotionals from file path'

    def handle(self, *args, **options):
        for d in Devotional.objects.all():
            d.delete()
        for file_path in args:
            now = datetime.datetime.now()
            reader = csv.reader(open(file_path, 'rb'), delimiter=',', quotechar='"')
            for row in reader:
                if row[1] == 'day': continue #skip first row

                created_date = datetime.datetime(year=now.year, month=int(row[2]), day=int(row[1]))
                body = row[3]
                body = body.replace('&lt;', '<').replace('&gt;', '>')
                Devotional.objects.create(created_date=created_date, title=row[0], body=body)
