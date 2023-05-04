from celery import shared_task

@shared_task
def app_hello():
    print ("This task is not registering")