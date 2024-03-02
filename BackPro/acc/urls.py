from django.urls import path
from . import views

urlpatterns = [
    path('', views.acc_home, name="acc_home"),
    path('create', views.create, name="create"),
    path('<int:pk>', views.AccDetail.as_view(), name='acc-detail'),
    path('<int:pk>/update', views.AccUpdateView.as_view(), name='acc-update'),
    path('<int:pk>/delete', views.AccDeleteView.as_view(), name='acc-delete')
]
