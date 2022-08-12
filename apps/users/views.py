from django.shortcuts import render
from rest_framework import status
# from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.urls import reverse



from apps.users.forms import LogInForm, SignUpForm
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """
        Вывод юзера.
        """
        user = CustomUser.objects.all()
        serializer = CustomUserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'sign-up.html', {'form': form})


def log_in(request):
    error = False
    if request.user.is_authenticated:
        return redirect('product_list')
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('product_list')
            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'sign-in.html', {'form': form, 'error': error})


def log_out(request):
    logout(request)
    return redirect(reverse('login'))