from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm
from .models import ProfilePhoto
from django.views.decorators.http import require_POST


@login_required
def profile_page(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            existing_main = ProfilePhoto.objects.filter(user=request.user, is_main=True).exists()    
            photo = ProfilePhoto.objects.create(user=request.user, image=image)   
            if not existing_main:           
                photo.is_main = True        
                photo.save()
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

@require_POST       
def set_main_photo(request, photo_id):       
    photo = get_object_or_404(ProfilePhoto, id=photo_id, user=request.user)

    # 把所有照片設為非主圖片
    ProfilePhoto.objects.filter(user=request.user, is_main=True).update(is_main=False)

    # 把這張設為主圖片
    photo.is_main = True
    photo.save()

    return redirect('profilepage')