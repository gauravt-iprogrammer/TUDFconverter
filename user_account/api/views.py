from re import I
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


@api_view(['POST',])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

