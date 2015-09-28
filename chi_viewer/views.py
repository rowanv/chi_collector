from django.shortcuts import render
from chi_viewer.models import Posting
from chi_viewer.forms import PostingForm


def home(request):

	if request.method == 'POST':
		form = PostingForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/')
	else:
		form = PostingForm()

	context = {'postings_list': Posting.objects.all(),
				'form': form}
	return render(request, 'index.html', context)
