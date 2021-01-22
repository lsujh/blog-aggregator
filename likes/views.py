from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import LikeDislike
from comments.models import Comment
from blog.models import Post


def like_dislike(self):
    request = self.request
    try:
        mark = request.GET.get('mark').split('-')
        vote = 0
        if 'like_post' == mark[0]:
            obj = Post.published.get(id=int(mark[1]))
            vote = 1
        elif 'like_comment' == mark[0]:
            obj = Comment.objects.get(id=int(mark[1]))
            vote = 1
        elif 'dislike_post' == mark[0]:
            obj = Post.published.get(id=int(mark[1]))
            vote = -1
        elif 'dislike_comment' == mark[0]:
            obj = Comment.objects.get(id=int(mark[1]))
            vote = -1
        elif 'remove_mark_post' == mark[0]:
            obj = Post.published.get(id=int(mark[1]))
            vote = 0
        elif 'remove_mark_comment' == mark[0]:
            obj = Comment.objects.get(id=int(mark[1]))
            vote = 0

        obj_type = ContentType.objects.get_for_model(obj)

        if vote:
            LikeDislike.objects.update_or_create(
                content_type=obj_type, object_id=obj.id, user=request.user, defaults={'vote': vote})
        else:
            LikeDislike.objects.filter(
                content_type=obj_type, object_id=obj.id, user=request.user).delete()
    except:
        pass

    success_url = reverse_lazy('blog:post_detail', args=(self.kwargs.get('category'),
                                                         self.kwargs.get('slug')))
    return redirect(success_url)

