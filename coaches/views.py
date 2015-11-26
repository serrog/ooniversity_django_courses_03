from django.shortcuts import render
from coaches.models import Coach

def detail(request, coach_id):
    coach = Coach.objects.get(pk=coach_id)
    context = {'coach': coach}
    return render(request, 'coaches/detail.html', context)