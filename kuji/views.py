import random

from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, FormView

from kuji.forms import MemberForm
from kuji.models import Member, Seat


class MemberUpdateView(FormView):
    form_class = MemberForm
    success_url = reverse_lazy('kuji:index')
    template_name = 'kuji/member_form.html'

    message_template = '社員番号{no}さんの座席は{seat}です'

    def form_valid(self, form):
        # 座席番号が指定されているかを確認
        member = get_object_or_404(Member, no=form.cleaned_data['no'])
        # member = Member.objects.get(no=form.cleaned_data['no'])

        # 指定されている場合、その番号を取得して表示
        if member.seat:
            messages.success(self.request,
                             self.message_template.format(no=member.no, seat=member.seat))
            return super().form_valid(form)

        # 指定されていない場合、残りの座席を取得
        rest_seats = Seat.objects.all().values_list('rest_no', flat=True)

        # ランダムで座席を取得
        your_seat = random.choice(list(rest_seats))

        # 残り座席から、取得した座席を削除
        Seat.objects.filter(rest_no=your_seat).delete()

        # メンバーに割当
        member.seat = your_seat
        member.save()

        # 番号を表示
        messages.success(self.request,
                         self.message_template.format(no=member.no, seat=member.seat))
        return super().form_valid(form)


class KujiAPI(View):
    pass
    # 自分の番号を取得するAPI

    # あれば、その番号を返す

    # なければ、「ないよ」と返す
