from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('lv1/<int:q_id>', views.querylv1),
	path('lv2/<int:q_id>', views.querylv2),
	path('lv3/<int:q_id>', views.querylv3),
	path('initialize', views.make_data, name="make_data"),
]
