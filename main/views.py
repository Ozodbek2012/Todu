from django.shortcuts import render
from .models import Student, Reja

def studentlar_view(request):
    students = Student.objects.all()
    return render(request, 'studentlar.html', {'students': students})

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def Reja_view(request):
    plans = Reja.objects.all()
    return render(request, 'Rejalar.html', {'plans': plans})

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def bajarilmagan_rejalar(request):
    plans = Reja.objects.filter(bajarildi=False)
    return render(request, 'bajarilmagan_rejalar.html', {'plans': plans})

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def bitiruvchilar(request):
    students = Student.objects.filter(kurs__gte=3)
    return render(request, 'bitiruvchilar.html', {'students': students})

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from django.shortcuts import redirect, get_object_or_404

def reja_ochir(request, reja_id):
    reja = get_object_or_404(Reja, id=reja_id)
    reja.delete()
    return redirect('rejalar')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def yangi_reja(request):
    form = Reja(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('rejalar')
    return render(request, 'yangi_reja.html', {'form': form})

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def kattalar(request):
    students = Student.objects.filter(yosh__gt=20)
    return render(request, 'kattalar.html', {'students': students})

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def bitiruvchi_rejalar(request):
    rejalari = Reja.objects.filter(student__kurs__gte=3)
    return render(request, 'bitiruvchi_rejalar.html', {'rejalari': rejalari})

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def talaba_rejalari(request, talaba_id):
    rejalari = Reja.objects.filter(student__id=talaba_id)
    return render(request, 'talaba_rejalari.html', {'rejalari': rejalari})

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

