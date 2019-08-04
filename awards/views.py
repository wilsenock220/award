from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from .forms import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
    return render(request, 'index.html', locals())


def home(request):
    return render(request, 'home.html', locals())


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    form = LoginForm
    return render(request, '.html', locals())


@login_required(login_url='/accounts/login/')
def upload_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.save()
            return redirect('home')
    else:
        form = ProjectForm()

    return render(request, 'upload_project.html', locals())


def profile(request, username):

    profile = User.objects.get(username=username)
    print(profile.id)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    user = request.user
    profile = User.objects.get(username=username)
    project = Project.objects.filter(owner=user)
    title = f'@{profile.username} awwward projects and screenshots'

    return render(request, 'profile.html', locals())


def edit(request):
    profile = User.objects.get(username=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('update_profile')
    else:
        form = ProfileForm()
    return render(request, 'edit_profile.html', locals())


def search_results(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        searched_project = Project.search_by_project(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', locals())

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
        rating = round(
            ((project.design + project.usability + project.content) / 3), 2)
        if request.method == 'POST':
            form = VoteForm(request.POST)
            if form.is_valid:
                if project.design == 1:
                    project.design = int(request.POST['design'])
                else:
                    project.design = (project.design +
                                      int(request.POST['design'])) / 2
                if project.usability == 1:
                    project.usability = int(request.POST['usability'])
                else:
                    project.usability = (project.design +
                                         int(request.POST['usability'])) / 2
                if project.content == 1:
                    project.content = int(request.POST['content'])
                else:
                    project.content = (project.design +
                                       int(request.POST['content'])) / 2
                project.save()
        else:
            form = VoteForm()
    except DoesNotExist:
        raise Http404()
    return render(request, "project.html", {
        'form': form,
        'project': project,
        'rating': rating
    })


def vote_project(request, project_id):
    project = Project.objects.get(id=project_id)
    rating = round(
        ((project.design + project.usability + project.content) / 3), 2)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid:
            if project.design == 1:
                project.design = int(request.POST['design'])
            else:
                project.design = (project.design +
                                  int(request.POST['design'])) / 2
            if project.usability == 1:
                project.usability = int(request.POST['usability'])
            else:
                project.usability = (project.design +
                                     int(request.POST['usability'])) / 2
            if project.content == 1:
                project.content = int(request.POST['content'])
            else:
                project.content = (project.design +
                                   int(request.POST['content'])) / 2
            project.save()
    else:
        form = VoteForm()
    return render(request, 'vote.html', {
        'form': form,
        'project': project,
        'rating': rating
    })


class ProjectList(APIView):
    def get(self, request, format=None):
        all_proj = Project.objects.all()
        serializers = ProjectSerializer(all_proj, many=True)
        return Response(serializers.data)


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Project.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)
