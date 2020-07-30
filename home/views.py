from django.shortcuts import render

from .models import Banner
from modules.file_selector import file_select as fs
# Create your views here.


def home_view(request):
    banner = Banner.objects.latest('id')
    styles = fs.get_files("css/home")
    js = fs.get_files("js/home")
    context = {'banner': banner, 'styles': styles, 'javascripts': js}
    return render(request, 'pages/home.html', context)
