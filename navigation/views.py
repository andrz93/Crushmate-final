from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profilepage.models import ProfilePhoto
from django.contrib.auth.models import User
from match.models import Match, Like
from django.db.models import Q

@login_required
def profilepage(request):
    return redirect('profilepage/profilepage.html')

@login_required
def homepage(request):
    current_user = request.user

    # 找出已經 Like 過的人
    liked_user_ids = Like.objects.filter(from_user=current_user).values_list('to_user_id', flat=True)

    # 過濾掉自己、已配對、已 like 的人
    matched_user_ids = Match.objects.filter(Q(user1=current_user) | Q(user2=current_user)).values_list('user1_id', 'user2_id')
    matched_ids_flat = set(sum(matched_user_ids, ()))  # 展平成單一 list

    # 推薦對象 = 除了自己 + 沒配對過 + 沒按過 like
    recommended_users = User.objects.exclude(id__in=liked_user_ids).exclude(id__in=matched_ids_flat).exclude(id=current_user.id)

    # 取得他們的大頭貼
    recommendations = []
    for user in recommended_users:
        main_photo = ProfilePhoto.objects.filter(user=user, is_main=True).first()
        recommendations.append({
            'user': user,
            'photo': main_photo
        })

    return render(request, 'navigation/home.html', {
        'recommendations': recommendations,
    })

@login_required
def like_user(request, user_id):
    if request.method == "POST":
        is_liked = request.POST.get("is_liked") == "true"
        to_user = get_object_or_404(User, id=user_id)

        Match.objects.create(from_user=request.user, to_user=to_user, is_liked=is_liked)

        # 如果對方也喜歡你，就建立聊天室（可用訊息或自動觸發）
        if is_liked:
            mutual_like = Match.objects.filter(from_user=to_user, to_user=request.user, is_liked=True).exists()
            if mutual_like:
                # 你可以通知用戶或顯示聊天室連結，這邊簡單跳過
                pass

    return redirect('home')