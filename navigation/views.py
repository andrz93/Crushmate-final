from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profilepage.models import ProfilePhoto

@login_required
def profilepage(request):
    return redirect('profilepage/profilepage.html')

@login_required                                                                                 #new
def homepage(request):                                                                              #new
    main_photo = ProfilePhoto.objects.filter(user=request.user, is_main=True).first()           #new
    return render(request, 'navigation/home.html', {'main_photo': main_photo})                  #new
