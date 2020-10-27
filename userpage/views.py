from django.shortcuts import render
from .forms import Trymsg
from . import publish
# Create your views here.
def index(request):
    msg_form = Trymsg() 
    isianform = {}
    context = {
        'msg_form' : msg_form,
    }
    print("views .py: ")
    isianform['msg'] = request.POST['msg']
    # publish.sentviabroker(isianform)
    print("format : ")
    print(isianform)

    # if request.method == 'POST':
    #     print("masuk method post")
    #     print(request.POST['nama'])
    #     print(request.POST['alamat'])
    #     context['nama'] = request.POST['nama']
    #     context['alamat'] = request.POST['alamat']
    #     print("context: ", context)
    # else:
    #     print("ini method get")
    return render(request, 'input.html', context )