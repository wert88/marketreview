from django.shortcuts import render, reverse, redirect
from django.views.generic import View, DetailView, ListView
from .models import Item, BannerImg
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import UserForm

from django_user_agents.utils import get_user_agent

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

class IndexView(View):

	def get(self, request):
		all = Item.objects.all()
		banner = BannerImg.objects.all()
		
		user_list = Item.objects.all()
		page = request.GET.get('page', 1)
		
		paginator = Paginator(user_list, 4)
		try:
			users = paginator.page(page)
		except PageNotAnInteger:
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)
		
		new = all[0::-1]

		if len(new) > 7:
			new = new[0:8]
		else:
			new = new[0:]


		popular = Item.objects.filter(label='P')
		contex = {'all':all,
				  'banner':banner,
				  'popular':popular,
				  'new':new,
				  
				  'users':users,
				}
		return render(request, "app/index.html", contex )
	

class SportsView(View):
	def get(self, request):
		popular = Item.objects.filter(label='P',category='S')
		Items = Item.objects.filter(category='S')
		new = Item.objects.filter(label='S', category='S')
		return render(request, "app/sports.html", {
		'popular':popular,
		'Items':Items,
		'new':new
		})

class HealthView(View):
	def get(self, request):
		
		Items = Item.objects.filter(category='H')
		return render(request, "app/health.html", {"Items":Items})

class BooksView(View):
	def get(self, request):
		
		Items = Item.objects.filter(category='B')
		return render(request, "app/books.html", {"Items":Items})

class MFashionView(View):
	def get(self, request):
		
		Items = Item.objects.filter(category='MF')
		return render(request, "app/men_fashion.html", {"Items":Items})

class SoftwareView(View):
	def get(self, request):
		
		Items = Item.objects.filter(category='SW')
		return render(request, "app/software.html", {"Items":Items})

class KidsView(View):
	def get(self, request):
		
		Items = Item.objects.filter(category='K')
		return render(request, "app/kids.html", {"Items":Items})

class ElectronicsView(View):
	def get(self, request):
	
		Items = Item.objects.filter(category='E')
		return render(request, "app/electronics.html", {"Items":Items})

class PrivacypolicyView(View):
	def get(self, request):
		return render(request, "app/privacypolicy.html")

class TermsofuseView(View):
	def get(self, request):
		return render(request, "app/termsofuse.html")

class AboutUsView(View):
	def get(self, request):
		return render(request, "app/aboutus.html")
		
class ContactUsView(View):
	def get(self, request):
		return render(request, "app/contactus.html")
				
				
class ItemDetailView(DetailView):
    model = Item
    template_name = "app/product.html"


class SearchView(ListView):

	def get(self, request):
		all = Item.objects.all() 
		search = request.GET.get("search_title")
		category = request.GET.get("category")
		category_result = ''
		noresult = ''
		
		if category == '':
			category_result = 'All categories'
		elif category == 'S':
			category_result = 'Sports'
		elif category == 'H':
			category_result = 'Health & Beauty'
		elif category == 'B':
			category_result = 'Books'
		elif category == 'MF':
			category_result = 'Men Fashion'
		elif category == 'K':
			category_result = 'Kids & Babies'
		elif category == 'E':
			category_result = 'Electronics'
		elif category == 'SW':
			category_result = 'Software'
			
		if category != '' and category is not None:
			all = all.filter(category__icontains=category)
		
		if search != '' and search is not None:
			all = all.filter(title__icontains=search)
			if all.__bool__() == False:
				noresult = 'No results found for : ' + '" ' + search + ' "'
				
		contex = {'all':all, 'search_title':search, 'category_result':category_result, 'noresult':noresult}

		return render(request, "app/search.html", contex )

class SignupView(View):
	form_class = UserForm
	template_name = 'registration/signup.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			
			user.set_password(password)
			user.save()

			# if Credential are correct
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('app:index')
		return render(request, self.template_name, {'form':form})

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            form.save()
			
            return redirect('app:index')
    return render(request, "app/contact.html", {'form': form})
