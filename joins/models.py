from django.db import models


class Join(models.Model):

    email = models.EmailField()
    name = models.CharField(max_length=20, default="Your Name?")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Joined : " + str(self.email)
