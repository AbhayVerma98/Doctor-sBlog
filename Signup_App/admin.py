from django.contrib import admin
from Signup_App.models import Registration, User_details_Model, CategoryModel, BlogModel

# Register your models here.

admin.site.register(Registration)
admin.site.register(User_details_Model)
admin.site.register(CategoryModel)
admin.site.register(BlogModel)
