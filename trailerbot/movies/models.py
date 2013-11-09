from django.db import models

class Movie (models.Model):
	title = models.CharField(max_length=500)
	imdb_id = models.CharField(max_length=500)
	poster = models.URLField(max_length=500)
	date = models.CharField(max_length=500)
	trailer = models.CharField(max_length=500)

class newMovie (models.Model):
	title = models.CharField(max_length=500)
	imdb_id = models.CharField(max_length=500)
	poster = models.URLField(max_length=500)
	date = models.CharField(max_length=500)
	trailer = models.CharField(max_length=500)
	
	def __unicode__(self):
		return u"%s" % self.id

