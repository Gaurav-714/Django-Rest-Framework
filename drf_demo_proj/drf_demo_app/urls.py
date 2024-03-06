# New File Created..

from django.urls import path
from .views import *

# To Create API's In A Simplest Way...
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'todo-view-set', TodoViewSet, basename = 'todo')


urlpatterns = [
    path('', home, name = 'home'),

    path('get-todo/', get_todo, name = 'get_todo'),      #Insted of these 3..
    path('post-todo/', post_todo, name = 'post_todo'),   #Insted of these 3..
    path('patch-todo/', patch_todo, name = 'patch_todo'),#Insted of these 3..

    path('todo/', TodoView.as_view()), # We Can Do This.. The Simplest Way..
]

urlpatterns += router.urls