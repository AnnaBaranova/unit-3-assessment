from django.shortcuts import redirect, render
from .models import Widget
from .forms import WidgetForm
from django.views.generic.edit import DeleteView
from django.db.models import Sum


from main_app import models


def index (request):
    widget = Widget.objects.all()
    total_quantity = Widget.objects.all().aggregate(Sum('quantity'))
    total_quantity_num = total_quantity['quantity__sum']
    widget_form = WidgetForm()
    return render(request, 'index.html',{
        'widget': widget, 'widget_form': widget_form,
        'total_quantity': total_quantity_num
  })

def widget_create(request):
  form = WidgetForm(request.POST)
  if form.is_valid():
    new_widget = form.save(commit=False)
    print(new_widget)
    new_widget.save()
  return redirect('/')


class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'
