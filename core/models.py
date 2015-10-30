from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def __unicode(self):
        return self.last_name

    
