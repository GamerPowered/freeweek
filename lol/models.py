from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=200)
    square_url = models.URLField(default="http://img3.wikia.nocookie.net/__cb20120730015737/leagueoflegends/images/9/95/ChampionSquare.png")
    champion_id = models.IntegerField(unique=True, null=True)

    def __unicode__(self):
        return self.name

class FreeWeek(models.Model):
    start = models.DateField()
    end = models.DateField()

    slot1 = models.ForeignKey(Hero, related_name='+')
    slot2 = models.ForeignKey(Hero, related_name='+')
    slot3 = models.ForeignKey(Hero, related_name='+')
    slot4 = models.ForeignKey(Hero, related_name='+')
    slot5 = models.ForeignKey(Hero, related_name='+')
    slot6 = models.ForeignKey(Hero, related_name='+')
    slot7 = models.ForeignKey(Hero, related_name='+')
    slot8 = models.ForeignKey(Hero, related_name='+')
    slot9 = models.ForeignKey(Hero, related_name='+')
    slot10 = models.ForeignKey(Hero, related_name='+')

    def __unicode__(self):
        return '%s - %s' % (self.start, self.end)


