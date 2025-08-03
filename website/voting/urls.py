from django.urls import path
from .views import *

urlpatterns = [
    path('', landing, name='landing-page'),
    path('logout/', log_out, name='logout'),
    path('profile/', profile, name='profile'),
    path('vote/', DoVote, name='vote'),
    path('error/', error, name='error'),
    path('view_votes/', view_votes, name='view_votes'),
    path('sign-up/', sign_up, name='sign-up'),
]
