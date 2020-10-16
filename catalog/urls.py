from django.urls import path
from . import views

urlpatterns = [
    # LOGIN PAGE
    path('', views.login, name='login'),
    # LANDING PAGE
    path('landing/', views.landingpage, name='landingpage'),
    # FULL LEADERBOARD
    path('leaderboard/',views.fullleaderboard, name='fullleaderboard'),
    # SCORINGPAGE
    path('scoring/', views.scoringpage, name='scoringpage'),
    # TOUR DETAILS
    path('tourdetails/', views.tourdetails, name='tourdetails'),
    # ROUND 1 DETAILS
    path('round1/', views.rd1holelist.as_view(), name='rd1holelist'),
    path('round1/', views.rd1holelist.as_view(), name='rd1holelist'),
    path('round1/<int:pk>', views.rd1holedetail, name='rd1holedetail'),
    path('round1/leaderboard', views.rd1leaderboard, name='rd1leaderboard'),
    # ROUND 2 DETAILS
    path('round2/', views.rd2holelist.as_view(), name='rd2holelist'),
    path('round2/<int:pk>', views.rd2holedetail, name='rd2holedetail'),
    path('round2/leaderboard', views.rd2leaderboard, name='rd2leaderboard'),
    # ROUND 3 DETAILS
    path('round3/', views.rd3holelist.as_view(), name='rd3holelist'),
    path('round3/<int:pk>', views.rd3holedetail, name='rd3holedetail'),
    path('round3/leaderboard', views.rd3leaderboard, name='rd3leaderboard'),
    # ROUND 4 DETAILS
    path('round4/', views.rd4holelist.as_view(), name='rd4holelist'),
    path('round4/<int:pk>', views.rd4holedetail, name='rd4holedetail'),
    path('round4/leaderboard', views.rd4leaderboard, name='rd4leaderboard'),
    # TEAMS ROUND DETAILS
    path('teamsround', views.teamsround, name='teamsround'),
    path('teamsroundleaderboard', views.teamsroundleaderboard, name='teamsroundleaderboard'),
    # OTHER EVENTS - tips
    path('entertips/', views.entertips, name='entertips'),
    path('tipresults/', views.tipresults, name='tipresults'),
    # OTHER EVENTS - social
    path('entersocial/', views.entersocial, name='entersocial'),
    # TOUR DETAILS - players
    path('tourplayers/', views.tourplayers, name='tourplayers'),
    # TOUR DETAILS - agenda
    path('touragenda/', views.touragenda, name='touragenda'),
    # PLAYER DETAILS
    path('player/<name>', views.playerdetail, name='playerdetail'),
    # MATCH REPORTS
    path('matchreports', views.matchreports, name='matchreports'),
    path('matchreportsfile', views.matchreportsfile, name='matchreportsfile'),
    path('matchreportsinput', views.matchreportsinputs, name='matchreportsinput'),
    path('matchreportsinputconfirm', views.matchreportsinputconfirm, name='matchreportsinputconfirm')

]
