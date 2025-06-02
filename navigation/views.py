# navigation/views.py
from profilepage.models import ProfilePhoto
from match.models import Like, Match
from bio.models import UserBio
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    # 排除目前使用者自己
    other_users = User.objects.exclude(id=request.user.id)

    recommendations = []
    for user in other_users:
        # 排除已 Like 或已 Match 的人
        if Like.objects.filter(from_user=request.user, to_user=user).exists():
            continue
        if Match.objects.filter(user1=request.user, user2=user).exists() or \
           Match.objects.filter(user1=user, user2=request.user).exists():
            continue

        # 主照片
        main_photo = ProfilePhoto.objects.filter(user=user, is_main=True).first()
        # 其他照片（排除主圖）
        other_photos = ProfilePhoto.objects.filter(user=user, is_main=False)

        # 使用者自我介紹與系所
        try:
            bio_obj = UserBio.objects.get(user=user)
            bio = bio_obj.bio
            department = bio_obj.department
        except UserBio.DoesNotExist:
            bio = ""
            department = ""

        if main_photo:  # 有主圖才推薦
            recommendations.append({
                "user": user,
                "main_photo": main_photo,
                "other_photos": other_photos,
                "bio": bio,
                "department": department,
            })

    return render(request, 'navigation/home.html', {
        "recommendations": recommendations
    })
