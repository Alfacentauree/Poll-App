from django.forms import ModelForm
from .models import Poll


class Create(ModelForm):
    class Meta:
        model = Poll
        fields = ['questions','option_one','option_two','option_three']


