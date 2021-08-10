from django.urls import path
from client import views

urlpatterns = [
    path('clients/', views.ClientListView.as_view(), name='clients'),
    path('clients-NA/', views.ClientListNAView.as_view(), name='NA-clients'),
    path('clients/create-new/', views.CreateClientView.as_view(),name='client-create'),
    path('clients/<str:slug>/', views.ClientDetailView.as_view(), name='client-detail'),
    path('clients/<str:slug>/update/', views.UpdateClientView.as_view(), name='client-update'),
    path('clients/<str:slug>/delete/',views.DeleteClientView.as_view(), name='client-delete'),

    path('clients/<str:slug>/asset-<int:pk>/', views.AssetDetailView.as_view(), name='asset-detail'),
    path('clients/<str:slug>/asset-<int:pk>/update',views.UpdateAssetView.as_view(), name='asset-detail-update'),
    path('clients/<str:slug>/asset-<int:pk>/delete',views.DeleteAssetView.as_view(), name='asset-detail-delete'),
    path('clients/<str:slug>/create-new-asset/',views.CreateAssetView.as_view(), name='asset-detail-create'),    

    path('clients/<str:slug>/employee-<int:pk>',views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('clients/<str:slug>/employee-<int:pk>/update',views.UpdateEmployeeView.as_view(), name='employee-detail-update'),
    path('clients/<str:slug>/employee-<int:pk>/delete',views.DeleteEmployeeView.as_view(), name='employee-detail-delete'),
    path('clients/<str:slug>/create-new-employee/',views.CreateEmployeeView.as_view(), name='employee-detail-create'),    

    path('clients/<str:slug>/related-<int:pk>',views.RelatedDetailView.as_view(), name='related-detail'),
    path('clients/<str:slug>/related-<int:pk>/update',views.UpdateRelatedView.as_view(), name='related-detail-update'),
    path('clients/<str:slug>/related-<int:pk>/delete',views.DeleteRelatedView.as_view(), name='related-detail-delete'),
    path('clients/<str:slug>/create-new-related/',views.CreateRelatedView.as_view(), name='related-detail-create'),    
]