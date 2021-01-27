from django.views.generic import ListView

from .models import News


class AggrecateVievs(ListView):
    template_name = 'aggregator/index.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        if self.request.GET.get('category') is not None:
            return News.objects.filter(category=self.request.GET.get('category'))
        elif self.request.GET.get('source') is not None:
            return News.objects.filter(source=self.request.GET.get('source'))
        else:
            return News.objects.all()


