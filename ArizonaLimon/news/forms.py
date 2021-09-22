from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ArticlesForm(ModelForm):
	class Meta:
		model = Articles
		fields = ['title', 'text', 'date']

		widgets = {
			'title': TextInput(attrs = {
				'class': 'form-control',
				'placeholder': 'На кого?',
			}),
			'text': Textarea(attrs = {
				'class': 'form-control',
				'placeholder': 'Суть жалобы.',
			}),
			'date': DateTimeInput(attrs = {
				'class': 'form-control',
				'placeholder': 'Дата публикации',
			}),

		}