from django.shortcuts import render
from myapp import form
from myapp import code
# Create your views here.
def index(request):
    return render(request,"index.html")

def form_(request):
    name=' '
    nam=' '
    bprice=' '
    mprice=' '
    img=' '
    bprice1=' '
    mprice1=' '
    img1=' '
    fo= form.formClass
    if request.method=="POST":
        fo=form.formClass(request.POST)
        if fo.is_valid():
        
            tex=fo.cleaned_data['search']    
            urf,ura=code.inpu(tex),code.inpu1(tex)
            nurf=code.scrap(urf)
            nura=code.scrap1(ura)
            img,nsp=code.image(nurf)
            img1=code.image1(nura)
            name,nam=code.title(nurf,nsp),code.title1(nura)
            bprice,bprice1=code.price(nurf,nsp),code.price3(nura)
            mprice,mprice1=code.price2(nurf,nsp),code.price4(nura)
            
    context={"key":fo,"x":name,"y":bprice,"z":mprice,"a":img ,"x1":nam,"y1":bprice1,"z1":mprice1,"a1":img1}
    return render(request,"main.html",context)   
