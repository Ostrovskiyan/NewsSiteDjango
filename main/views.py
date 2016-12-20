from django.views.generic.list import ListView

from main.models import News

class StudentListView(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'

    def dispatch(self, request, *args, **kwargs):
        return super(StudentListView, self).dispatch(request, *args, **kwargs)