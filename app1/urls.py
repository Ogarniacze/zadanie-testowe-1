from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from . import views
from .views import CityViewSet, CitySearchView, CityListView, CityListCreateView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('city', CityViewSet, basename='city')

urlpatterns = [
    url(r'^$', CityListView.as_view(template_name="city_list.html"),
        name='u-citylist'),
    path(r'add/', CityListCreateView.as_view(template_name="city_list.html"),
         name='u-citylist-create'),
    path('szukaj/', CitySearchView.as_view(), name="u-citysearch"),
    # LOGIN/LOGOUT/PASSWORD
    url(r'^login/$', auth_views.LoginView.as_view(
        redirect_authenticated_user=True, template_name='login.html', ), name='u-login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/'), name='u-logout'),
    ]
