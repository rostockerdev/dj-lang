from django.shortcuts import render
from django.views.generic import ListView

from course.models import Course

# def course_view(request):
# return render(request, 'course/course_list.html')


class CourseView(ListView):
    model = Course
    context_object_name = "courses"
    template_name = "course/course_list.html"
