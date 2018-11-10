from django import forms
import pandas as pd

# our new form


class ContactForm(forms.Form):
	choices =[('Yes','Yes'),('No','No')]
	relevant = forms.ChoiceField(choices=choices, widget=forms.RadioSelect())
	choices =[('WET','WET'),('B&F','B&F'),('PT&D','PT&D'),('TI','TI'),('SW','SW'),('HC','HC'),('GS','GS'),('MMH','MMH'),('RE','RE'),('DC','DC')]
	dept = forms.ChoiceField(choices=choices)
	choices =[('Domestic','Domestic'),('International','International'),('Middle East','Middle East')]
	location = forms.ChoiceField(choices=choices)
	new_category = forms.CharField(required=True)
	description	 = forms.CharField(required=True,widget=forms.Textarea(attrs={'rows':1, 'cols':40}))