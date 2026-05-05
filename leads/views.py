from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Lead
from .forms import LeadForm

def home(request):
    return render(request, 'home.html')

def section1(request):
    return render(request, 'section1.html')

def section2(request):
    return render(request, 'section2.html')

def section3(request):
    return render(request, 'section3.html')

def section4(request):
    return render(request, 'section4.html')

def section5(request):
    return render(request, 'section5.html')

def add_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ تم حفظ البيانات بنجاح!')
            return redirect('view_leads')
    else:
        form = LeadForm()
    return render(request, 'add_lead.html', {'form': form})

def view_leads(request):
    leads = Lead.objects.all().order_by('-timestamp')
    return render(request, 'view_leads.html', {'leads': leads})
