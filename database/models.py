from django.db import models
from django.forms import ModelForm


class Song(models.Model):
    name = models.CharField(max_length = 100)
    lyrics = models.TextField()
    lines = models.IntegerField(blank = True,
                                null = True)

    def __str__(self):
        return "%s" % (self.name)

    @classmethod
    def create(cls,n,l):
        song = cls(name=n,
                   lyrics=l)
        song.lines = int(len(song.lyric_list()))
        song.save()
        return song

    @classmethod
    def get_song(cls, chat_text):
        songs = cls.objects.all()
        text = regex_line(chat_text)

        for song in songs:
            for line in song.lyric_list():
                l = regex_line(line)
                if l in text:
                    return song

        return None

    def lyric_list(self):
        clean = [line.strip() for line in self.lyrics.splitlines() if line.strip() != ""]
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

    @classmethod
    def get_chat(cls,chat):
        try:
            chat = cls.objects.get(chat_id = chat.id)
            player.update(name = get_chat_name(chat))

            return player

        except cls.DoesNotExist:
            chat = cls.objects.create(chat_id = chat.id,
                                      name = get_chat_name(chat))

            return chat

    @staticmethod
    def get_chat_name(chat):
        try:
            return chat.title
        except KeyError:
            try:
                return chat.first_name + chat.last_name
            except KeyError:
                return chat.first_name


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
        lyriclist = self.song.lyric_list()

        if self.line_number < self.song.lines and regex_line(lyriclist[self.line_number-1]) in text:
            lyric = lyriclist[self.line_number]
            self.line_number += 2
            self.save()
            return lyric

        for i in range(len(lyriclist)):
            if regex_line(lyriclist[i]) in text and i+1 < self.song.lines:
                self.line_number = i+3
                self.save()
                return lyriclist[i+1]

        return None

    @classmethod
    def find_tracker(cls,chat,song):
        tracker = Tracker.objects.get_or_create(
            chat = chat,
            song = song
        )

        return tracker


class Response(models.Model):
    trigger = models.CharField(max_length = 100)
    response = models.CharField(max_length = 2000)

    def __str__(self):
        return "Trigger: %s \nResponse: %s" % (self.trigger,
                                               self.response)

    @classmethod
    def get_meme(cls, chat_text):
        memes = cls.objects.all()
        text = regex_line(chat_text)

        for meme in memes:
            if regex_line(meme.trigger) in text:
                return meme.response

        return None


class Player(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)

    def __str__(self):
        return "%s" % (self.name)

    @classmethod
    def get_player(cls, user):
        try:
            player = cls.objects.get(user_id = user.id)
            player.update(name = user.first_name,
                          username = user.username)

            return player

        except cls.DoesNotExist:
            player = cls.objects.create(user_id = user.id,
                                        name = user.first_name,
                                        username = user.username)

            return player


def regex_line(string):
    import re
    re_string = re.sub('[^A-z\s]', '', string.lower())

    return re_string
