# Uncomment the imports before you add the code
# from django.urls import path
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    
    # # path for registration
    path(route='register', view=views.registration, name='registration'),
    # path for login
     path(route='login', view=views.login_user, name='login'), 
    # path for dealer reviews view

    path(route='dealer/<int:dealer_id>/reviews/', view=views.get_dealer_reviews, name='dealer-reviews'),

    # path for add a review view

    path(route='dealer/<int:dealer_id>/reviews/add/', view=views.add_review, name='add-review'),
    path(route='get_cars', view=views.get_cars, name ='getcars'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
