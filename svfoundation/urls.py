from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from news import views as news_views
from help import views as help_views
from payments import views as payment_views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('health/', news_views.health),
    path('news/', news_views.NewsViewSet.as_view({'get': 'list'})),
    path('news/<str:slug>', news_views.NewsViewSet.as_view({'get': 'retrieve'})),
    path('tags/', news_views.NewsTagsList.as_view({'get': 'list'})),
    path('help_requests/', help_views.HelpRequestView.as_view()),
    path('fund_documents/', payment_views.FundDocumentsSet.as_view({'get': 'list'})),
    path('payment_details/', payment_views.PaymentDetailsSet.as_view({'get': 'list'})),
    path('payment_details/<str:pk>', payment_views.PaymentDetailsSet.as_view({'get': 'retrieve'})),
    path('make_payment/', payment_views.MakePayment.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
