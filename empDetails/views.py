from django.shortcuts import render, get_object_or_404


from django.contrib import messages
from .forms import EmpForm
from .models import EmpDetailsModel




def form_view(request):
    form = EmpForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, " Details Saved ")
        form=EmpForm()
    else:
        messages.error(request, "Incomplete details")
    context = {
        "form": form,
    }
    return render(request, "detailsform.html", context)
    

def search_view(request):
#     instance = get_object_or_404(EmpDetailsModel)
    query = request.GET.get("q")
    queryset_list = EmpDetailsModel.objects.all()

    base_url=request.META['HTTP_HOST']
    
    context={
             "objList":queryset_list, 
             'key':query, 
             'base_url':base_url,
             'T':True,
             'F':False,
             }
    
    return render(request, "searchform.html", context)


def base_view(request):
#     instance = get_object_or_404(EmpDetailsModel)
    obj=EmpDetailsModel.objects.all()
    base_url=request.build_absolute_uri()
    details_link=base_url+"detailsform/"
    searchform_link=base_url+"searchform/"
    context={
             "detailsform_url":details_link,
             'searchform_url':searchform_link
             }
    
    return render(request, "home.html", context)