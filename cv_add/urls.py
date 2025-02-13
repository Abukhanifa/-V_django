from django.urls import path
from .views import contact_view, success_view, create_cv, cv_list_view, share_cv_email  # Import the success view
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success_page'),
    path('cv_create/', create_cv, name='cv_create'),
    path('cv_list/', cv_list_view, name='cv_list'),
    path('share/email/<int:cv_id>/', share_cv_email, name='share_cv_email'), 
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
