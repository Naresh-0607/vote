from django.shortcuts import render,HttpResponse, redirect
from .forms import SignupForm, VoteForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages

# Create your views here.
def landing(request):
    return render(request, 'voting/landing.html')

@login_required
def profile(request):
    
    return render(request, 'voting/profile.html', {'profile': request.user.profile})

def sign_up(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/profile')
    else:
        form = SignupForm()

    return render(request, 'registration/sign-up.html', {'form' : form})

def log_out(request):
    logout(request)
    return redirect('/login')

def error(request):
    return render(request, 'voting/error.html')

@login_required
def DoVote(request):
    profile = request.user.profile
    if profile.is_voted:
        return render(request, 'voting/error.html')
    if request.method == 'POST':
        form = VoteForm(request.POST, instance=profile)
        if form.is_valid():
            voted = form.save(commit=False)
            voted.is_voted = True
            voted.save()
            return redirect('/profile')
    else:
        form = VoteForm(instance=profile)
    return render(request, 'voting/actualVote.html', {'form': form})

@login_required
def view_votes(request):
    if request.user.is_superuser:
        c1_votes = Profile.objects.filter(candidates='C1')
        c2_votes = Profile.objects.filter(candidates='C2')
        c3_votes = Profile.objects.filter(candidates='C3')
        c4_votes = Profile.objects.filter(candidates='C4')
    else:
        messages.warning(request, "You are not allowed to visit that page")
        return redirect('/profile')
    return render(request, 'voting/all_votes.html', {'c1_votes': c1_votes, 'c2_votes': c2_votes, 'c3_votes': c3_votes, 'c4_votes': c4_votes})