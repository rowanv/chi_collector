from django import forms

class PostingForm(forms.Form):
	check1 = forms.BooleanField(label='Check 1')