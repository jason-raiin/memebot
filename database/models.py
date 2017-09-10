from django.db import models
from django.forms import ModelForm

class Song(models.Model):
    name = models.CharField(max_length = 100)
    lyrics = models.CharField(max_length = 10000)
    lines = models.IntegerField()

    def __str__(self):
        return "%s" % (self.name)

class Chat(models.Model):
    chat_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 100)
    lyric_tracker = models.ManyToManyField('Song',
                                           through = 'Counter')
    players = models.ManyToManyField('Player',
                                     blank = True)

    def __str__(self):
        return "%s" % (self.name)

class Counter(models.Model):
    chat = models.ForeignKey('Chat',
                             on_delete = models.CASCADE)
    song = models.ForeignKey('Song',
                             on_delete = models.CASCADE)
    line_number = models.IntegerField()

    def __str__(self):
        return "Chat: %s \nSong: %s \nAt line: %d" % (self.chat.name,
                                                      self.song.name,
                                                      self.line_number)

class Response(models.Model):
    trigger = models.CharField(max_length = 100)
    response = models.CharField(max_length = 2000)

    def __str__(self):
        return "Trigger: %s \nResponse: %s" % (self.trigger,
                                               self.response)

class Player(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200,
                            blank = True)

    def __str__(self):
        return "%s" % (self.name)
