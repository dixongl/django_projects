import csv
from unesco.models import Site, Category, States, Region, Iso

Category.objects.all().delete()
Site.objects.all().delete()
States.objects.all().delete()
Region.objects.all().delete()
Iso.objects.all().delete()

with open('unesco/whc-sites-2018-small.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        try:
            c = Category.objects.get(name=row[7])
        except:
            c = Category(name=row[7])
            c.save()
        try:
            st = States.objects.get(name=row[8])
        except:
            st = States(name=row[8])
            st.save()
        try:
            r = Region.objects.get(name=row[9])
        except:
            r = Region(name=row[9])
            r.save()
        try:
            i = Iso.objects.get(name=row[10])
        except:
            i = Iso(name=row[10])
            i.save()
        try:
            y = int(row[3])
        except:
            y = None
        try:
            lo = float(row[4])
        except:
            lo = None
        try:
            la = float(row[5])
        except:
            la = None
        try:
            ah = float(row[6])
        except:
            ah = None
        site = Site(name=row[0], description=row[1], justification=row[2],year = y, longitude=lo, latitude=la, area_hectares=ah, category=c, states=st, region=r, iso=i)
        site.save()
