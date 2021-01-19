from django.urls import path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import ChoiceList, CreateVote, PollList, PollDetail, PollViewSet, UserCreate, LoginView

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path("login2/", views.obtain_auth_token, name="login2"), # another way to login
]

urlpatterns += router.urls

# >>> from django.contrib.auth.models import User
# >>> from rest_framework.authtoken.models import Token
# >>> user = User.objects.get(pk=pk_of_user_without_token)
# >>> Token.objects.create(user=user)
# <Token: e2b9fa2d4ae27fe1fdcf17b6e37711334d07e167>

# Do a POST with a correct username and password, and you will get a response like this.
# { "token": "c300998d0e2d1b8b4ed9215589df4497de12000c" }

# Add an authorization header Authorization: Token <your token>, and you can access the API.

