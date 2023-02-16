from django.urls import path
from .import views
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('student/form/', views.studentForm, name="student-form"),
    path('student/register/', views.studentRegister, name="student-register"),
    path('student/view/', views.showStudent, name="student-view"),
    path('student/edit/<int:pk>', views.editStudent, name="student-edit"),
    path('student/update/', views.updateStudent, name="student-update"),
    path('student/delete/<int:pk>', views.deleteStudent, name="student-delete"),
    path('course/code/', views.fetch_course_code, name="course-code"),
    path('batch/form/', views.batchForm, name="batch-form"),
    path('batch/create/', views.createBatch, name="batch-create"),
    path('batch/edit/<int:pk>', views.editBatch, name="batch-edit"),
    path('batch/update/', views.updateBatch, name="batch-update"),
    path('batch/view/', views.viewBatch, name="batch-view"),
    path('batch/delete/<int:pk>', views.deleteBatch, name="batch-delete"),
    path('course/form/', views.courseForm, name="course-form"),
    path('course/register/', views.registerCourse, name="course-register"),
    path('course/view/', views.showCourse, name="course-view"),
    path('course/edit/<int:pk>', views.editCourse, name="course-edit"),
    path('course/update/', views.updateCourse, name="course-update"),
    path('course/delete/<int:pk>', views.deleteCourse, name="course-delete"),
]
