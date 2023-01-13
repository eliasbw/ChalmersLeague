from django.db import models


class Player(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email


class Division(models.Model):
    div_nr = models.IntegerField(default=0, unique=True)

    class Meta:
        ordering = ['div_nr']

    def __str__(self):
        return f"{self.div_nr}"


class Team(models.Model):
    p1 = models.OneToOneField(Player, related_name="first_player", unique=True, on_delete=models.CASCADE, default=-2, null=True)
    p2 = models.OneToOneField(Player, related_name="second_player", unique=True, blank=True, null=True,
                              on_delete=models.CASCADE, default=-1)

    div = models.ForeignKey(Division, on_delete=models.CASCADE, default=-1, null=True)
    points = models.IntegerField(default=0)

    @property
    def name(self):
        name = f"{self.p1.first} {self.p1.last}/{self.p2.first} {self.p2.last}"
        return name

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['div', 'points']
