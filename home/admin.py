from django.contrib import admin
from home.models import Contact, Education, Skill,Project,Experince,About
# Register your models here.
admin.site.register(Contact)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Experince)
admin.site.register(About)