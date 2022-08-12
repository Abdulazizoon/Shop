from django.urls import path


from .views import CustomUserAPIView, log_in, signup, log_out

urlpatterns = [
    path('', CustomUserAPIView.as_view(), name='user_api'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('register/', signup, name='register')
]