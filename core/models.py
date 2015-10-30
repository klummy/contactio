from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, null=True)
    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    info = models.TextField(null=True)

    avatar = models.ImageField(upload_to='contact_avatars/', null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def __unicode(self):
        return self.title
