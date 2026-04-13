"""Shopmate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from Shpmate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_add),
    path('login_post',views.login_post),
    path('logout',views.logout),
    #admin module
    path('adminhome',views.adminhome),
    path('Changepswadmin',views.Changepswadmin),
    path('Changepsw_post',views.Changepsw_post),
    path('Viewshop',views.Viewshop),
    path('approveshop/<id>',views.approveshop),
    path('rejectshop/<id>',views.rejectshop),
    path('viewuser',views.viewuser),
    path('verifiedshop',views.verifiedshop),
    path('viewcomplaints',views.viewcomplaints),
    path('viewfeedback',views.viewfeedback),
    path('Addcategorey',views.Addcategorey),
    path('addcategorey_post',views.addcategorey_post),
    path('viewcategorey',views.viewcategorey),
    path('editcate/<id>',views.editcate),
    path('editcat_p/<id>',views.editcat_p),
    path('delcate/<id>',views.delcate),
    path('sndreplay/<id>',views.sndreplay),
    path('sndreplay_p/<id>',views.sndreplay_p),
    #Shop Module
    path('ShopHome',views.ShopHome),
    path('Changepswshop',views.Changepswshop),
    path('Changepsw_posts',views.Changepsw_posts),
    path('RegisterShop',views.RegisterShop),
    path('Regshop_post',views.Regshop_post),
    path('editshop/<id>',views.editshop),
    path('editshop_post/<id>',views.editshop_post),
    path('Viewprofileshop',views.Viewprofileshop),
    path('viewcatefories',views.viewcatefories),
    path('addpro',views.addpro),
    path('addpro_post',views.addpro_post),
    path('Viewproduct',views.Viewproduct),
    path('editpro/<id>',views.editpro),
    path('editpro_post/<id>',views.editpro_post),
    path('deletepro/<id>',views.deletepro),
    path('viewreviews',views.viewreviews),
    path('viewOrder',views.viewOrder),
    path('viewsuborder/<id>',views.viewsuborder),
    path('updatestatus/<id>',views.updatestatus),
    path('update_post/<id>',views.update_post),
    path('forgetpassword',views.forgetpassword),
    path('forgotpassword_post',views.forgotpassword_post),
    #User Module Android(usermangement)
    path('UserHome',views.UserHome),
    path('login_addu',views.login_addu),
    path('Changepswu',views.Changepswu),
    path('forgotpasswdu',views.forgotpasswdu),
    path('registeruser',views.registeruser),
    path('viewuprofile',views.viewuprofile),
    path('Editprou',views.Editprou),
    path('Editu_post',views.Editu_post),
    path('viewcategoriesu',views.viewcategoriesu),
    path('viewprou',views.viewprou),
    path('addcart',views.addcart),
    path('viewcart',views.viewcart),
    path('delete_cart',views.delete_cart),
    path('placeorder',views.placeorder),
    path('vieworderstatus',views.vieworderstatus),
    path('sndreview',views.sndreview),
    path('SndComplaints',views.SndComplaints),
    path('viewReplay',views.viewReplay),
    path('sndfdback',views.sndfdback),
    path('vieworderpro',views.vieworderpro),
    path('offline_payment',views.offline_payment),
    path('online_payment',views.online_payment),
]