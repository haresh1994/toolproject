
from django.urls import path
from . import views
app_name='toolapp'
urlpatterns = [
   path('',views.index,name='index'),
   path('tool/<int:tools_id>/',views.detail,name='detail'),
   path('add/',views.add_tool,name='add_tool'),
   path('update/<int:id>/',views.update,name='update'),
   path('delete/<int:id>/', views.delete, name='delete'),
]