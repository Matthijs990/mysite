from django.urls import path
try:
    from . import views
except Exception as ex:
    raise ex
    import views
urlpatterns = [
    path('', views.index, name='index'),
    path('feedback/<str:vote>/', views.feedback, name='feedback'),
    path('get', views.Get, name='get'),
    path('search', views.search, name='search'),
    path('tricks', views.tricks, name='tricks'),
]
