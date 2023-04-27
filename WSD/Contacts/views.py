from .models import Branch, Manager, Ticket
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def testing(request):
  tickets = Ticket.objects.all().count()
  template = loader.get_template('home.html')
  context = {
    'ticket': tickets,
  }
  return HttpResponse(template.render(context, request))

class HomePageView(TemplateView):
    model = Ticket.objects.all().count()
    print(Ticket.objects.all().count())
    template_name = 'home.html'

class ManagerSearchResultsView(ListView):
    model = Manager
    template_name = 'manager_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("qm")
        print(query)
        return Manager.objects.filter(
            Q(name__icontains=query) | Q(position__icontains=query))

class BranchSearchResultsView(ListView):
    model = Branch
    template_name = 'branch_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("qb")
        print(query)
        return Branch.objects.filter(
            Q(name__icontains=query))

class ManagerView(ListView):
    model = Manager 
    template_name = 'manager.html'

class BranchView(ListView):
    model = Branch 
    template_name = 'branch.html'