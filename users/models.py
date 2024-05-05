from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# class CustomUser(AbstractUser):
#     username = models.EmailField(max_length=100)
#     birth_date = models.DateField(null=True, blank=True)
#     phone_number = models.CharField(max_length=13, null=True, blank=True)
#
#     def __str__(self):
#         if self.first_name and self.last_name:
#             return f"{self.first_name} {self.last_name}"
#         return self.username
#
#     class Meta:
#         db_table = 'users'
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'
#         get_latest_by = 'date_joined'
#         ordering = ['date_joined']


class PasswordResets(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'password_resets'
        unique_together = (('user', 'created_at'),)
        index_together = (('user', 'created_at'),)
        verbose_name = 'Password Reset'
        verbose_name_plural = 'Password Resets'

