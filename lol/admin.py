from django.contrib import admin
from lol.models import FreeWeek, Hero
from freeweek import settings
from urllib2 import urlopen
import json

class HeroAdmin(admin.ModelAdmin):
    actions = ['regen_api']

    def regen_api(self, request, queryset):

        api_base_url = "https://global.api.pvp.net/api/lol/static-data/euw/v1.2"

        for hero in queryset:
            if hero.champion_id:
                hero_api_url = "%s/champion/%s?champData=image&api_key=%s" % ( api_base_url, hero.champion_id, settings.RIOT_API_KEY )

                hero_up = urlopen(hero_api_url)

                hero_data = json.loads(hero_up.read())

                img_url = "http://ddragon.leagueoflegends.com/cdn/img/champion/loading/%s_0.jpg" % hero_data['key']

                hero.square_url = img_url
                hero.name = hero_data['name']

                hero.save()


    regen_api.short_description = "Regenerate from API"

admin.site.register(Hero, HeroAdmin)
admin.site.register(FreeWeek)