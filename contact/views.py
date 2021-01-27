from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Contact


class ContactCreate(SuccessMessageMixin, CreateView):
    model = Contact
    template_name = "contact/contact_new.html"
    fields = ["email", "title", "message", "files"]
    success_message = "Ваше повідомлення успішно надіслане!"

    def get_initial(self):
        initial = super(ContactCreate, self).get_initial()
        if self.request.user.is_authenticated:
            initial["email"] = self.request.user.email
        return initial

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Помилка завантаження файла. Невідповідний розмір або тип.')
        return self.render_to_response(self.get_context_data(form=form))




