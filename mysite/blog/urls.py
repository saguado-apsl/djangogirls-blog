from django.utls import path
from .views import views

urlpatterns = [
    path('post_list', views.post_list ),
]