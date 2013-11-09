from django.shortcuts import render, loader, RequestContext, HttpResponse, HttpResponseRedirect
from django.db.models import Min
from random import randint
from django.views.generic import TemplateView

from unicodedata import normalize

from models import newMovie

def safe_str(s):
	return normalize('NFKD', s).encode('ascii', 'ignore')
def make_js(mv_list):
	return [[[safe_str(mv.title), safe_str(mv.imdb_id), safe_str(mv.poster)] for mv in mv_grp] for mv_grp in mv_list]

# Create your views here.
def index(request):

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


# def trailerplay(request):
# 	if request.method == 'GET':
# 		# <view logic>
# 		return HttpResponse('result')

class trailerplay(TemplateView):
	def get(self, request):
		# <view logic>
		return HttpResponse(template.render)


# class trailerplay(TemplateView):
# 	template = loader.get_template('movies/trailerplay.html')
# 	def get(self, request, *args, **kwargs):
# 		# return HttpResponse(template.render())

# 	def post(self, request, *args, **kwargs):
# 		pass
	
