from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Position, Worker

admin.site.register(Position)


class WorkerAdmin(UserAdmin):
   fieldsets = UserAdmin.fieldsets + (
       ("Position", {'fields': ('position',)}),
   )

admin.site.register(Worker, WorkerAdmin)
