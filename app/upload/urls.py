
from django.urls import path

from upload.views import ImageUploadView, FichierListView, telecharger_fichier

urlpatterns = [
    path("", ImageUploadView.as_view(), name="upload"),
    path('fichiers/', FichierListView.as_view(), name='fichier_list'),
    path('fichier/<int:fichier_id>/telecharger/', telecharger_fichier, name='telecharger_fichier'),
    
]

