from django.urls import path
from .views import HomePageView

urlpatterns = [
    path ("",HomePageView.as_view(), name="home")
]
#Los corchetes son usados para hacer listas
#La segunda coma es el visualizador de la pagina (lo que se va a mostrar)
#La tercera coma es el pseudomino de la segunda coma (Nombrarlo de otra manera para q cuando lo llamemos seria con "home")