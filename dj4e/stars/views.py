from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from stars.models import Lower, Higher
from stars.forms import HigherForm

# Create your views here.

class MainList(LoginRequiredMixin, View) :
    def get(self, request):
        hc = Higher.objects.all().count();
        ll = Lower.objects.all();

        ctx = { 'higher_count': hc, 'lower_list': ll };
        return render(request, 'stars/lower_list.html', ctx)

class HigherView(LoginRequiredMixin,View) :
    def get(self, request):
        hl = Higher.objects.all();
        ctx = { 'higher_list': hl };
        return render(request, 'stars/higher_list.html', ctx)

class HigherCreate(LoginRequiredMixin, View):
    template = 'stars/higher_form.html'
    success_url = reverse_lazy('main_list')
    def get(self, request) :
        form = HigherForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = HigherForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        higher = form.save()
        return redirect(self.success_url)

class HigherUpdate(LoginRequiredMixin, View):
    model = Higher
    success_url = reverse_lazy('main_list')
    template = 'stars/higher_form.html'
    def get(self, request, pk) :
        higher = get_object_or_404(self.model, pk=pk)
        form = HigherForm(instance= higher)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        higher = get_object_or_404(self.model, pk=pk)
        form = HigherForm(request.POST, instance = higher)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class HigherDelete(LoginRequiredMixin, DeleteView):
    model = Higher
    success_url = reverse_lazy('main_list')
    template = 'stars/higher_confirm_delete.html'

    def get(self, request, pk) :
        higher = get_object_or_404(self.model, pk=pk)
        form = HigherForm(instance=higher)
        ctx = { 'higher': higher }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        higher = get_object_or_404(self.model, pk=pk)
        higher.delete()
        return redirect(self.success_url)

# Take the easy way out on the main table
class LowerCreate(LoginRequiredMixin,CreateView):
    model = Lower
    fields = '__all__'
    success_url = reverse_lazy('main_list')

class LowerUpdate(LoginRequiredMixin, UpdateView):
    model = Lower
    fields = '__all__'
    success_url = reverse_lazy('main_list')

class LowerDelete(LoginRequiredMixin, DeleteView):
    model = Lower
    fields = '__all__'
    success_url = reverse_lazy('-main_list')
