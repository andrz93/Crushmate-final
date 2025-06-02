# match/views.py
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from .models import Like, Match
import json

@csrf_exempt
@require_POST
@login_required
def swipe(request):
    data = json.loads(request.body)
    direction = data.get('direction')
    username = data.get('username')

    try:
        to_user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'User not found'}, status=404)

    is_liked = (direction == 'right')

    # 儲存 Like（會更新重複的記錄）
    like_obj, _ = Like.objects.update_or_create(
        from_user=request.user,
        to_user=to_user,
        defaults={'is_liked': is_liked}
    )

    if is_liked:
        # 檢查是否雙向 Like 成功
        mutual_like = Like.objects.filter(
            from_user=to_user,
            to_user=request.user,
            is_liked=True
        ).exists()

        if mutual_like:
            # 用 user id 排序來避免重複
            user1, user2 = sorted([request.user, to_user], key=lambda u: u.id)
            Match.objects.get_or_create(user1=user1, user2=user2)
            return JsonResponse({'status': 'match'})

    return JsonResponse({'status': 'ok'})
