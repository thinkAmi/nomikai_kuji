from django import forms


class MemberForm(forms.Form):
    no = forms.CharField(label='社員番号', max_length=6, min_length=6)
