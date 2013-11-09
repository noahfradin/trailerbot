from django.shortcuts import render, loader, RequestContext, HttpResponse, HttpResponseRedirect
from django.db.models import Min
from random import randint
from django.views.generic import TemplateView

from unicodedata import normalize

from models import newMovie

import logging


def safe_str(s):
	return normalize('NFKD', s).encode('ascii', 'ignore')
    
def make_js(mv_list):
	return [[[safe_str(mv.title), safe_str(mv.imdb_id), safe_str(mv.poster)] for mv in mv_grp] for mv_grp in mv_list]

# Create your views here.
def index(TemplateView):

	def get(self, request, *args, **kwargs):
		return HttpResponseRedirect(template.render(context))

	def post(self, request, *args, **kwargs):
		# post
		pass

	db_length = len(newMovie.objects.all())
	min_id = newMovie.objects.aggregate(Min('id'))['id__min']
	movies_list = []
	
	for j in range(3):
		temp = []
		while len(temp) < 8:
			idx = randint(min_id, min_id+db_length)
			movie_data = newMovie.objects.get(id=idx)
			if 'imdb' in str(movie_data.poster):
				temp.append(movie_data)
		movies_list.append(temp)

	template = loader.get_template('movies/index.html')
	context = RequestContext(request, {
		'movies_list': make_js(movies_list),
	})
	return HttpResponse(template.render(context))


# def trailerplay(request):
# 	if request.method == 'GET':
# 		# <view logic>
# 		return HttpResponse('result')

class trailerplay(TemplateView):
	def get(self, request):
		template = loader.get_template('movies/trailerplay.html')
		db_length = len(newMovie.objects.all())
		min_id = newMovie.objects.aggregate(Min('id'))['id__min']
		idx = randint(min_id, min_id+db_length)
		movie_data = newMovie.objects.get(id=idx)
		

		# for inp in inputs:
		# 	titles.append(request[inp])

		# pool = []
		# for title in titles:
		# 	pool.extend(get_tastekid_recs(title))
            
		# next_two = get_random_two(pool)
        
		context = RequestContext(request, {
			'movie_data': str(movie_data.trailer).strip(),
		})
		return HttpResponse(template.render(context))

def get_random_two(pool):
    return [pool[randint(0,len(pool))] for i in range(2)]
        
# class trailerplay(TemplateView):
# 	template = loader.get_template('movies/trailerplay.html')
# 	def get(self, request, *args, **kwargs):
# 		# return HttpResponse(template.render())

# 	def post(self, request, *args, **kwargs):
# 		pass
	
