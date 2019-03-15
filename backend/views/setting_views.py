import os
import time

from django.contrib import messages
from django.core.files import File
from django.core.management import call_command
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from app import settings
from app.models import Operators, Backups
from app.utils import Utils
from backend.tables.backup_tables import BackupsTable


# noinspection PyUnusedLocal, PyShadowingBuiltins
@csrf_exempt
def temp_upload(request):
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        if request.POST:
            file_path = settings.MEDIA_ROOT + '/temp/' + request.POST['name']
            image_data = request.POST['data']
            Utils.save_image_base64(image_data, file_path)
            return HttpResponse('success')
        else:
            return HttpResponseBadRequest('no data')


@csrf_exempt
def generate_qr_code(data, size=10, border=0):
    print("QR Data: " + data)
    import qrcode
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=size, border=border)
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image()


@csrf_exempt
def get_qr_code_image(request, size, text):
    print(size)
    print(text)
    qr = generate_qr_code(text, 10, 2)
    response = HttpResponse()
    qr.save(response, "PNG")
    return response

# noinspection PyUnusedLocal
def index(request):
    template_url = 'settings/index.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        return render(
            request, template_url,
            {
                'section': settings.BACKEND_SECTION_SETTINGS,
                'title': 'Settings',
                'name': 'settings',
                'operator': operator,
                'auth_permissions': auth_permissions,
            }
        )


def backup_restore(request):
    template_url = 'settings/backup-restore.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_SETTINGS_VIEW in auth_permissions.values():

            objects = []
            files = []
            for filename in os.listdir('backups'):
                filepath = os.path.join(settings.BASE_DIR, 'backups/') + filename
                f = open(filepath, 'r')
                file = File(f)
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(filepath)
                filename, file_extension = os.path.splitext(filepath)
                files.append(file)
                print(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
                print("last modified: %s" % time.ctime(mtime))
                print("size: %s" % os.path.getsize(filepath))
                f.close()
                if file_extension == '.bz2':
                    objects.append(Backups(
                        backup_file_name=os.path.basename(filepath),
                        backup_file_size=Utils.bytes_2_human_readable(os.path.getsize(filepath)),
                        backup_file_created_at=mtime,
                        backup_file_updated_at=mtime,
                    ))

            table = BackupsTable(objects)

            table.set_auth_permissions(auth_permissions)
            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_SETTINGS,
                    'title': Backups.TITLE,
                    'name': Backups.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'table': table,
                    'index_url': reverse("backup_restore"),
                    'select_single_url': reverse("backup_restore_select_single"),
                    'select_multiple_url': reverse("backup_restore_select_multiple"),
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


@csrf_exempt
# noinspection PyUnusedLocal
def backup_restore_select_single(request):
    if request.is_ajax():
        operator = Operators.login_required(request)
        if operator is None:
            # Operators.set_redirect_field_name(request, request.path)
            # return redirect(reverse("operators_signin"))
            return HttpResponse('signin', content_type='text/plain')
        else:
            auth_permissions = Operators.get_auth_permissions(operator)
            action = request.POST['action']
            id = request.POST['id']
            if action != '' and id is not None:
                if action == 'backup':
                    if settings.ACCESS_PERMISSION_SETTINGS_VIEW in auth_permissions.values():
                        try:
                            call_command('archive')
                            messages.success(request, 'Backup taken successfully.')
                        except(TypeError, ValueError, OverflowError):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'delete':
                    if settings.ACCESS_PERMISSION_SETTINGS_VIEW in auth_permissions.values():
                        print(action + '-' + id)
                        filepath = os.path.join(settings.BASE_DIR, 'backups/') + id
                        print(filepath)
                        if os.path.isfile(filepath):
                            os.remove(filepath)
                        messages.success(request, 'Backup file deleted successfully.')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')

                return HttpResponse('success', content_type='text/plain')
            else:
                return HttpResponseBadRequest('Bad Request', content_type='text/plain')
    else:
        operator = Operators.login_required(request)
        if operator is None:
            Operators.set_redirect_field_name(request, request.path)
            return redirect(reverse("operators_signin"))
        else:
            auth_permissions = Operators.get_auth_permissions(operator)
            action = request.POST['action']
            id = request.POST['id']
            if action != '' and id is not None:
                if action == 'download':
                    if settings.ACCESS_PERMISSION_SETTINGS_VIEW in auth_permissions.values():
                        print(action + '-' + id)
                        filepath = os.path.join(settings.BASE_DIR, 'backups/') + id
                        print(filepath)
                        filename, file_extension = os.path.splitext(filepath)
                        if file_extension == '.bz2' and os.path.exists(filepath):
                            with open(filepath, 'rb') as fh:
                                response = HttpResponse(fh.read(), content_type="application/x-gzip")
                                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filepath)
                                return response
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                return HttpResponse('success', content_type='text/plain')
            else:
                return HttpResponseBadRequest('Bad Request', content_type='text/plain')


@csrf_exempt
# noinspection PyUnusedLocal
def backup_restore_select_multiple(request):
    if request.is_ajax():
        operator = Operators.login_required(request)
        if operator is None:
            # Operators.set_redirect_field_name(request, request.path)
            # return redirect(reverse("operators_signin"))
            return HttpResponse('signin', content_type='text/plain')
        else:
            auth_permissions = Operators.get_auth_permissions(operator)
            action = request.POST['action']
            ids = request.POST['ids']
            try:
                ids = ids.split(",")
            except(TypeError, ValueError, OverflowError):
                ids = None
            if action != '' and ids is not None:
                if action == 'delete':
                    if settings.ACCESS_PERMISSION_SETTINGS_VIEW in auth_permissions.values():
                        for id in ids:
                            try:
                                print(action + ' ' + id)
                            except(TypeError, ValueError, OverflowError):
                                continue
                        messages.success(request, 'Deleted successfully.')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')

                return HttpResponse('success', content_type='text/plain')
            else:
                return HttpResponseBadRequest('Bad Request', content_type='text/plain')
    else:
        return HttpResponseForbidden('Forbidden', content_type='text/plain')
