from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [      
    path('details_products/', views.details_products, name='details_products'),
    path('product_list/', views.product_list, name='product_list'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)