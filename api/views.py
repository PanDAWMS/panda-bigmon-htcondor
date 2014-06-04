from api.models import HTCondorJob
from api.serializers import HTCondorJobSerializer
from rest_framework import generics
from rest_framework_bulk import ListCreateBulkUpdateAPIView
from rest_framework import status
from rest_framework.response import Response

from pprint import pprint

class JobList(ListCreateBulkUpdateAPIView):
    queryset = HTCondorJob.objects.all()
    serializer_class = HTCondorJobSerializer
    
    def pre_save(self, obj):
        pprint(vars(obj))

    def delete(self, request, *args, **kwargs):
        """Accept htcondor-remove DELETE method but do nothing"""
        return Response(status=status.HTTP_204_NO_CONTENT)

class JobDetail(generics.RetrieveAPIView):
    queryset = HTCondorJob.objects.all()
    serializer_class = HTCondorJobSerializer

