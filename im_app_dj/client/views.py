from client.models import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'index.html')

class ClientListView(LoginRequiredMixin, generic.ListView):
    model = attr_company
    context_object_name = 'client_list'
    queryset = attr_company.objects.filter(is_not_active=False)
    template_name = 'client/company_list.html'

class ClientListNAView(LoginRequiredMixin, generic.ListView):
    model = attr_company
    context_object_name = 'client_list'
    queryset = attr_company.objects.filter(is_not_active=True)
    template_name = 'client/company_list_not_active.html'

class ClientDetailView(LoginRequiredMixin,generic.DetailView):
    model = attr_company

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet
        company_id = attr_company.objects.get(company_name=context['attr_company'])
        context['assets'] = attr_asset.objects.filter(company=company_id)
        context['employees'] = attr_employee.objects.filter(company=company_id)
        context['related'] = attr_related.objects.filter(company=company_id)

        return context

class UpdateClientView(LoginRequiredMixin,generic.edit.UpdateView):
    model = attr_company
    fields = [
        'is_not_active',
        'company_name',
        'registration_no',
        'main_address',
        'post_address',
        'bank_iban',
        'keyword',
        'comp_date',
        'vat_date',
        'mun_period_from',
        'mun_period_to',
        'nace_code',
        'nace_desc',
        'contr_id',
        'comp_form',
        'risk_asses_1',
        'risk_asses_2',
        'risk_asses_3',
        'risk_asses_4',
        'risk_asses_5',
        'risk_asses_6',
        'risk_asses_7',
        'risk_asses_8',
        'risk_asses_9',
        'risk_asses_10',
        'risk_asses_11',
        ]
    template_name_suffix = '_update_form'


class DeleteClientView(LoginRequiredMixin,generic.edit.DeleteView):
    model = attr_company
    success_url = reverse_lazy('clients')

class CreateClientView(LoginRequiredMixin,generic.edit.CreateView):
    model = attr_company
    fields = [
        'company_name',
        'registration_no',
        'main_address',
        'post_address',
        'bank_iban',
        'keyword',
        'comp_date',
        'vat_date',
        'mun_period_from',
        'mun_period_to',
        'nace_code',
        'nace_desc',
        'contr_id',
        'comp_form',
        'risk_asses_1',
        'risk_asses_2',
        'risk_asses_3',
        'risk_asses_4',
        'risk_asses_5',
        'risk_asses_6',
        'risk_asses_7',
        'risk_asses_8',
        'risk_asses_9',
        'risk_asses_10',
        'risk_asses_11',
    ]

class AssetDetailView(LoginRequiredMixin,generic.DetailView):
    model = attr_asset

class UpdateAssetView(LoginRequiredMixin,generic.edit.UpdateView):
    model = attr_asset
    fields = [
        'asset_type',
        'asset_id',
        'asset_contr_id',
        'asset_desc'
        ]
    template_name_suffix = '_update_form'

class DeleteAssetView(LoginRequiredMixin,generic.edit.DeleteView):
    model = attr_asset
    success_url = reverse_lazy('clients')

class CreateAssetView(LoginRequiredMixin,generic.edit.CreateView):
    model = attr_asset
    fields = [
        'asset_type',
        'asset_id',
        'asset_contr_id',
        'asset_desc',
        ]

    def form_valid(self, form):
        company_object = attr_company.objects.get(slug__exact=self.kwargs['slug'])
        _company_id = get_object_or_404(attr_company, pk=company_object.id)
        form.instance.company = _company_id
        return super(CreateAssetView, self).form_valid(form)

class EmployeeDetailView(LoginRequiredMixin,generic.DetailView):
    model = attr_employee

class UpdateEmployeeView(LoginRequiredMixin,generic.edit.UpdateView):
    model = attr_employee
    fields = [
        'employee',
        'role',
        'email',
        'tele',
        'is_board',
        'is_sh_holder',
        'is_main_benf',
        ]
    template_name_suffix = '_update_form'

class DeleteEmployeeView(LoginRequiredMixin,generic.edit.DeleteView):
    model = attr_employee
    success_url = reverse_lazy('clients')

class CreateEmployeeView(LoginRequiredMixin,generic.edit.CreateView):
    model = attr_employee
    fields = [
        'employee',
        'role',
        'email',
        'tele',
        'is_board',
        'is_sh_holder',
        'is_main_benf',
        ]

    def form_valid(self, form):
        company_object = attr_company.objects.get(slug__exact=self.kwargs['slug'])
        _company_id = get_object_or_404(attr_company, pk=company_object.id)
        form.instance.company = _company_id
        return super(CreateEmployeeView, self).form_valid(form)

class RelatedDetailView(LoginRequiredMixin,generic.DetailView):
    model = attr_related

class UpdateRelatedView(LoginRequiredMixin,generic.edit.UpdateView):
    model = attr_related
    fields = [
        'rel_comp_name',
        'rel_comp_reg',
        'description'
        ]
    template_name_suffix = '_update_form'

class DeleteRelatedView(LoginRequiredMixin,generic.edit.DeleteView):
    model = attr_related
    success_url = reverse_lazy('clients')

class CreateRelatedView(LoginRequiredMixin,generic.edit.CreateView):
    model = attr_related
    fields = [
        'rel_comp_name',
        'rel_comp_reg',
        'description',
        ]

    def form_valid(self, form):
        company_object = attr_company.objects.get(slug__exact=self.kwargs['slug'])
        _company_id = get_object_or_404(attr_company, pk=company_object.id)
        form.instance.company = _company_id
        return super(CreateRelatedView, self).form_valid(form)
