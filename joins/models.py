from django.db import models


class Join(models.Model):

    email = models.EmailField()
    friend = models.ForeignKey("self", related_name='referral',
                               null=True, blank=True)
    ref_id = models.CharField(max_length=100, default='ABC', unique=True)
    ip_address = models.CharField(max_length=120, default='ABC')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Joined : " + str(self.email)

    class Meta:
        unique_together = ('email', 'ref_id', )


# class JoinFriends(models.Model):
#     email = models.OneToOneField(Join, related_name='sharer')
#     friends = models.ManyToManyField(Join, related_name="Friend",
#                                      null=True, blank=True)
#     emailall = models.ForeignKey(Join, related_name='email_all')
#
#     def __str__(self):
#         print("fiends are", self.friends.all())
#         print(self.emailall)
#         print(self.email)
#         return self.email.email
