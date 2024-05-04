from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
#Solo los nombres de las clases se escriben incialmente con mayusculas
    template_name = "home.html"