from django.urls import path
from . import views

urlpatterns = [
    path('',views.styleSel),
    path('puzzle',views.puzzle),
    path('styleSel',views.styleSel),
    path('contentSel',views.contentSel)
]
