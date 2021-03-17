from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('fullname','mobile','pizza_name','size')


    def __init__(self, *args, **kwargs):
        super(OrderForm,self).__init__(*args, **kwargs)
        self.fields['size'].empty_label = "Select"
        self.fields['pizza_name'].required = False
