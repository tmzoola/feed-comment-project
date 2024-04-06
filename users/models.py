from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to="user_photos/",null=True, default='user_photos/applesize.jpeg')
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True)
    friends = models.ManyToManyField('users.User', blank=True)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    is_accepted = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.from_user.username} sent friend request to {self.to_user}"

    class Meta:
        unique_together = ['from_user', 'to_user']




