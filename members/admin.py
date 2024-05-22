from django.contrib import admin
from .models import Member

# Register your models here.

# Set list_display
class MemberAdmin(admin.ModelAdmin):
    list_display = ("lastname", "firstname", "phone", "joined_date")

admin.site.register(Member, MemberAdmin)
