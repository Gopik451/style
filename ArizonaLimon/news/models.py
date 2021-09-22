from django.db import models


class Articles(models.Model):
	title = models.CharField('На кого?', max_length = 100)
	text = models.TextField('Суть жалобы.')
	date = models.DateTimeField('Дата публикации', default = '14.11.2021 14:15')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Жалобу'
		verbose_name_plural = 'Жалобы'