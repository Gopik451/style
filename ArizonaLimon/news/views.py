from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


def news_home(request):
	news = Articles.objects.all()
	data = {
		'news': news,
		'title': 'Жалобы'
	}
	return render(request, 'news/news_home.html', data)


class NewsDetailView(DetailView):
	model = Articles
	temlate_name = 'news/articles_detail.html'
	context_object_name = 'article'


def create(request):
	error = ''
	if request.method == 'POST':
		form = ArticlesForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('news_home')
		else:
			error = 'Ошибка'

	form = ArticlesForm()
	data = {
		'form': form,
		'title': 'Подача жалобы',
		'error': error
	}

	return render(request, 'news/create.html', data)