from django.shortcuts import render,  get_object_or_404, redirect
from .models import Profile, Service
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm

def profileapp(request):
  profile = Profile.objects.get(user=request.user)
  services = Service.objects.all()
  context = {
        "profile":profile,
        "services":services
    }
  return render (request, 'profile.html', context) 



def add_new_service(request):
  if request.method == "POST":
    form = ServiceForm(request.POST)
    if form.is_valid:
      form.save()
      return redirect('profileapp:profileapp')
  else:
    form = ServiceForm()

  context = {
        "form": form,
        "page_title": "Add new Service"
  }
  return render(request, 'add_new_service.html', context)
