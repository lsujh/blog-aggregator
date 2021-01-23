from django.views.generic.edit import CreateView
from django.contrib import messages

from .models import Contact

class ContactCreate(CreateView):
    model = Contact
    template_name = 'contact/contact_new.html'
    fields = ['email', 'title', 'message', 'files']


    def get_initial(self):
        initial = super(ContactCreate, self).get_initial()
        if self.request.user.is_authenticated:
            initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Ваше повідомлення успішно надіслане!')
        return super().form_valid(form)
