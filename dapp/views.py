from django.shortcuts import render,get_object_or_404
from.models import department,docters,appoinment,Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Create your views here.
def doc(request):
    obj=department.objects.all()
    return render(request,'index.html',{'dep':obj})

def doclist(request):
    obj=docters.objects.all()
    return render(request,'docters.html',{'doc':obj})
def CategoryView(request, cats=None):
    category_post = docters.objects.filter(category=cats)
    return(request,'categories.hml',{'cats':cats,'category_post':category_post})
def allProdCat(request,c_slug=None):
    c_page=get_object_or_404(department,slug=c_slug)
    products_list=docters.objects.filter(category=c_page)

    return render(request,'categories.html',{'category':c_page,'product':products_list})
def ProCatDetail(request,c_slug,product_slug):
    try:
        product = docters.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
            raise e
    return render(request,'product.html',{'product':product})


# def demo(request):
#     product1 = appoinment.objects.all()
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         department = request.POST.get('department')
#         date= request.POST.get('date')
#         email= request.Post.get('email')
#         phone = request.Post.get('phone')
#         obj = appoinment(name=name,department=department,phone=phone,date=date,email =email)
#         obj.save()
#         return render(request, "appoinment.html", {'product': product1})
#     return render(request, "appoinment.html")
def demo(request):
    product1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date= request.POST.get('date')
        obj = Task(name=name, priority=priority,date=date)
        obj.save()
        return render(request, "home.html", {'product': product1})
    return render(request, 'home.html')