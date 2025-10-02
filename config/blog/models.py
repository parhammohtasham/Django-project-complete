from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# Create your models here.

class PostManger(models.Manager):
    def publisheyear(self,year):
        return self.filter(publish__year=year)
    
class Published(models.Manager):
    def get_queryset(self):
        return super(Published,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published')
    )
    title=models.CharField(_("عنوان"), max_length=50)
    slug=models.SlugField(_("اسلاگ") , unique_for_date="publish")
    author=models.ForeignKey(User, verbose_name=_("نویسنده"),related_name="Post", on_delete=models.CASCADE)
    content=models.TextField(_("متن "))
    publish=models.DateTimeField(_("زمان انتشار"), default=timezone.now)
    created=models.DateTimeField(_("زمان ساخت پست"), auto_now=False, auto_now_add=True)
    status=models.CharField(_("وضعیت انتشار"), max_length=10 , choices=STATUS_CHOICES , default='draft')
    update=models.DateTimeField(_("زمان ویرایش"), auto_now=True, auto_now_add=False)
    objects=models.Manager()
    published=Published()

    class Meta:
        ordering=('-publish',)
        verbose_name='پست'
        verbose_name_plural='پست ها'


    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.pk , self.slug , self.publish.year , self.publish.month , self.publish.day])
    

    def __str__(self):
        return self.title
    