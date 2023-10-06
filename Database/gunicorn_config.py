bind = "0.0.0.0:8000"
workers = 4

import os

from Database.settings import STATIC_ROOT

from Database.wsgi import application

application = WhiteNoise(application, root=STATIC_ROOT)

STATIC_URL = '/static/'

