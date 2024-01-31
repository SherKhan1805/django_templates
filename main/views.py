from django.views.generic import ListView

from main.models import Cards


class CardListView(ListView):
    """
    Класс для создания списка блоговых записей
    """
    model = Cards
    # form_class = BlogForm
    template_name = 'main/index.html'
