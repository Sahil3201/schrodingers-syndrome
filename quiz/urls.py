from django.conf.urls import url, include
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "quiz"

urlpatterns = [
    path("", views.instructions.as_view(), name="instructions"),
    path("instructions/", views.instructions.as_view(), name="instruction"),
    path("quiz/", views.quiz_page, name="quiz"),
    # path("quiz/get_time_for_question",
    #     views.get_time_for_question,
    #     name="get_time_for_question",),
    # path(
    #     "login",
    #     LoginView.as_view(
    #         template_name="quiz/login.html",
    #         redirect_field_name="quiz",
    #         redirect_authenticated_user=True,
    #     ),
    #     name="login",
    # ),
    path("login/", views.login.as_view(), name="login"),
    path('logout/',views.logout.as_view(), name='logout'),
]
