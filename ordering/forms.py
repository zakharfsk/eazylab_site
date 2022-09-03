from django import forms

from ordering.models import Order


class OrderingForm(forms.ModelForm):
    type_work = forms.ChoiceField(
        required=True,
        choices=(
            ('Практична робота', 'Практична робота'),
            ('Лабораторна робота', 'Лабораторна робота'),
            ('Репетиторство', 'Репетиторство'),
            ('Курсова робота', 'Курсова робота'),
            ('Контрольна робота', 'Контрольна робота'),
            ('Реферат', 'Реферат'),
        )
    )
    subject = forms.CharField(max_length=100, required=True)
    name_work = forms.CharField(max_length=100, required=True)
    deadline = forms.DateField(required=True)
    description_work = forms.CharField(required=False, max_length=1000)
    file_order = forms.FileField(required=False)

    class Meta:
        model = Order
        fields = ('type_work', 'subject', 'name_work', 'deadline', 'description_work', 'file_order', 'cost_work', )
