from django.contrib import admin

from unesco.models import Category, State, Region, Site, Iso

admin.site.register(Category)
admin.site.register(State)
admin.site.register(Region)
admin.site.register(Site)
admin.site.register(Iso)
