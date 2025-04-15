from django.urls import path
from . import views

"""urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('novo/', views.create_card, name='create_card'),  # Nome correto aqui
    path('editar/<int:card_id>/', views.edit_card, name='edit_card'),
    path('excluir/<int:card_id>/', views.delete_card, name='delete_card'),
]"""

urlpatterns = [
    path("", views.exibir_cards, name="exibir_cards"),
    path("novo_card/", views.create_card, name="create_card"),
    path("editar_card/<int:card_id>/", views.edit_card, name="edit_card"),
    path("excluir_card/<int:card_id>/", views.delete_card, name="delete_card"),
]
