from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Clue, Entry
import random
# Create your views here.
class DrillView(ListView):
    model = Clue
    template_name = "drill.html"

#randomized the clue objects
    def get_queryset(self):
        return Clue.objects.order_by('?')


class AnswerView(TemplateView):
    template_name = "answer.html"
