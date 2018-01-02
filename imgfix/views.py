from django.views.generic import CreateView, ListView
from .models import Person
from .forms import PersonForm


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = "imgfix/form.html"
    success_url = "/imgfix"  # 成功時にリダイレクトするURL    
    
    
class PersonListView(ListView):
    model = Person
    template_name = "imgfix/list.html"
