from django.db import models
from django.urls import reverse
# from django.utils.text import slugify
# from django.contrib.auth.models import User

# Create your models here.

class Issue(models.Model):
    issue_num = models.IntegerField(unique=True)
    release_date = models.DateField()
    cover_img_url = models.URLField(null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'issue'
        verbose_name_plural = 'issues'
        ordering = ['-issue_num']

    def __str__(self):
        return f'issue {self.issue_num}'


class Person(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    appears_in = models.ManyToManyField(Issue, related_name='contributors')
    role = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = 'person'
        verbose_name_plural = 'people'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Bio(models.Model):
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    pronouns = models.CharField(max_length=50, blank=True)
    pseudonym = models.CharField(max_length=50, blank=True)
    social_url = models.URLField(null=True)
    person_url = models.URLField(null=True)
    bio_text = models.TextField()
    bio_img_url = models.URLField()

    class Meta:
        db_table = 'bio'
        verbose_name_plural = 'bios'

    def __str__(self):
        return f'{self.person}\'s bio'


class Content(models.Model):
    #Content type choices, for choosing css class:
    POEM = 'poem'
    LONG_FORM = 'long'
    SHORT_FORM = 'short'
    COMIC = 'comic'
    GALLERY = 'gallery'
    SOLO_IMG = 'soloimg'
    ED_NOTE = 'ednote'

    CONTENT_CHOICES = [
        (POEM, 'poem'),
        (LONG_FORM, 'long form'),
        (SHORT_FORM, 'short form'),
        (COMIC, 'comic'),
        (GALLERY, 'image gallery'),
        (SOLO_IMG, 'single image'),
        (ED_NOTE, 'editors note'),
    ]

    title = models.CharField(max_length=250)
    creator = models.ManyToManyField(Person, related_name='contributions')
    issue = models.ForeignKey(Issue, on_delete=models.DO_NOTHING, related_name='contents')
    slug = models.SlugField(max_length=200, unique=True)
    pub_date = models.DateField()
    metades = models.CharField(max_length=300, default="magazine page")
    page = models.IntegerField()
    css_class = models.CharField(max_length=7, choices=CONTENT_CHOICES, default=SHORT_FORM)
    body = models.TextField()

    class Meta:
        db_table = 'content'
        verbose_name_plural = 'contents'
        ordering = ['page']

    def __str__(self):
        return self.title
    
    # Instead of this, override clean method in form
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Content, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('content_detail', kwargs={"slug": self.slug})

    def get_content_class(self):
        return self.css_class

