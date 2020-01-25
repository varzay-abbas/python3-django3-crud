from django.contrib import admin  
from django.urls import path  
from django.conf.urls import url
from employee import views  
urlpatterns = [  
    url('admin/', admin.site.urls),  
    url('emp', views.emp),  
    url('show',views.show),  
    #url('edit/<int:id>', views.edit),  
    path('edit/<int:id>', views.edit),  
    #url('update/<int:id>', views.update),
    path('update/<int:id>', views.update),  
    #url('delete/<int:id>', views.destroy),
    path('delete/<int:id>', views.destroy),
  
]  