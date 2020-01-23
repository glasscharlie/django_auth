from veggies.views import VeggieList, VeggieDetail
from django.urls import path


urlpatterns=[
    path('', VeggieList.as_view(), name='post_list'),
    path('<int:pk>/', VeggieDetail.as_view(), name='post_detail')
]