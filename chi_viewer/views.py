from django.shortcuts import render
from chi_viewer.models import Posting


def home(request):
	context = {'postings_list': Posting.objects.all()}
	return render(request, 'index.html', context)
