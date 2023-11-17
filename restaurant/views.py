from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, DestroyAPIView
from .serializers import MenuSerializer
from .models import Menu

# Create your views here.
def index(request):
    return HttpResponse("test")


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveDestroyAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
