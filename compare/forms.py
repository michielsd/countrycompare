from django import forms

from compare.models import WorldBorder

class ComparisonForm(forms.Form):

    country_1 = forms.ModelMultipleChoiceField(
        queryset=WorldBorder.objects.all()
    )
    
    country_2 = forms.ModelMultipleChoiceField(
        queryset=WorldBorder.objects.all()
    )
    