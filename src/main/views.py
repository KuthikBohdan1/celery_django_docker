from django.views.generic import CreateView
import time
from .models import Contact
from .forms import ContactForm
from .tasks import send_spam_email
from .service import send

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'main/contact.html'

    def form_valid(self, form):
        form.save()
        print(f"email_instsnse {form.instance.email}")
        send_spam_email.delay(user_email = form.instance.email, text = form.instance.name)
        return super().form_valid(form)
