from django.shortcuts import render,redirect
from firstapp.models import details_bio
from django.contrib import messages
from django.db.models import Q

def home(request):
    if request.method =='POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        c_type = request.POST.get('c_type')
        symptoms = request.POST.get('symptoms')

        store = details_bio(bname = name, bcat = category, btype = c_type, bsymt = symptoms)
        store.save()
        messages.success(request, f'{store.bname} added successfully!')
        return redirect('home')
    return render(request, 'home.html') 

def data(request):
    if request.method =='GET':
        obj = details_bio.objects.all()
        return render(request, 'getdata.html',{'obj':obj})

def search(request):
    if(request):
        if request.method == 'POST':
            srch = request.POST['srh']

            if srch:
                match = details_bio.objects.filter(Q(bname__icontains=srch) | Q(bcat__icontains=srch) | Q(btype__icontains=srch))

                if match:
                    return render(request,'search.html',{'sr':match})
                else:
                    messages.error(request, 'No Result found')
                    return redirect('home')
                    
            else:
                return redirect('home')
                return render (request, 'home.html')



