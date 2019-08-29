from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render, redirect
from .forms import UserForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from django.http import JsonResponse


def MyProfileView(request):
    if request.user.is_anonymous is True:
        return redirect('Task:login')

    return render(request, 'Task/profile.html', {'current_user': request.user})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserFormView(View):
    template_name = 'Task/registration_form.html'
    form_class = UserForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)

            # clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # pass in the password
            user.set_password(password)
            # save user to database
            user.save()

            # check in database to see if they exist
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # redirect to another page
                    return redirect('home')

        return render(request, self.template_name, {'form': form})


def home(request):
    if request.user.is_anonymous is True:
        return redirect('login')
    template = 'Task/home.html'
    return render(request, template)


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'Task/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'Task/simple_upload.html')


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)
