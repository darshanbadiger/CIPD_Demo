from django.shortcuts import render,redirect
from firstapp.models import details_bio
from firstapp.models import upload_data
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



def upload(request):
        if request.method == 'POST':
            p_name = request.POST.get('p_name')
            spe = request.POST.get('spe')
            f_tags = request.POST.get('f_tags')
            geo_file = request.FILES['geo_file']
            mesh_file = request.FILES['mesh_file']
            up_data = upload_data(part_name=p_name, species=spe, function_tag=f_tags, geometry=geo_file, mesh=mesh_file)
            up_data.save()
            messages.success(request, f'{up_data.part_name} added successfully!')
        return render(request, 'upload.html')



def data(request):
    if request.method =='GET':
        obj = details_bio.objects.all()
        return render(request, 'getdata.html',{'obj':obj})

def search(request):
    if(request):
        if request.method == 'POST':
            srch = request.POST['srh']

            if srch:
                match = upload_data.objects.filter(Q(part_name__icontains=srch) | Q(species__icontains=srch))

                if match:
                    return render(request,'search.html',{'sr':match})
                else:
                    messages.error(request, 'No Result found')
                    return redirect('home')
                    
            else:
                return redirect('home')
                return render (request, 'home.html')

