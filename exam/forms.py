from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms.formsets import formset_factory, BaseFormSet
from django.utils.translation import ugettext_lazy as _
from django.utils.http import int_to_base36



from The_Xaming_Arena.exam.models import Question, Answer, SubmittedAnswers


ANSWER_CHOICES = (('A','A'),('B','B'),('C','C'),('D','D'))

class BaseAnswerFormSet(BaseFormSet):
	def clean(self):
		so= []
		for i in range(0, self.total_form_count()):
		        form = self.forms[i]
			try:
				so.append(form.cleaned_data['options'])
			except KeyError:
				so.append('x')
		return so

class AnswerForm(forms.Form):
	options = forms.ChoiceField(choices = ANSWER_CHOICES, widget = forms.RadioSelect())
	


