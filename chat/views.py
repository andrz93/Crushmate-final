from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Message
from django.contrib.auth.models import User

@login_required
def chat_room(request, username):
    recipient = get_object_or_404(User, username=username)

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
    users = User.objects.exclude(username=request.user.username)
    return render(request, "chat/user_list.html", {"users": users})
