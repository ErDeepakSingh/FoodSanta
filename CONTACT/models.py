from django.db import models
# from ACCOUNTS.models import User

class Contact_Post(models.Model):
    name=models.CharField(max_length=150)
    mobile_no=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    message=models.TextField(max_length=500)
    # recieved = models.DateTimeField(auto_now_add=True)
    # author=models.ForeignKey(User)

    def __str__(self):
        return