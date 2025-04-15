from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Card
from .forms import CardForm

"""def gallery(request):
    return render(request, 'cards/gallery.html') 
"""


# Exibir a galeria de cards
def exibir_cards(request):
    cartoes = Card.objects.all()

    return render(request, "cards/gallery.html", {"cards": cartoes})


# Salva um novo card no banco de Dados ou exibir um formulario html


def create_card(request):
    if request.method == "POST":
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("exibir_cards")
    else:
        formulario = CardForm()
        return render(request, "cards/card_form.html", {"form": formulario})


# Editar um card existente


def edit_card(request, card_id):
    cartao = get_object_or_404(Card, id=card_id)
    if request.method == "POST":
        form = CardForm(request.POST, request.FILES, instance=cartao)
        if form.is_valid():
            form.save()
            return redirect("exibir_cards")
    else:
        form = CardForm(instance=cartao)

        return render(request, "cards/card_form.html", {"form": form})


# Excluir um card
def delete_card(request, card_id):
    cartao = get_object_or_404(Card, id=card_id)
    if request.method == "POST":
        cartao.delete()
        return redirect("exibir_cards")
    else:
        return render(request, "cards/card_confirm_delete.html", {"card": cartao})
