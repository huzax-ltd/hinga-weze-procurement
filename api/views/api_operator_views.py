import json

from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from app.models import Operators


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def operator_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Incorrect email address or password.'},
                        status=HTTP_400_BAD_REQUEST, content_type="application/json")

    try:
        operator = Operators.objects.get(operator_username=username)
    except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
        return Response({'error': 'Email Id not found.'},
                        status=HTTP_404_NOT_FOUND, content_type="application/json")

    if not check_password(password, operator.operator_password_hash):
        return Response({'error': 'Incorrect email id or password.'},
                        status=HTTP_400_BAD_REQUEST, content_type="application/json")
    else:
        Operators.login(request, operator)
        token = request.session.get(Operators.HASH_SESSION_KEY, None)
        if token is None:
            return Response({'error': 'Not able to create API Token.'},
                            status=HTTP_400_BAD_REQUEST)
        return Response({'token': token}, status=HTTP_200_OK, content_type="application/json")


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def operators(request):
    api_token = request.META.get('HTTP_AUTHORIZATION')
    session_token = "Bearer " + str(request.session.get(Operators.HASH_SESSION_KEY, None))
    if api_token != session_token:
        return Response({'error': 'Invalid API Token.'},
                        status=HTTP_400_BAD_REQUEST, content_type="application/json")
    else:
        operator = Operators.login_required(request)
    if operator is None:
        return Response({'error': 'Session expired.'},
                        status=HTTP_400_BAD_REQUEST, content_type="application/json")
    else:
        objects = Operators.objects.all()
        data = json.dumps([{
            'username': o.operator_username,
            'type': o.operator_type,
            'name': o.operator_name,
            'gender': o.operator_gender,
            'status': o.operator_status,
        } for o in objects])
        return Response(json.loads(data), status=HTTP_200_OK, content_type="application/json")
