from django.urls import path
from website import views

urlpatterns=[
	path('',views.add_show,name='add_show'),
	path('delete/<int:id>/',views.delete_data,name='delete_data'),
	path('<int:id>/',views.update_data,name='update_data'),
	
]