from django.urls import path
from .views import (DrillView, AnswerView)

app_name = 'xword_data'

urlpatterns = [
    path('', DrillView.as_view(), name='home'),
    path('answer/', AnswerView.as_view(), name='answer')
]
