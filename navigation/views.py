from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
    return render(request, 'navigation/home.html')

@login_required
def profilepage(request):
    return redirect('profilepage/profilepage.html')

#@login_required                #new
#def chat(request):
#    return redirect('/chat/')

#@login_required                #new
#def settings(request):
#    return redirect('/settings/')
