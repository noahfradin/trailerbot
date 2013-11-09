from django.shortcuts import render, loader, RequestContext, HttpResponse
from django.db.models import Min
from random import randint

from unicodedata import normalize

from models import newMovie

def safe_str(s):
	return normalize('NFKD', s).encode('ascii', 'ignore')
def make_js(mv_list):
	return [[[safe_str(mv.title), safe_str(mv.imdb_id), safe_str(mv.poster)] for mv in mv_grp] for mv_grp in mv_list]

# Create your views here.
def index(request):
	db_length = len(newMovie.objects.all())
	min_id = newMovie.objects.aggregate(Min('id'))['id__min']
	movies_list = []
	for j in range(3):
		temp = []
		for m in range(8):
			idx = randint(min_id, min_id+db_length)
			movie_data = newMovie.objects.get(id=idx)
			temp.append(movie_data)
		movies_list.append(temp)

	template = loader.get_template('movies/index.html')
	context = RequestContext(request, {
		'movies_list': make_js(movies_list),
	})
	return HttpResponse(template.render(context))