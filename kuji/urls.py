from django.urls import path

from kuji.views import MemberUpdateView

app_name = 'kuji'

urlpatterns = [
    path('', MemberUpdateView.as_view(), name='index'),
]