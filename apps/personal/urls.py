from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
      path("",login_fun,name='home'),
       
      path("accounts/login/",login_fun,name='login'),
      path("index/",index_fun,name='index'),
      path("logout/",logout_fun,name='logout'),
      path("kode6zn/",kode6zn_fun,name='kode6zn'),
      path("forgotPassword/",forgotPassword_fun,name='forgotPassword'),
      path("registration/",registration_fun,name='registration'),
      path("adminpage/",adminpage_fun,name='adminpage'),
      path("userpage/",userpage_fun,name='userpage'),
      path("employees/",addemployees_fun,name='employees'),
      path("uchetvremeni/",uchetvremeni_fun,name='uchetvremeni'),
      path("udalennyesotrudniki/",udalennyesotrudniki_fun,name='udalennyesotrudniki'),
      path("check_add/",check_add_fun,name='check_add'),
      
]

urlpatterns += static(settings.STATIC_URL,
                              document_root=settings.STATIC_URL)
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)