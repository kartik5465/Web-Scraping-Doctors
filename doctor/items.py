# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DoctorItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    gender = scrapy.Field()
    expertise = scrapy.Field()
    research = scrapy.Field()
    phone = scrapy.Field()
    location = scrapy.Field()
    education = scrapy.Field()
