from django.db import models


class Join(models.Model):

    email = models.EmailField()
    ref_id = models.CharField(max_length=100, default='ABC', unique=True)
    ip_address = models.CharField(max_length=120, default='ABC')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Joined : " + str(self.email)

    class Meta:
        unique_together = ('email', 'ref_id', )
