import os
import opbeat_wrapper
import noop

if os.environ.get('OPBEAT_APP_ID', None):
    client = opbeat_wrapper.Client(
        os.environ.get('OPBEAT_ORGANIZATION_ID'),
        os.environ.get('OPBEAT_APP_ID'),
        os.environ.get('OPBEAT_SECRET_TOKEN'),
        os.environ.get('UNIT_NAME'))
else:
    client = noop.Client()
