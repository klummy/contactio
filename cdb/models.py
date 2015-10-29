from django.db import models

# Create your models here.
class Contact(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    slug = models.SlugField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.last_name + self.first_name)

        super(test, self).save(*args, **kwargs)
