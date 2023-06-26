# coding=utf-8
from django.urls import re_path as url
from . import views


#加载静态资源的服务 serve 处理媒体文件的函数
from django.views.static import serve



urlpatterns = [

    url(r'^success/$', views.success),
    url(r'^index/$', views.index),
    url(r'^passenger_index/$', views.passenger_index),
    url(r'^administrator_index/$', views.administrator_index),

    url(r'^administrator_information/$', views.administrator_information),
    url(r'^administrator_add/$', views.administrator_add),
    url(r'^administrator_edit/$', views.administrator_edit),
    url(r'^administrator_delete/$', views.administrator_delete),
    url(r'^administrator_search/$', views.administrator_search),

    url(r'^ticket_information/$', views.ticket_information),
    url(r'^ticket_search/$', views.ticket_search),
    url(r'^ticket_add/$', views.ticket_add),
    url(r'^ticket_edit/$', views.ticket_edit),
    url(r'^ticket_delete/$', views.ticket_delete),

    url(r'^ticket_information2/$', views.ticket_information2),
    url(r'^ticket_search2/$', views.ticket_search2),
    url(r'^ticket_buy/$', views.ticket_buy),
    url(r'^ticket_back/$', views.ticket_back),
    url(r'^ticket_deleted/$', views.ticket_deleted),

    url(r'^ticket_list/$', views.ticket_list),
    url(r'^ticket_list_search/$', views.ticket_list_search),


    url(r'^passenger_information/$', views.passenger_information),
    url(r'^passenger_add/$', views.passenger_add),
    url(r'^passenger_edit/$', views.passenger_edit),
    url(r'^passenger_delete/$', views.passenger_delete),
    url(r'^passenger_search/$', views.passenger_search),


]
