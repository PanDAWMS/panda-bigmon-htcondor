from django.db import models


class HTCondorJob(models.Model):
    """
    Required fields are 'id'
    """
    id = models.CharField(max_length=100, primary_key=True)
    factory = models.CharField(max_length=64, blank=True)
    Schedd = models.CharField(max_length=64, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    submitted = models.DateTimeField(editable=False, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, editable=False)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=3, blank=True)

    LastJobStatus = models.IntegerField(blank=True, null=True)
    EnteredCurrentStatus = models.IntegerField(blank=True, null=True)
    GridResource = models.CharField(max_length=255, blank=True)
    Environment = models.CharField(max_length=1024, blank=True)

    GlobalJobId = models.CharField(max_length=100, blank=True, null=True)
    Requirements = models.CharField(max_length=1024, blank=True)
    Cmd = models.CharField(max_length=64, blank=True)
    wmsid = models.CommaSeparatedIntegerField(max_length=1024, blank=True)

#    description = models.CharField(max_length=140, blank=True)
#    stdout = models.CharField(max_length=255, blank=True)
#    stderr = models.CharField(max_length=255, blank=True)
