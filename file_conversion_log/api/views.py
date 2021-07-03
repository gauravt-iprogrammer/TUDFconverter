from rest_framework.response import Response
from rest_framework.decorators import api_view
from file_conversion_log.models import ConversionLog
from file_conversion_log.api.serializers import ConversionLogSerializer


@api_view()
def log_list(request):
    logs = ConversionLog.objects.all()
    serializer = ConversionLogSerializer(logs, many=True)
    return Response(serializer.data)