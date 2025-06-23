from django.shortcuts import render
from .models import abexam

# Create your views here.

def abexam_step6(request):
    exams = abexam.objects.filter(is_public=True)
    return render(request, 'abexam_step6.html', {
        'exams': exams,
    })