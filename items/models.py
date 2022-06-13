from django.db import models

# Create your models here.


class Item(models.Model):
    type = (('SteamGiftCard', 'SteamGiftCard'),
            ('Game', 'Game'),
            ('CardWoW', 'CardWoW'),
            ('CardRiotPoints', 'CardRiotPoints'),
            ('DotaItem','DotaItem'),
            )
    rarity = (('Legendary', 'Legendary'),
              ('Immortal', 'Immortal'),
              ('Arcana', 'Arcana'),
              ('Rare', 'Rare'),
              ('Common', 'Common'),
              ('Persona', 'Persona'),
              )
    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.IntegerField(blank=False)
    picture = models.ImageField(blank=True, null=True)
    quantity = models.IntegerField(blank=False)
    rarities = models.CharField(max_length=255, choices=rarity)
    type = models.CharField(max_length=255, choices=type)
    hero = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    @property
    def discount_price(self):
        off = (self.price * (10/100))
        return off

    @property
    def ImageURL(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name