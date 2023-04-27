from django.contrib import admin
from .models import Branch, Manager, Ticket

admin.site.register(Ticket)
admin.site.register(Manager)
admin.site.register(Branch)
# Register your models here.
