from django.urls import path
from .views import PagesListView , PagesDetailView , PageCreateView


pages_patterns = ([
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:page_slug>/',  PagesDetailView.as_view() , name='page'),
    path('create/', PageCreateView.as_view(),name='create')
],'pages')