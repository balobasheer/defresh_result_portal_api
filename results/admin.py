from django.contrib import admin

# Register your models here.
from results.models import Classroom, AcademicSession, Subject, AdminComment, Result


admin.site.register(Classroom)
admin.site.register(AcademicSession)
admin.site.register(Subject)
admin.site.register(AdminComment)
admin.site.register(Result)
