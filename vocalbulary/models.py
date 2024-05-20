"""
model class build
"""
from django.db import models


class Vocalbulary(models.Model):
    """
    a row in database
    """
    ru_word = models.CharField(max_length=50)
    en_word = models.CharField(max_length=50)
    word_type = models.CharField(max_length=20, blank=True)
    example = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        """
        __str__ dunder method
        """
        return '{}-{}'.format(self.ru_word, self.en_word)
