

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
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',
        views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
]
