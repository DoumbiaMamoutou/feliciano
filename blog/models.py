from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField()
    contenu = HTMLField('contenu')
    image = models.ImageField(upload_to='blog/articles')
    category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='category_arcticle')
    author = models.ForeignKey('Author',on_delete=models.CASCADE,related_name='author_article')
    tag = models.ManyToManyField('Tag')
    acceuil = models.BooleanField(default=True,null=True)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return '{} {}'.format(self.titre,self.author)

class Category(models.Model):
    # TODO: Define fields here
    titre = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog/category')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return '{}'.format(self.titre)


class Tag(models.Model):
    # TODO: Define fields here
    titre = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return '{}'.format(self.titre)

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='article_comment')
    image = models.ImageField(upload_to='blog/comment',default='profile/default.png')
    message = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    website = models.URLField(max_length=200)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return '{}'.format(self.name)


class Author(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='auteur')
    image = models.ImageField(upload_to='blog/author')
    description = models.TextField()
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return '{}'.format(self.user)
    