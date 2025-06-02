from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserBio
import json

@login_required
def bio_settings(request):
    profile, created = UserBio.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile.bio = request.POST.get('bio', '')
        profile.height = request.POST.get('height') or None
        profile.weight = request.POST.get('weight') or None
        profile.department = request.POST.get('department', '')

        interests_raw = request.POST.get('interests_list', '[]')
        profile.interests = json.loads(interests_raw)

        profile.save()
        return redirect('settings')

    return render(request, 'bio/bio.html', {'profile': profile})

