from django.db import models
from django.forms import ModelForm


class Song(models.Model):
    name = models.CharField(max_length = 100)
    lyrics = models.TextField()
    lines = models.IntegerField(blank = True)

    def __str__(self):
        return "%s" % (self.name)

    @classmethod
    def create(cls,name,lyrics):
        song = cls(name,lyrics)
        song.lines = len(song.lyric_list())
        song.save()
        return song

    def lyric_list(self):
        clean = [line for line in self.lyrics.splitlines() if line != ""]
        return clean


class Chat(models.Model):
    chat_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 100)
    lyric_tracker = models.ManyToManyField('Song',
                                           through = 'Tracker')
    players = models.ManyToManyField('Player',
                                     blank = True)

    def __str__(self):
        return "%s" % (self.name)


class Tracker(models.Model):
    chat = models.ForeignKey('Chat',
                             on_delete = models.CASCADE)
    song = models.ForeignKey('Song',
                             on_delete = models.CASCADE)
    line_number = models.IntegerField(default = 1)

    def __str__(self):
        return "Chat: %s \nSong: %s \nAt line: %d" % (self.chat.name,
                                                      self.song.name,
                                                      self.line_number)

    def next_line(self, chat_text):
        text = regex_line(chat_text)
        lyriclist = [regex_line(line) for line in self.song.lyric_list()]

        if self.line_number < self.song.lines and lyriclist[self.line_number-1] in text:
            lyric = lyriclist[self.line_number]
            self.line_number += 2
            return lyric

        for i in range(len(lyriclist)):
            if lyriclist[i] in text:
                self.line_number = i+1
                return lyriclist[i+1]

        return None


class Response(models.Model):
    trigger = models.CharField(max_length = 100)
    response = models.CharField(max_length = 2000)

    def __str__(self):
        return "Trigger: %s \nResponse: %s" % (self.trigger,
                                               self.response)

    def is_meme(self, chat_text):
        text = regex_line(chat_text)
        trig = regex_line(trigger)

        if trig in text:
            return response

        return None


class Player(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200,
                            blank = True)

    def __str__(self):
        return "%s" % (self.name)


def regex_line(string):
    re_string = re.sub('[^A-z\s]', '', string.lower())
    return re_string
