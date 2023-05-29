from django.contrib import admin

from HappinessAPP.models import Members, Teams, HappinessLevel

admin.site.register([Teams, Members])
