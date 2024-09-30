from django.db import models
from django.urls import reverse
from django.conf import settings


# class Author(models.Model):
#     first_name= models.CharField(max_length=255)
#     last_name= models.CharField(max_length=255)

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
    
    



class Book(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    title= models.CharField(max_length=255)
    description= models.TextField()
    author= models.CharField(max_length=255)
    price= models.DecimalField(max_digits=6, decimal_places=2)
    cover= models.ImageField( upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})



class Comment(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    book= models.ForeignKey(Book ,on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True, verbose_name='توصیه میکنم')
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
