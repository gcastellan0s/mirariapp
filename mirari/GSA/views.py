# -*- coding: utf-8 -*-
from mirari.mirari.views import *
from .models import *
from .vars import *

import requests

class prices__TemplateView(Generic__TemplateView):
    template_name = "prices.pug"