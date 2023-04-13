from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  PostJob ,AppliedJob

# admin.site.register(UserTable)
admin.site.register(PostJob)
# admin.site.register(ProfileStudent)
admin.site.register(AppliedJob)
# admin.site.register(Ranking)
