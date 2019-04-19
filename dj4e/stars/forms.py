from django.forms import ModelForm
from stars.models import Higher

class HigherForm(ModelForm):
    class Meta:
        model = Higher
        fields = '__all__'
