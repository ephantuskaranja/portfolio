from django.contrib import admin

# Register your models here.


from portfolio.models import Profile, Education, Skills, Contacts, Projects


admin.site.register(Profile)
admin.site.register(Projects)
admin.site.register(Skills)
admin.site.register(Contacts)
admin.site.register(Education)