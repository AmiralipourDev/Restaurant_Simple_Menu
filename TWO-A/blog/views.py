from django.shortcuts import render
from .models import ContactForm, Food, Chef


# Create your views here.
def foods_list(request):
    food_list = Food.objects.all()
    context = {"food_list": food_list}

    return render(request, 'blog/index.html', context=context)


def chefs_list(request):
    chef_list = Chef.objects.all()
    context = {"chef_list": chef_list}

    return render(request, 'blog/about.html', context=context)


def contact_form(request):
    if request.method == "POST":
        form_name = request.POST.get("form_name", "")
        form_email = request.POST.get("form_email", "")
        form_message = request.POST.get("form_message", "")

        newform = ContactForm(form_name=form_name, form_email=form_email, form_message=form_message)
        newform.save()

    return render(request, 'blog/contact.html')
