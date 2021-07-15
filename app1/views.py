from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import City
from .forms import CityForm
from .serializers import CitySearchSerializer
from rest_framework import generics
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class CityListCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView, ):
    login_url = 'u-login'
    permission_required = 'app1.add_city'

    def get(self, request, *args, **kwargs):
        context = {'form': CityForm()}
        return render(request, 'city_list.html', context)

    def post(self, request, *args, **kwargs):
        form = CityForm(request.POST)
        if form.is_valid():
            customer = form.save()
            customer.save()
            return HttpResponseRedirect(reverse_lazy('u-citylist', ))
        return render(request, 'city_list.html', {'form': form})


class CityListView(PermissionRequiredMixin, LoginRequiredMixin, ListView, ):
    login_url = 'u-login'
    model = City
    permission_required = 'app1.view_city'
    ordering = ['city']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['form'] = CityForm()
        return context


class CitySearchView(generics.ListAPIView):
    search_fields = ['city', ]
    filter_backends = (filters.SearchFilter, )
    queryset = City.objects.all()
    serializer_class = CitySearchSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySearchSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
