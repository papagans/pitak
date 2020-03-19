from django.shortcuts import render
from accounts.models import Profile
from django.views.generic import TemplateView, ListView


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = ''
    model = Profile

    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     context.update({
    #         'announcements': Announcements.objects.order_by('-created_at')[0:2]
    #     })
    #     return context

    # def get_queryset(self):
    #     return News.objects.order_by('-created_at')[0:2]