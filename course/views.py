from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import CourseEntry  # ← 加這一行！
import json

@login_required
def course_schedule_view(request):
    user = request.user
    if request.method == 'POST':
        data = request.POST.get('course_data')
        if data:
            CourseEntry.objects.filter(user=user).delete()
            entries = json.loads(data)
            for key, name in entries.items():
                try:
                    day, period = map(int, key.split('_'))
                    CourseEntry.objects.create(user=user, day=day, period=period, course_name=name)
                except:
                    continue
    entries = CourseEntry.objects.filter(user=user)
    table_data = {f"{e.day}_{e.period}": e.course_name for e in entries}
    return render(request, 'course/course.html', {
        'table_data': table_data,
        'period_range': list(range(1, 10)),
        'days': list(range(5)),
    })

@login_required
def course_suggestions(request):
    day = request.GET.get('day')
    period = request.GET.get('period')
    if not day or not period:
        return JsonResponse([], safe=False)
    suggestions = (CourseEntry.objects
                   .filter(day=day, period=period)
                   .exclude(course_name='')
                   .values_list('course_name', flat=True)
                   .distinct())
    return JsonResponse(list(suggestions), safe=False)
