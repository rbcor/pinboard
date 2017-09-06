from random import choice

from django.db import models
from django.utils import timezone

color_list = ['LightPink',
              'LightGreen',
              'yellow',
              'YellowGreen',
              'AntiqueWhite',
              'Beige',
              'Cornsilk',
              'Azure',
              'LavenderBlush',
              'MistyRose',
              ]

def get_color():
    return choice(color_list)

def get_range():
    return choice(list(range(-3,4)))

def get_font():
    return choice(['BenSenHandwriting', 'Sharifa_03-09-2005'])


class Pin(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tag = models.ManyToManyField('Tag', blank=True)

    style_color = models.CharField(max_length=50, default=get_color, blank=True)
    style_transform_range = models.IntegerField(default=get_range, blank=True)
    style_font = models.CharField(max_length=50, default=get_font, blank=True)

    def get_tags(self):
        return ', '.join([tag.name for tag in self.tag.all() ])

    def __str__(self):
        return self.text[:30]

    class Meta:
        ordering = ['-updated_at','-created_at']


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
