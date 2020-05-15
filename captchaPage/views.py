from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    return render(req,'captchaPage/index.html')


def puzzle(req):
    return render(req,'captchaPage/puzzle.html')

def styleSel(req):
    return render(req,'captchaPage/styleSel.html')

def contentSel(req):
    return render(req,'captchaPage/contentSel.html')
