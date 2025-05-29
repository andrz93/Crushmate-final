from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Message
from django.contrib.auth.models import User
from match.models import Match  # 確保你有這個模型
from django.http import HttpResponseForbidden

@login_required
def chat_room(request, username):
    recipient = get_object_or_404(User, username=username)

    # 檢查雙方是否有配對
    is_matched = Match.objects.filter(
        Q(user1=request.user, user2=recipient) | Q(user1=recipient, user2=request.user)
    ).exists()

    if not is_matched:
        return HttpResponseForbidden("You can only chat with matched users.")

    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Message.objects.create(sender=request.user, recipient=recipient, content=content)

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
    matches = Match.objects.filter(
        Q(user1=request.user) | Q(user2=request.user)
    )
    matched_users = [
        match.user2 if match.user1 == request.user else match.user1
        for match in matches
    ]
    return render(request, "chat/user_list.html", {"users": matched_users})