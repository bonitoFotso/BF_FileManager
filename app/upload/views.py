from django.shortcuts import render
from django.views import View
from .models import Fichier
from django.views.generic import ListView
from django.http import HttpResponse

class ImageUploadView(View):
    template_name = 'upload.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.method == "POST" and request.FILES["image_file"]:
            image_file = request.FILES["image_file"]
            fichier = Fichier()
            fichier.nom = image_file.name
            fichier.fichier = image_file
            fichier.save()
            return render(request, self.template_name, {
                "image_url": fichier.fichier.url
            })
        return render(request, self.template_name)

class FichierListView(ListView):
    model = Fichier
    template_name = 'fichier.html'
    context_object_name = 'fichiers'


def telecharger_fichier(request, fichier_id):
    fichier = Fichier.objects.get(id=fichier_id)
    response = HttpResponse(fichier.fichier, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{fichier.nom}"'
    return response

