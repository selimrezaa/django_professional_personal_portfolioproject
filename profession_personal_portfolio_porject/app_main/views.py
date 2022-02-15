from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from .forms import *
# Create your views here.


def index(request):
    #home qurery
    current_user = request.user
    profile_obj = Profile.objects.filter(user=current_user)
    home_obj = Home.objects.filter(user=current_user)
    service_obj = Service.objects.filter(user=current_user)
    service_obj2 = Service.objects.filter(user=current_user)
    skill_obj = Skills.objects.filter(user=current_user)
    portfolio_obj = Portfolio.objects.filter(user=current_user)
    count_down_obj = CountDown.objects.filter(user=current_user)
    testimonial_obj = Testimonial.objects.filter(user=current_user)
    partner_obj = Partners.objects.filter(user=current_user)
    lets_connect_obj = Lets_Connect.objects.filter(user=current_user)
    footer_obj = Footer.objects.filter(user=current_user)


    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('okay')
        else:
            return HttpResponse('the filed input value is not valid')
    else:
        form = ContactForm()

    context = {
        'profile_obj': profile_obj,
        'home_obj': home_obj,
        'service_obj': service_obj,
        'service_obj2': service_obj2,
        'skill_obj': skill_obj,
        'portfolio_obj': portfolio_obj,
        'count_down_obj': count_down_obj,
        'testimonial_obj': testimonial_obj,
        'partner_obj': partner_obj,
        'lets_connect_obj': lets_connect_obj,
        'footer_obj': footer_obj,
        #contact form
        'form': form,
    }

    return render(request, 'base.html', context)



#service details
def service_details(request, pk):
    service_det = Service.objects.get(pk=pk)
    print('===============================================================', service_det)
    context = {'service_det': service_det, }
    return render(request, 'app_main/modal.html', context)
