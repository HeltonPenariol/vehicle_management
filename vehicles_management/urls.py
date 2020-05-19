from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .api.viewsets import OwnerViewSet, \
    OwnerCreateViewSet, \
    OwnerDocViewSet, \
    OwnerMatViewSet, \
    VehicleBrandViewSet, \
    VehicleModelViewSet, \
    VehicleTypeViewSet, \
    VehicleListViewSet, \
    VehiclePlateListViewSet, \
    VehicleChassisListViewSet, \
    VehicleDocListViewSet, \
    VehicleCreateViewSet

urlpatterns = [
    # Autenticação
    url(r'^auth/', obtain_jwt_token),

    # Gestão de proprietarios
    url(r'^proprietario/', OwnerViewSet.as_view({'get': 'list'})),
    url(r'^criar/proprietario/', OwnerCreateViewSet.as_view({'post': 'create'})),
    url(r'^doc/proprietario/(?P<doc>\w+)$', OwnerDocViewSet.as_view({'get': 'list'})),
    url(r'^mat/proprietario/(?P<mat>\w+)$', OwnerMatViewSet.as_view({'get': 'list'})),

    # Lista modelos cadastrados
    url(r'^modelos/', VehicleModelViewSet.as_view({'get': 'list'})),
    # Lista marcas cadastradas
    url(r'^marcas/', VehicleBrandViewSet.as_view({'get': 'list'})),
    # Lista tipos de veículos cadastrados
    url(r'^tipos/', VehicleTypeViewSet.as_view({'get': 'list'})),

    # Gestão de veículos
    url(r'^veiculos/', VehicleListViewSet.as_view({'get': 'list'})),
    url(r'^placa/veiculos/(?P<placa>\w+)$', VehiclePlateListViewSet.as_view({'get': 'list'})),
    url(r'^chass/veiculos/(?P<chass>\w+)$', VehicleChassisListViewSet.as_view({'get': 'list'})),
    url(r'^doc/veiculos/(?P<doc>\w+)$', VehicleDocListViewSet.as_view({'get': 'list'})),
    url(r'^criar/veiculos/', VehicleCreateViewSet.as_view({'post': 'create'}))
]
