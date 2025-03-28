from django.urls import path
from .views import HomePageView, AboutPageView, ImageViewNoDI, ProductIndexView, ProductShowView, ProductCreateView, CartView, CartRemoveAllView, RegisterView
from django.contrib.auth import views as auth_views
from .utils import ImageLocalStorage
from .views import ImageViewFactory

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='index'), 
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('cart/', CartView.as_view(), name='cart_index'), 
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'), 
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
    # Rutas de autenticación
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
    path('imagesnotid/', ImageViewNoDI.as_view(), name='imagesnotid'), 
    path('imagesnotid/save', ImageViewNoDI.as_view(), name='imagesnotid_save'), 
]