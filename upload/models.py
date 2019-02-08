from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='cover/')
    pdf = models.FileField(upload_to='pdf/')

    def delete(self, *args, **kwargs):
        self.cover.delete()
        self.pdf.delete()
        super(Book, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title
