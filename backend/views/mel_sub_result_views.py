from django.contrib import messages
from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from app import settings
from app.models import Operators, Mel_Results, Mel_Sub_Results
from app.utils import Utils
from backend.forms.mel_result_forms import MelSubResultCreateForm, MelSubResultUpdateForm


# noinspection PyUnusedLocal, PyShadowingBuiltins
def create(request, id):
    template_url = 'mel-sub-results/create.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_MEL_RESULTS_CREATE in auth_permissions.values():
            try:
                mel_result = Mel_Results.objects.get(mel_result_id=id)
                if request.method == 'POST':
                    form = MelSubResultCreateForm(request.POST)
                    # noinspection PyArgumentList
                    if form.is_valid():
                        model = Mel_Sub_Results()
                        model.mel_results_mel_result_id = mel_result.mel_result_id
                        model.mel_sub_result_details = form.cleaned_data['mel_sub_result_details']

                        model.mel_result_created_at = Utils.get_current_datetime_utc()
                        model.mel_result_created_id = operator.operator_id
                        model.mel_result_created_by = operator.operator_name
                        model.mel_sub_result_created_department = operator.operator_department
                        model.mel_sub_result_created_role = operator.operator_role

                        model.mel_sub_result_updated_at = Utils.get_current_datetime_utc()
                        model.mel_sub_result_updated_id = operator.operator_id
                        model.mel_sub_result_updated_by = operator.operator_name
                        model.mel_sub_result_updated_department = operator.operator_department
                        model.mel_sub_result_updated_role = operator.operator_role

                        # noinspection PyCallByClass,PyTypeChecker
                        model.save('Created')

                        messages.success(request, 'Added successfully.')
                        return redirect(reverse("mel_results_view", kwargs={'pk': id}))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("mel_results_view", kwargs={'pk': id}))

                else:
                    form = MelSubResultCreateForm()

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_MEL_DEPARTMENT_RESULTS,
                        'title': Mel_Sub_Results.TITLE,
                        'name': Mel_Sub_Results.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                    }
                )
            except(TypeError, ValueError, OverflowError, Mel_Results.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update(request, pk):
    template_url = 'mel-sub-results/update.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_MEL_RESULTS_UPDATE in auth_permissions.values():
            try:
                model = Mel_Sub_Results.objects.get(mel_sub_result_id=pk)
                if request.method == 'POST':

                    form = MelSubResultUpdateForm(request.POST)

                    # noinspection PyArgumentList
                    if form.is_valid():
                        model.mel_sub_result_details = form.cleaned_data['mel_sub_result_details']

                        model.mel_sub_result_updated_at = Utils.get_current_datetime_utc()
                        model.mel_sub_result_updated_id = operator.operator_id
                        model.mel_sub_result_updated_by = operator.operator_name
                        model.mel_sub_result_updated_department = operator.operator_department
                        model.mel_sub_result_updated_role = operator.operator_role

                        model.save()

                        messages.success(request, 'Updated successfully.')
                        return redirect(reverse("mel_results_view", kwargs={'pk': model.mel_results_mel_result_id}))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("mel_results_view", kwargs={'pk': model.mel_results_mel_result_id}))
                else:
                    form = MelSubResultUpdateForm(
                        initial={
                            'mel_sub_result_details': model.mel_sub_result_details,
                        }
                    )

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_MEL_DEPARTMENT_RESULTS,
                        'title': Mel_Sub_Results.TITLE,
                        'name': Mel_Sub_Results.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                        'model': model,
                    }
                )
            except(TypeError, ValueError, OverflowError, Mel_Sub_Results.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')
