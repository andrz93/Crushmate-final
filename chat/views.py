from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponseForbidden
from .models import Message
from match.models import Match
from django.contrib.auth.models import User

@login_required
def chat_room(request, username):
    recipient = get_object_or_404(User, username=username)

    # 確認是否有 Match
    is_matched = Match.objects.filter(
        Q(user1=request.user, user2=recipient) | Q(user1=recipient, user2=request.user)
    ).exists()

    if not is_matched:
        return HttpResponseForbidden("You can only chat with matched users.")

    # 發送訊息
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Message.objects.create(sender=request.user, recipient=recipient, content=content)

    # 顯示歷史訊息
    messages = Message.objects.filter(
        Q(sender=request.user, recipient=recipient) |
        Q(sender=recipient, recipient=request.user)
    ).order_by("timestamp")

    return render(request, "chat/chat_room.html", {
        "recipient": recipient,
        "messages": messages
    })

@login_required
def user_list(request):
    # 找出所有有 match 的對象
    matches = Match.objects.filter(
        Q(user1=request.user) | Q(user2=request.user)
    )
    matched_users = [
        match.user2 if match.user1 == request.user else match.user1
        for match in matches
    ]
    return render(request, "chat/user_list.html", {"users": matched_users})
