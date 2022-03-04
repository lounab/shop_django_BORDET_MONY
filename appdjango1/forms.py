from django import forms
from .models import Question
 
 
# creating a form
class Appform(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Question
 
        # specify fields to be used
        fields = [
            "titre","prix","quantite","lienimage","description",
        ]


class Achatform(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Question
 
        # specify fields to be used
        fields = [
            "quantite",
        ]