from django.shortcuts import render


def index(request):
	data = {
		'title': 'Главная',
	}
	return render(request, 'main/index.html', data)


def rules(request):
	data = {
		'title': 'Правила',
	}
	return render(request, 'main/rules.html', data)