from django.contrib import admin
from .models import ADD_JOB,Category,Reveiw
# Register your models here
class category_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(ADD_JOB)
admin.site.register(Category, category_admin)
admin.site.register(Reveiw)
