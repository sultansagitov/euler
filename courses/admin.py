from django.contrib import admin
from .models import *


admin.site.register(CourseType)
admin.site.register(Course)
admin.site.register(Level)
admin.site.register(Question)
admin.site.register(Answer)