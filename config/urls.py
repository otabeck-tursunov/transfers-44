from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('clubs/', views.clubs_view, name='clubs'),
    path('clubs/<int:pk>/', views.club_details_view, name='club-details'),
    path('latest-transfers/', views.latest_transfers_view, name='latest-transfers'),
    path('players/', views.players_view, name='players'),
    path('tryouts/', views.tryouts_view, name='tryouts'),
    path('u-20-players/', views.u20_players_view, name='u-20'),
    path('statistics/', views.StatisticsView.as_view(), name='stats'),
    path('statistics/150-accurate-predictions/', views.Top150AccuratePredictionsView.as_view(), name='150-accurate-predictions'),
    path('statistics/top-50-clubs-by-expenditure/', views.Top50ClubsByExpenditureView.as_view(), name='top-50-clubs-by-expenditure'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
