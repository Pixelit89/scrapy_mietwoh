# -*- coding: utf-8 -*-


from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import MietwohItem
class MietSpider(CrawlSpider):
    name = "miet"
    allowed_domains = ["ebay-kleinanzeigen.de"]
    start_urls = ["https://www.ebay-kleinanzeigen.de/s-wohnung-mieten/c203"]
    rules = [
        Rule(LinkExtractor(allow="s-anzeige/"), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow="/s-wohnung-mieten/seite:\d+/c203"), follow=True)
    ]

    def parse_item(self, response):
        item = MietwohItem()
        try:
            pre = response.xpath('//dt[contains(.,"Ort")]/following::dd/span/span/text()').extract()
            striped = [elem.strip() for elem in pre]
            item['Ort'] = ' '.join(striped).encode('utf-8')
        except AttributeError:
            pass
        try:
            item['Erstellungsdatum'] = response.xpath('//dt[contains(.,"Erstellungsdatum")]/following::dd/text()').extract_first().strip()
        except AttributeError:
            pass
        try:
            item['Anzeigennummer'] = response.xpath('//dt[contains(.,"Anzeigennummer")]/following::dd/text()').extract_first().strip()
        except AttributeError:
            pass
        try:
            item['Zimmer'] = response.xpath('//dt[contains(.,"Wohnfl")]/following::dd/span/text()').extract_first().strip()
        except AttributeError:
            pass
        try:
            item['Wohnflache_qm'] = response.xpath('//dt[contains(.,"Wohnfl")]/following::dd/span/text()').extract_first().strip()
        except AttributeError:
            pass
        try:
            item['Etage'] = response.xpath('//dt[contains(.,"Etage")]/following::dd/span/text()').extract_first().strip()
        except AttributeError:
            pass
        try:
            item['Heizkosten_in_Euro'] = response.xpath('//dt[contains(.,"Heizkosten")]/following::dd/span/text()').extract_first().strip()
        except AttributeError:
            pass
        try:
            item['Warmmiete_in_Euro'] = response.xpath('//dt[contains(.,"Warmmiete")]/following::dd/span/text()').extract_first().strip()
        except AttributeError:
            pass
        try:
            item['Kaution_Genossenschaftsanteile_in_Euro'] = response.xpath('//dt[contains(.,"Kaution")]/following::dd/span/text()').extract_first().strip()
        except AttributeError:
            pass
        try:
            raw = response.xpath('//dt[contains(.,"Wohnungstyp")]/following::dd/span/a/text()').extract_first().strip()
            item['Wohnungstyp'] = raw.encode('utf-8')
        except AttributeError:
            pass
        try:
            raw = response.xpath('//dt[contains(.,"Heizungsart")]/following::dd/span/text()').extract_first().strip()
            item['Heizungsart'] = raw.encode('utf-8')
        except AttributeError:
            pass
        try:
            item['Verfugbar_ab_Monat'] = response.xpath('//dt[contains(.,"Monat")]/following::dd/span/text()').extract_first().strip()
        except AttributeError:
            pass
        try:
            item['Verfugbar_ab_Jahr'] = response.xpath('//dt[contains(.,"Jahr")]/following::dd/span/text()').extract_first().strip()
        except AttributeError:
            pass
        try:
            pre = response.xpath(u'//dt[contains(.,"Ausstattung")]/following::dd/a/text()'.encode('utf-8')).extract()
            striped = [elem.strip() for elem in pre]
            item['Ausstattung'] = ' '.join(striped).encode('utf-8')
        except AttributeError:
            pass
        return item