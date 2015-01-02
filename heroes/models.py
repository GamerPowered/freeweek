from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=200)

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

    def __unicode__(self):
        return '%s - %s' % (self.start, self.end)


