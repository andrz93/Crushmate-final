from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Like, Match
from django.db.models import Q

@login_required
def like_user(request, user_id):
    to_user = get_object_or_404(User, id=user_id)
    from_user = request.user

    # 如果已經按過 Like，就不要重複建立
    like, created = Like.objects.get_or_create(from_user=from_user, to_user=to_user)

    # 檢查對方是否也按過你（形成 Match）
    if Like.objects.filter(from_user=to_user, to_user=from_user).exists():
        # 如果還沒建立 Match，就建立
        match_exists = Match.objects.filter(
            (Q(user1=from_user) & Q(user2=to_user)) | (Q(user1=to_user) & Q(user2=from_user))
        ).exists()
        if not match_exists:
            Match.objects.create(user1=from_user, user2=to_user)

        # 自動導向聊天室（你要確保 chat_room URL name 有設定）
        return redirect('chat_room', username=to_user.username)

    # 如果對方還沒按 like，就回到主頁面
    return redirect('home')