from xml.dom.minidom import Document
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('nosotros', views.nosotros,name='nosotros'),
    path('libros', views.showlibros,name='libros'),
    path('libros/nuevo', views.newBook,name='newBook'),
    path('libros/edita', views.updateBook,name='updateBook'),
    path('eliminar/<int:id>', views.deleteBook,name='deleteBook'),
    path('libros/edita/<int:id>', views.updateBook,name='updateBook'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)