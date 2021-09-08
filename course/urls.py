from django.urls import path
from django.urls.conf import include

from course.views import CourseView

app_name = "course"

urlpatterns = [path("", CourseView.as_view(), name="course")]
