from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm
from .models import ProfilePhoto

@login_required
def profile_page(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            ProfilePhoto.objects.create(user=request.user, image=image)
            return redirect('profilepage')
    else:
        form = PhotoForm()

    photos = ProfilePhoto.objects.filter(user=request.user)
    return render(request, 'profilepage/profilepage.html', {'form': form, 'photos': photos})

def delete_photo(request, photo_id):
    photo = get_object_or_404(ProfilePhoto, id=photo_id, user=request.user)
    if request.method == "POST":
        photo.delete()
    return redirect('profilepage')
