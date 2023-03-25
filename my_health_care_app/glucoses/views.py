from django.contrib.messages.views import SuccessMessageMixin
from django.forms import BaseForm, DateTimeInput
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.db.models import QuerySet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Glucose
# Create your views here.

class GlucoseListView(LoginRequiredMixin,ListView):
    model = Glucose

    def get_queryset(self) -> QuerySet:
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset

glucoses_list_view = GlucoseListView.as_view()


class GlucoseDetialView(LoginRequiredMixin,DetailView):
    model = Glucose


glucose_detail_view = GlucoseDetialView.as_view()


class GlucoseCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Glucose
    fields = ['value','record_datetime','notes']
    success_url = reverse_lazy("glucoses:list")
    success_message = "Succesfully added!"

    def get_form(self,form_class = None):
        form = super().get_form(form_class)
        form.fields['record_datetime'].widget = DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'form-control'}
        )
        return form

    def form_valid(self, form: BaseForm) -> HttpResponse:
        bloodpressure = form.save(commit=False)
        bloodpressure.user = self.request.user
        bloodpressure.save()
        return super().form_valid(form)

glucoses_create_view = GlucoseCreateView.as_view()

class GlucosesDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Glucose

    success_message = "Deleted succesfully!"
    success_url = reverse_lazy("glucoses:list")

glucoses_delete_view = GlucosesDeleteView.as_view()


class GlucoseUpadteView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Glucose
    fields = ["value","record_datetime","notes"]
    template_name = "glucoses/glucose_update.html"
    success_message = "Measurement updated."

    def get_success_url(self):
        g_id = self.kwargs['pk']
        return reverse_lazy('glucoses:detail', kwargs={'pk': g_id})

glucoses_update_view = GlucoseUpadteView.as_view()
