# forms.py
from django import forms

class ExampleForm(forms.Form):
    # Example field for user input
    example_field = forms.CharField(
        max_length=100,
        required=True,
        help_text="Enter some text (max 100 characters)"
    )

