import wikipedia
from celery import task
from .models import Order

@task
title = wikipedia.search("gRPC").title
slug = wikipedia.search("gRPC").links

@task
title = wikipedia.search("RESTfull API").title
slug = wikipedia.search("RESTfull API").links