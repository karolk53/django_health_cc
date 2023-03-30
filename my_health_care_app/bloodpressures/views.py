from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.forms import BaseForm
from django.forms.widgets import DateTimeInput
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import BloodPressure

# Create your views here.


class BloodPressureListView(LoginRequiredMixin, ListView):
    model = BloodPressure

    def get_queryset(self) -> QuerySet:
        return self.model.objects.filter(user=self.request.user).order_by(
            "-examination_datetime"
        )


bloodpressuer_list_view = BloodPressureListView.as_view()


class BloodPressureCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = BloodPressure
    fields = ["systlic", "diastolic", "pulse", "examination_datetime", "notes"]
    success_url = reverse_lazy("bloodpressures:list")
    success_message = "Added succesfully!"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["examination_datetime"].widget = DateTimeInput(
            attrs={"type": "datetime-local", "class": "form-control"}
        )
        return form

    def form_valid(self, form: BaseForm) -> HttpResponse:
        bloodpressure = form.save(commit=False)
        bloodpressure.user = self.request.user
        bloodpressure.save()
        return super().form_valid(form)


bloodpressuer_create_view = BloodPressureCreateView.as_view()


class BloodPressureDetailView(LoginRequiredMixin, DetailView):
    model = BloodPressure
    fields = ["systlic", "diastolic", "pulse", "examination_datetime", "notes"]


bloodpressuer_detail_view = BloodPressureDetailView.as_view()


class BloodPressureUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = BloodPressure
    fields = ["systlic", "diastolic", "pulse", "examination_datetime", "notes"]
    template_name = "bloodpressures/bloodpressure_update.html"
    success_message = "Updated succesfully!"

    def get_success_url(self):
        g_id = self.kwargs["pk"]
        return reverse_lazy("bloodpressures:detail", kwargs={"pk": g_id})


bloodpressure_update_view = BloodPressureUpdateView.as_view()


class BloodPressureDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = BloodPressure

    success_url = reverse_lazy("bloodpressures:list")
    success_message = "Measuremen deleted"


bloodpressure_delete_view = BloodPressureDeleteView.as_view()
