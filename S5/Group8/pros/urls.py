from django.conf.urls import url

from . import views


app_name = 'pros'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cadastro_ordem/$', views.cadastro_ordem, name='cadastro_ordem'),
    url(r'^update_ordem/(?P<pk>[0-9]+)/$', views.update_ordem, name='update_ordem'),
    url(r'^delete_ordem/(?P<pk>[0-9]+)/$', views.delete_ordem, name='delete_ordem'),
    url(r'^imprimir_ordem/(?P<pk>[0-9]+)/$', views.imprimir_ordem, name='imprimir_ordem'),
    url(r'^empresas/$', views.empresas, name='empresas'),
    url(r'^empresas/delete_empresa/(\d+)/$', views.delete_empresa, name='delete_empresa'),
    url(r'^empresas/(?P<empresa_id>[0-9]+)/$', views.clientes, name='clientes'),
    url(r'^empresas/cadastro_empresa/$', views.cadastro_empresa, name='cadastro_empresa'),
    url(r'^empresas/update_empresa/(\d+)/$', views.update_empresa, name='update_empresa'),
    url(r'^empresas/(?P<empresa_id>[0-9]+)/cadastro_cliente/$', views.cadastro_cliente, name='cadastro_cliente'),
    url(r'^empresas/(?P<empresa_id>[0-9]+)/update_cliente/(?P<pk>[0-9]+)/$', views.update_cliente, name='update_cliente'),
    url(r'^empresas/(?P<empresa_id>[0-9]+)/delete_cliente/(?P<pk>[0-9]+)/$', views.delete_cliente, name='delete_cliente'),
]

