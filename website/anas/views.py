from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from anas.forms import NameForm
from django.core.mail import send_mail

# Create your views here.
def index(request):

    template = loader.get_template('anas/nav.html')
    return HttpResponse(template.render())

def get_name(request):

    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ["shaikhanas600@gmail.com"]
            if cc_myself:
                recipients.append(sender)
            send_mail(subject, message, sender, recipients)

            return HttpResponseRedirect("thanks")
    else:
        form = NameForm()
        return render(request, "anas/index.html", {"form": form})
