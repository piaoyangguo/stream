from django.core.management.base import BaseCommand
from stream.models import Student

namelist = ["a", "b", "c", "d"]


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-r", "--reset", dest="reset", action='store_true', default=False,
                            help="reset all cache data.")

    def handle(self, *args, **options):
        if options['reset']:
            print 'starting resset all article list cache'
            alist = []
            for i in range(100000):
                s = Student()
                s.name = namelist[i % 4]
                s.age = i
                alist.append(s)
            Student.objects.bulk_create(alist)
