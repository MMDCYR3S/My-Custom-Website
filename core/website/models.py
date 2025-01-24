from django.db import models

# Contact model
class Contact(models.Model):
    """ Summary:
        This model is used for contact. Gets email from user
        and then save it to the database. 
    """
    email = models.EmailField(max_length=200)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class WorkSamples(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to="work-sample/")
    link = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
