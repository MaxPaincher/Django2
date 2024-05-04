from django.views.generic import TemplateView

# Create your views here.
class HomePageView (TemplateView):
#Solo los nombres de las clases se escriben incialmente con mayusculas y al final los dos puntos :
    template_name = "home.html"

class AboutPageView (TemplateView):
    template_name = "about.html"