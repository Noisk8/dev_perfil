from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cv.pdf", views.cv_pdf, name="cv_pdf"),
]
