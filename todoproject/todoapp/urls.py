from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    # path('details',views.details,name='details'),

    path('chome/',views.Listview.as_view(),name='chome'),
    path('cdetail/<int:pk>/',views.Detailview.as_view(),name='cdetail'),
    path('cupdate/<int:pk>/', views.Updateview.as_view(), name='cupdate'),
    path('cdelete/<int:pk>/', views.Deleteview.as_view(), name='cdelete'),
]