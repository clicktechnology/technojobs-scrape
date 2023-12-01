# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html



import scrapy
from w3lib.html import remove_tags
from scrapy.loader.processors import Join, MapCompose, Identity, TakeFirst

class JobsjsonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date_scraped = scrapy.Field()
    date_posted = scrapy.Field()
    valid_until = scrapy.Field()
    job_id = scrapy.Field()
    job_title = scrapy.Field()
    job_type = scrapy.Field()
    location = scrapy.Field()
    contact_name = scrapy.Field()
    start_date = scrapy.Field()
    salary_min = scrapy.Field()
    salary_min_int = scrapy.Field()
    salary_max = scrapy.Field()
    salary_max_int = scrapy.Field()
    listed_on = scrapy.Field()
    recruiter = scrapy.Field()
    recruiter_url = scrapy.Field()
    job_reference = scrapy.Field()
    url = scrapy.Field()
    job_description = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Join(),
    )
    job_skills = scrapy.Field()
    addressLocality = scrapy.Field()
    addressRegion = scrapy.Field()
    postalCode = scrapy.Field()
    addressCountry = scrapy.Field()
    search_postcode = scrapy.Field()
    search_radius = scrapy.Field()


    # Housekeeping fields

    spider = scrapy.Field()
