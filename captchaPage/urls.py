from django.urls import path
from . import views

urlpatterns = [
    path('',views.styleSel),
    path('puzzle',views.puzzle),
    path('styleSel',views.styleSel),
    path('contentSel',views.contentSel),
    path('styleSel4',views.styleSel4),
    path('contentSel4',views.contentSel4),
    path('stylecontentSel',views.stylecontentSel),
]
