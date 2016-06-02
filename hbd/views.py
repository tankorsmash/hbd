import time
import datetime

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, FormView

from hbd.models import User, Cheers, Birthday
from hbd.forms import AddUserForm

class IndexView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)

		context['users'] = User.objects.all()
		context['cheers'] = Cheers.objects.all()
		context['birthdays'] = Birthday.objects.all()

		print "in context methofd"
		return context

class AddUserView(FormView):
	template_name = "add_user.html"

	form_class = AddUserForm
	
	def get_success_url(self):
		return reverse("index")

	def form_valid(self, form):
		#temp username
		form.instance.username = time.time()
		form.save()
		return super(AddUserView, self).form_valid(form)

class TodayView(TemplateView):
	template_name = "today.html"

	def get_context_data(self, **kwargs):
		context = super(TodayView, self).get_context_data(**kwargs)
		context['user'] = User.objects.get(id=self.kwargs.get("user_id", 1))

		#from Jan 1st offset by a number of days
		today = datetime.date(year=2000, month=1, day=1) + datetime.timedelta(days=int(self.kwargs.get("days", 0)))
		context['today'] = today.strftime("%d %b")

		context['birthdays'] = User.objects.filter(birthday__date__month=today.month, birthday__date__day=today.day)
		return context
