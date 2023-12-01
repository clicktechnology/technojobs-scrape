# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.http import Request
from urllib.parse import urljoin
from scrapy.loader import ItemLoader, Selector
from jobsjson.items import JobsjsonItem
from extruct.jsonld import JsonLdExtractor
import re

class JobsjsonldSpider(scrapy.Spider):
    name = 'jobsjsonld'
    # Some search parameters for the initial query..

    search_postcode = 'W4 2LP'    # BBC Broadcasting House, Central London.  The search radius starts here.
    search_radius = 3              # 1 mile search radius

    #search_postcode = search_postcode.replace(" ", "+")
    allowed_domains = ['technojobs.co.uk']
    start_urls = [('https://www.technojobs.co.uk/search.phtml?page=1&row_offset=10&sortby=5&keywords=any&salary=0&jobtype=all&postedwithin=all&location={}&radius={}').format(search_postcode, search_radius)]

    def parse(self, response):
        # Pick out each page of the typically 8 or 9 pages of jobs.
        job_pages = response.xpath('//div[@id="content"]/div[@class="pagination"]/div[@class="content"]/a/@href')
        # Now iterate the pages in turn and extract them..
        for job_page_url in job_pages.extract():
            yield Request(urljoin(response.url, job_page_url))

        # Now pick the individual job page advert
        job_selector = response.xpath('//a[@href][@class="view-job-button"]/@href')
        # Now iterate each individual job page and extract them..
        for job in job_selector.extract():
            yield Request(urljoin(response.url, job), callback=self.parse_job)

    def parse_job(self, response):
        # Create the loader using the response
        # E.G. : l.add_xpath('item', '*xpath*', re='*expression*')
        jslde = JsonLdExtractor()
        data = jslde.extract(response.text)
        data = data[0]

        l = ItemLoader(item=JobsjsonItem(), response=response)
        l.add_value('search_postcode', self.search_postcode)
        l.add_value('search_radius', self.search_radius)
        l.add_value('date_scraped', time.strftime("%Y-%m-%d %H:%M:%S"))
        l.add_value('date_posted', data['datePosted'])
        l.add_value('valid_until', data['validThrough'])
        l.add_value('job_id', response.url, re='\d{7}')
        l.add_value('job_title', data['title'])
        l.add_value('job_type', data['employmentType'])
        l.add_value('location', ",".join([  data['jobLocation']['address']['addressLocality'], data['jobLocation']['address']['addressRegion'], data['jobLocation']['address']['postalCode'], data['jobLocation']['address']['addressCountry']]))
        l.add_xpath('contact_name', '//table[@class="job-listing-table"]//tr[8]//td//text()')
        l.add_xpath('start_date', '//table[@class="job-listing-table"]//tr[6]//td//text()')
        try:
            l.add_value('salary_min', data['baseSalary']['value']['value'])
        except:
            l.add_value('salary_min', 'NA')
        l.add_value('listed_on', data['datePosted'])
        l.add_value('recruiter', data['hiringOrganization']['name'])
        l.add_value('recruiter_url', data['hiringOrganization']['sameAs'])
        try:
            l.add_value('job_reference', data['identifier']['value'])
        except:
            l.add_value('job_reference', 'NA')
        l.add_value('url', response.url)
        l.add_value('job_description', data['description'])
        l.add_value('job_skills', data['skills'])
        l.add_value('addressLocality', data['jobLocation']['address']['addressLocality'])
        l.add_value('addressRegion', data['jobLocation']['address']['addressRegion'])
        l.add_value('postalCode', data['jobLocation']['address']['postalCode'])
        l.add_value('addressCountry', data['jobLocation']['address']['addressCountry'])
        return l.load_item()