from django.db import models

class Subscription(models.Model):
    email = models.EmailField(unique=True)  # Assuming you want unique email addresses

    def __str__(self):
        return self.email
