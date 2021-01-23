from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.db.models import Count
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.contrib import messages

from .models import Post, Category, PostStatistic, Tag
from .forms import EmailPostForm
from likes.views import like_dislike


class BlogListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 5
    queryset = Post.published.all()

    def get_queryset(self):
        self.breadcrumb = []
        sort = self.request.GET.getlist("sort")
        if self.kwargs.get("category") is not None:
            category = get_object_or_404(Category, slug=self.kwargs.get("category")).get_descendants(
                include_self=True)
            posts = Post.published.filter(category__in=category)
            self.breadcrumb = category[0].get_ancestors(include_self=True)
        elif self.kwargs.get("tag_slug") is not None:
            posts = Post.published.filter(tags__slug=self.kwargs.get('tag_slug'))
        else:
            posts = Post.published.all()
        if sort:
            posts.order_by(*sort)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumb"] = self.breadcrumb
        context['tag'] = Tag.objects.filter(slug=self.kwargs.get("tag_slug")).first()
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    queryset = Post.objects.filter(status="published")
    def get_queryset(self):
        if self.request.GET:
            like_dislike(self)
        post = self.queryset.filter(slug=self.kwargs.get("slug"),)
        if post:
            obj, created = PostStatistic.objects.get_or_create(
                date=timezone.now(), post=post[0], defaults={"post": post[0], "date": timezone.now()}
            )
            obj.views += 1
            obj.save(update_fields=["views"])
        return post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_tags_ids = context['post'].tags.values_list("id", flat=True)
        similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=context['post'].id)
        context['similar_posts'] = similar_posts.annotate(same_tags=Count("tags")).order_by(
            "-same_tags", "-publish"
        )[:4]
        return context


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ['category', 'title', 'description', 'body', 'keywords', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published = False
        self.success_url = reverse_lazy('blog:post_list')
        form.save()
        messages.success(self.request, 'Стаття успішно додана і відправлена на модерацію.')
        return super(BlogCreateView, self).form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'description', 'body', 'keywords', 'tags']

    def form_valid(self, form):
        messages.success(self.request, 'Стаття успішно оновлена.')
        return super(BlogUpdateView, self).form_valid(form)


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:post_list')


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status="published")
    sent = False
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(
                cd["name"], cd["email"], post.title
            )
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(
                post.title, post_url, cd["name"], cd["comments"]
            )
            send_mail(subject, message, "admin@myblog.com", [cd["to"]])
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request, "blog/post/share.html", {"post": post, "form": form, "sent": sent}
    )


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: /accounts/",
        "Disallow: /badwordfilter/",
        "Disallow: /likes/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")