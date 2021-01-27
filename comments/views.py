from django.contrib.contenttypes.models import ContentType
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from badwordfilter.views import PymorphyProc, RegexpProc
from .forms import CommentForm
from .models import Comment
from blog.models import Post


class CommentCreate(SuccessMessageMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "comments/comments-create.html"
    success_message = "Коментар успішно додано."

    def get_initial(self):
        initial = super(CommentCreate, self).get_initial()
        initial["parent"] = self.request.GET.get("parent")
        if self.request.user.is_authenticated:
            initial["author"] = self.request.user.full_name()
            initial["email"] = self.request.user.email
        return initial

    def form_valid(self, form):
        cd = form.cleaned_data
        form.instance.author = cd.get("author")
        form.instance.email = cd.get("email")
        try:
            form.instance.parent = Comment.objects.get(id=cd.get("parent"))
        except:
            form.instance.parent = None
        post = Post.published.get(slug=self.kwargs.get("slug"))
        form.instance.content_type = ContentType.objects.get_for_model(post)
        form.instance.object_id = post.id
        form.instance.post_slug = self.kwargs.get("slug")
        content = PymorphyProc.replace(cd.get("content"), repl="***")
        content = RegexpProc.replace(content, repl="***")
        form.instance.content = content
        self.success_url = post.get_absolute_url()
        form.save()
        return super(CommentCreate, self).form_valid(form)
