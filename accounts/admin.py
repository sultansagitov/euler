from django.contrib import admin
from .models import Student, FriendRequest, FriendNotification


admin.site.register(Student)
admin.site.register(FriendRequest)
admin.site.register(FriendNotification)
