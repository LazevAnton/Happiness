from django.contrib import admin

from HappinessAPP.models import Members, Teams

admin.site.register([Teams, Members])
