from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeView

from .views import (
    add_product,
    login_,
    add_user,
    search_product,
    delete_user
)


urlpatterns = [
    path('add/product', add_product, name="add_product"),
    path('login', login_, name="login"),
    path('add/user/', add_user, name="add_user"),
    path('delete/user/<int:id>', delete_user, name="delete_user"),
    path('', search_product, name="search"),
    path('logout/', LogoutView.as_view(), name='logout'),
]