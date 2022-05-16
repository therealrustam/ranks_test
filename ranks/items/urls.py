from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('buy/<int:buy_id>/', views.buy_item),
    path('item/<int:item_id>/', views.get_item),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),
]
