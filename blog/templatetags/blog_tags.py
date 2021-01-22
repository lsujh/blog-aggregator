import markdown

from django import template
from django.utils import timezone
from django.db.models import Count, Sum
from django.utils.safestring import mark_safe

from ..models import Post, PostStatistic, Category
from comments.models import Comment


register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag("blog/category_posts.html")
def show_category_posts():
    categories = Category.objects.all()
    return {"categories": categories}


@register.inclusion_tag("blog/latest_posts.html")
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by("-publish")[:count]
    return {"latest_posts": latest_posts}


@register.inclusion_tag("blog/popular_posts.html")
def show_popular_posts(count=5):
    popular_posts = (
        PostStatistic.objects.filter(
            date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]
        )
        .values("post__title", 'post__slug', 'post__category__slug')
        .annotate(views=Sum("views"))
        .order_by("-views")[:count]
    )
    return {"popular_posts": popular_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count("comments")).order_by(
        "-total_comments"
    )[:count]

@register.simple_tag
def get_views_post(pk):
    return PostStatistic.objects.filter(post=pk).aggregate(Sum("views"))['views__sum']


@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.filter
def user_in(objects, user):
    if user.is_authenticated:
        return objects.filter(user=user).exists()
    return False

@register.inclusion_tag('comments/comments.html', takes_context=True)
def comments_show(context, pk):
    return {"comments": Comment.objects.filter(object_id=pk, active=True), "context": context}
