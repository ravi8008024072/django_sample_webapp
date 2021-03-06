from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, SignUpForm

# Create your views here.
def home(request):
    title = "WELCOME!"
    if request.user.is_authenticated():
        user = request.user
    form = SignUpForm(request.POST or None)
    context = {
        'title':title,
        'user_logedin': user,
        'form' : form,
    }
    if form.is_valid():
        # form.save()
        #OR
        #print request.POST["email"] #not recommended
        #OR
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "User not Entered"
        instance.full_name = full_name
        #OR
        # if not instance.full_name:
        #     instance.full_name = "User not Entered"
        instance.save()
        context = {
            'title': "Thank you."
        }
    return render(request, "home.html", context)



def contact(request):
    title = "Contact Us"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key in form.cleaned_data:
        #     print key,":", form.cleaned_data[key]
        #OR
        form_email = form.cleaned_data.get("email")
        form_full_name  = form.cleaned_data.get("full_name")
        form_message = form.cleaned_data.get("message")
        # print form_full_name, form_email, form_message
        subject = "Site Contact Form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, "otheremail@email.com"]
        contact_message = "%s: %s via %s" %(
                form_full_name,
                form_message,
                form_email)
        send_mail(subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=False)

    context = {
        "form": form,
        "title": title,
    }
    return render(request, "forms.html", context)
