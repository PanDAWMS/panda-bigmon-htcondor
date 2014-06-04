from rest_framework import serializers
from api.models import HTCondorJob


class HTCondorJobSerializer(serializers.ModelSerializer):
#    st = serializers.WritableField(write_only=True, source='state', default='', required=False)
#    test = serializers.CharField(source='schedd', read_only=True)

    class Meta:
        model = HTCondorJob

#    def transform_test(self, obj, value):
#        return 'foo'

#    def validate(self, attrs):
#        """
#        Check for valid state transitions, must return attrs
#        or serializers.ValidationError
#        """
#        print 'PALisvalid', self.is_valid()
#        print 'PALerrors', self.errors
#        if 'wmsid' in attrs:
#            print 'PALwmsid', attrs['wmsid']
#        return attrs

    def __init__(self, *args, **kwargs):
        self.many = kwargs.pop('many', True)
        self.partial = kwargs.pop('partial', True)
        super(HTCondorJobSerializer, self).__init__(*args, **kwargs)

## no longer need this since we moved to 'id' as the PK. 
#    def get_identity(self, data):
#        """
#        This hook is required for bulk update.
#        We need to override the default, to use the globaljobid as the identity.
#
#        Note that the data has not yet been validated at this point,
#        so we need to deal gracefully with incorrect datatypes.
#        """
#        try:
#            return data.get('globaljobid', None)
#        except AttributeError:
#            return None
