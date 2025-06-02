# navigation/views.py
from profilepage.models import ProfilePhoto
from match.models import Like, Match
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    # 排除目前使用者自己
    other_users = User.objects.exclude(id=request.user.id)

    # 取得該使用者的主圖片
    recommendations = []
    for user in other_users:
        # 排除已 Like 或已 Match 的人
        if Like.objects.filter(from_user=request.user, to_user=user).exists():
            continue
        if Match.objects.filter(user1=request.user, user2=user).exists() or \
           Match.objects.filter(user1=user, user2=request.user).exists():
            continue

        # 取得主圖片
        main_photo = ProfilePhoto.objects.filter(user=user, is_main=True).first()
        if main_photo:
            recommendations.append({
                "user": user,
                "photo": main_photo
            })

    return render(request, 'navigation/home.html', {
        "recommendations": recommendations
    })
