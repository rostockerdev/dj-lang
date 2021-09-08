from django.contrib import admin

from course.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "date", "price"]


admin.site.register(Course, CourseAdmin)
