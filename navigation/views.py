#navigation/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profilepage.models import ProfilePhoto

@login_required
def profilepage(request):
    return redirect('profilepage/profilepage.html')

@login_required
def homepage(request):
    photos = ProfilePhoto.objects.filter(user=request.user)
    main_photo = photos.filter(is_main=True).first()
    return render(request, 'navigation/home.html', {
        'photos': photos,
        'main_photo': main_photo,
    })