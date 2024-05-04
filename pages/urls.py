from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path ("",HomePageView.as_view(), name="home")
    path ("about/",AboutPageView.as_view(), name="about")
]
#Los corchetes son usados para hacer listas
#La segunda coma es el visualizador de la pagina (lo que se va a mostrar)
#La tercera coma es el pseudomino de la segunda coma (Nombrarlo de otra manera para q cuando lo llamemos seria con "home")