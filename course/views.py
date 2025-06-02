from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfileSettings
import json

@login_required
def course(request):
    user_settings, created = UserProfileSettings.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        raw_data = request.POST.get('course_schedule', '{}')
        user_settings.course_schedule = json.loads(raw_data)
        user_settings.save()
        return redirect('course')

    # 建立 context，確保每天都有資料（預設為 9 節空白）
    def get_day_data(day):
        return user_settings.course_schedule.get(day, [""] * 9)

    context = {
    'days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'periods': range(1, 10),
    'course_data': {
        'Mon': get_day_data('Mon'),
        'Tue': get_day_data('Tue'),
        'Wed': get_day_data('Wed'),
        'Thu': get_day_data('Thu'),
        'Fri': get_day_data('Fri'),
    }
}

    return render(request, 'course/course.html', context)
