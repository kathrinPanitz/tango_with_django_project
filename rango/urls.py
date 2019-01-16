

# This code imports the relevant Django machinery for URL mappings
# and the views module from rango.
# This allows us to call the function url and point to the index view
# for mapping in urlpatterns.

from django.conf.urls import url
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
