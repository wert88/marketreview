from django.contrib import admin
from django.urls import path, include
from app import views
from .views import contactView
	
app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
	
	path('sports/', views.SportsView.as_view(), name='sports'),
	path('health/', views.HealthView.as_view(), name='health'),
	path('books/', views.BooksView.as_view(), name='books'),
	path('men_fashion/', views.MFashionView.as_view(), name='men_fashion'),
	path('software/', views.SoftwareView.as_view(), name='software'),
	path('kids/', views.KidsView.as_view(), name='kids'),
	path('electronics/', views.ElectronicsView.as_view(), name='electronics'),
	path('privacypolicy/', views.PrivacypolicyView.as_view(), name='privacypolicy'),
	path('termsofuse/', views.TermsofuseView.as_view(), name='termsofuse'),
	path('aboutus/', views.AboutUsView.as_view(), name='aboutus'),
    path('contact/', contactView, name='contact'),
	

	path('product/<slug>/', views.ItemDetailView.as_view(), name='product'),
    path('search/', views.SearchView.as_view(), name='search'),
	

]
  