from django.shortcuts import render
from django.http import JsonResponse
from chi_viewer.models import Posting
from chi_viewer.forms import PostingForm


def home(request):

	if request.method == 'POST':
		form = PostingForm(request.POST)
		if request.is_ajax():
			check_1 = request.POST.get('check_1')
			data = {'check_1': check_1}
			return JsonResponse(data)
	else:
		form = PostingForm()

	context = {'postings_list': Posting.objects.all(),
				'form': form}
	return render(request, 'index.html', context)
