from django import forms
from .models import Table,Rest,Product
from django.http import HttpResponseRedirect
from django.forms import ModelChoiceField

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('table_num',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['table'].queryset = Table.table_num.none()

class OrderRegister(forms.Form):
      table_num =forms.ModelChoiceField(queryset=Table.objects.filter(state=0))


class ItemState1(forms.Form):
    Item = forms.ModelChoiceField(queryset=Product.objects.filter(state=1))

class AddGet(forms.Form):


  #count = forms.ModelChoiceField(choices=('1','2'))

  count = forms.IntegerField(min_value=1,required=True, widget=forms.NumberInput(attrs={'size':100}))

class product_Add(forms.ModelForm):
    CHOICES = [(1, 'Food'),
               (2, 'Drink'),
               (3, 'Swit')]


    Type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "namear",
            "descriptionar",
            "nameru",
            "descriptionru",

            "Price",
            "image",
            "Type",

        ]



class PostForm(forms.ModelForm):
      class Meta:
          model=Rest
          fields=[
              "name",
              "address",
              "phone",
              "logo",
          ]



class new(forms.Form):
      order = forms.IntegerField(required=True,min_value=1,max_value=10000, widget=forms.NumberInput())
      table = forms.IntegerField(min_value=1,max_value=1000,required=True, widget=forms.NumberInput())