from django.urls import include, path

from .views import UserListView, UserDetailView, UserCreate


app_name = "connection"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
	path('create-users/', UserCreate.as_view(), name='user-create'),
    path('users-list/', UserListView.as_view()),
    path('user/<int:pk>', UserDetailView.as_view()),
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
]
