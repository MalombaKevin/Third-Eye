from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from third_eye_app.forms import Add_Profile_Form, Business_Form, Post_Form

from third_eye_app.models import Business, Profile_thirdeye, User_Posts

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts = User_Posts.objects.all()
    business =Business.objects.all()
    return render(request, 'index.html', {'posts': posts, "mabiz":business})

#Profile
@login_required(login_url='/accounts/login/')  
def profile(request):
    if Profile_thirdeye.objects.filter(user_id=request.user.id).exists():
        profile = Profile_thirdeye.objects.get(user_id=request.user.id)
        posts = User_Posts.objects.filter(user_id = request.user.id).all()
        biashara = Business.objects.filter(user_id = request.user.id).all()
    else:
        profile = None
        posts= None

    
    return render(request, 'profile.html', {'profile': profile,'posts': posts, "mabiz":biashara})

#add new Profile

@login_required(login_url='/accounts/login/')   
def add_profile(request):
    if request.method == 'POST':
        form = Add_Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = Add_Profile_Form()

    return render(request, 'add/add_profile.html', {'form': form})


# add a business
@login_required(login_url='/accounts/login/')
def add_biashara(request):
    if request.method == 'POST':
        form = Business_Form(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit = False)
            business.user = request.user
            business.save()
            return redirect ('index')
    else:
        form = Business_Form()
    
    return render (request, 'add/add_business.html', {'form': form})


# add post
@login_required(login_url='/accounts/login/')
def add_post(request):
    if request.method == 'POST':
        form = Post_Form(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit = False)
            business.user = request.user
            business.save()
            return redirect ('index')
    else:
        form = Post_Form()
    
    return render (request, 'add/add_posts.html', {'form': form})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'biz' in request.GET and request.GET["biz"]:
        search_term = request.GET.get("biz")
        business = Business.search_business(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {'mabiz':business, 'message':message})
    else:
    
        return render(request, 'search.html')




