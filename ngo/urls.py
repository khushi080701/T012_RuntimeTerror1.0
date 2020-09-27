
from django.urls import path
from . import views
from django.views.generic.base import TemplateView
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('login.html/', views.login, name='login'),
    path('login.html/signUp.html', views.signUp, name='signUp'),
    path('login.html/login.html', views.login, name='login'),
    path('login.html/codeit.html', views.home, name='home'),
    path('login.html/addProduct.html',views.addProduct,name="addproduct"),
    path('req/', views.req, name='req'),
    #path('login.html/index.html', views.index, name='browse'),
    path('login.html/requirements.html/', views.requirements, name='requirements'),
    path('req/addProduct.html',views.addProduct,name='addproduct')
]
