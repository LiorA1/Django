import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from many.models import Person, Course, Membership


def run():
    fhandler = open('many/load.csv') # open an handler to the file
    reader = csv.reader(fhandler)    # Initilize a CSV reader, from the handle.
    next(reader)  # Advance past the header row

    # Erase all the data.
    Person.objects.all().delete()
    Course.objects.all().delete()
    Membership.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        p, created = Person.objects.get_or_create(email=row[0]) # DISTINCT (unique) email field
        c, created = Course.objects.get_or_create(title=row[2]) # DISTINCT (unique) title field

        # Returns a tuple of (object, created),
        #  where object is the retrieved or created object
        #  and created is a boolean specifying whether a new object was created.
        #
        # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#get-or-create

        r = Membership.LEARNER
        if row[1] == 'I':
            r = Membership.INSTRUCTOR
        m = Membership(role=r, person=p, course=c)

        m.save() # save it to the DB





