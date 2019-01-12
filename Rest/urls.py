"""Rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.decorators import login_required

from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from men.views import TableCreateView,TableListView,load_Tables,RegisterOrder,product,start,donek,print,\
    item,invoice,delete,ensure,control,kitchen,order_control,done,productRegistration,Rest,Rest_infor,home,ItemState,cash


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', TableCreateView.as_view(template_name="about.html"), name='person_changelist'),
    #path('', '),
    path('dd/', load_Tables),
    path('new/<ln>', RegisterOrder),
    path('list/<Order_id>/', product,name='List'),
    #url(r'^list/(?P<Order_id>[0-9]+)/$', product)
    path('item/list/<Order_id>/<Product_id>', item),
    path('invoice/<Order_id>', invoice,name='invoice'),
    path('invoice/<product_id>/<Order_id>', delete,name='delete_Item'),
    path('invoice1/<Order_id>',ensure,name='ensure'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('control/', login_required(control),name='control'),
    path('kitchen/', kitchen,name='kitchen'),
    path('done/<order_id>', done,name='done'),
    path('print/<order_id>', print, name='print'),

    path('order_control/', order_control,name='order_control'),
    path('Add_product/', productRegistration,name='productRegistration'),
    path('Rest_inform/', Rest_infor, name='Rest_inform'),
    path('start/<ln>', start,name='start'),
    path('done_k/<id>', donek,name='donek'),
    path('ItemState/<name>', ItemState, name='ItemState'),
    path('cash/',cash, name='cash'),

    path('', home,name='home'),
                  #path('rest_inform/', rest_inform, name='rest_inform'),

 ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
