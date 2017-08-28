# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MietwohItem(scrapy.Item):
    # define the fields for your item here like:
    Ort = scrapy.Field()
    Erstellungsdatum = scrapy.Field()
    Anzeigennummer = scrapy.Field()
    Zimmer = scrapy.Field()
    Wohnflache_qm = scrapy.Field()
    Etage = scrapy.Field()
    Heizkosten_in_Euro = scrapy.Field()
    Warmmiete_in_Euro = scrapy.Field()
    Kaution_Genossenschaftsanteile_in_Euro = scrapy.Field()
    Wohnungstyp = scrapy.Field()
    Heizungsart = scrapy.Field()
    Verfugbar_ab_Monat = scrapy.Field()
    Verfugbar_ab_Jahr = scrapy.Field()
    Ausstattung = scrapy.Field()
