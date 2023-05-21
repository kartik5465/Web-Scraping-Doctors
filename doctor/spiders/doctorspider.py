import scrapy
from doctor.items import DoctorItem


class DoctorspiderSpider(scrapy.Spider):
    name = "doctorspider"
    allowed_domains = ["www.hopkinsmedicine.org"]
    start_urls = ["https://www.hopkinsmedicine.org/profiles/search?count=100"]


    def parse(self, response):
        doctor = response.css('h2.h4 span.doctor-name::text')
        profile_urls = response.css('div.main-wrap a::attr(href)').getall()

        for profile_url in profile_urls:
            yield response.follow(profile_url, callback=self.parse_profile)

        for i in range(1,31):
            url = f'https://www.hopkinsmedicine.org/profiles/search?query=&page={i}&count=100'
            yield response.follow(url, callback=self.parse)
   
    def parse_profile(self, response):
        #a_research = response.xpath("//p[@class='read-more-wrapper']/text()")
        #research =  a_research.get() + (''.join(response.xpath("//p[@class='read-more-wrapper']/span[@class='read-more-text-hidden']/text()").getall()))
        #location = response.xpath("//div[@class='practice loc-chosen']/h3/text()").get() + response.xpath("//div[@class='address']/text()").get().strip().replace(",\n", "\n")
        research = response.xpath("//p[@class='read-more-wrapper']/text()").getall()
        hidden_text = response.xpath("//p[@class='read-more-wrapper']/span[@class='read-more-text-hidden']/text()").getall()
        research = " ".join(research) + " ".join(hidden_text)
        location = response.xpath("//div[@class='practice loc-chosen']/h3/text() | //div[@class='address']/text()").getall()
        location = " ".join([loc.strip() for loc in location])
        
        doctoritem = DoctorItem() 
        doctoritem['name']= response.css('div.name h1::text').get()
        doctoritem['title']= response.css('ul.titles li::text').get()
        doctoritem['gender']= response.css('div.gender strong::text').get()
        doctoritem['expertise']= response.xpath("//div[@class='expertise']/p/text()").get()
        doctoritem['research']=research
        doctoritem['phone'] = response.css('div.phone ::text').get()
        doctoritem['location'] = location
        doctoritem['education']= response.xpath("//div[@class='restrict']/ul/li/text()").getall()
        
        yield doctoritem
        
      

      
        
#name = response.css('h2.h4 span.doctor-name::text').get()

#name_inside_link = response.css('div.name h1::text').get()

#title_inside_link = response.css('ul.titles li::text').get()

#gender_inside_link = response.css('div.gender strong::text').get()

#'p.read-more-wrapper ::text' ,  span.read-more-text-show ::text'

# number - response.css('div.phone ::text').get()

# address_ to be changed = response.css('div.address ::text').get()

# profile_link = response.css('div.main-wrap a::attr(href)').get()

#Education_all = response.xpath("//div[@class='restrict']/ul/li/text()").getall()

#Title_in_profile = response.xpath("//div[@class='side-column']/ul/li/text()").getall()

#Research_interest_half = response.xpath("//p[@class='read-more-wrapper']/text()").getall()

#a = response.xpath("//div[@class='practice loc-chosen']/h3/text()").get()
#b = response.xpath("//div[@class='address']/text()").get().strip().replace(",\n", "\n")
#c = a + ' ' + b

#expertise =  response.xpath("//div[@class='expertise']/p/text()").get()

#a_research = response.xpath("//p[@class='read-more-wrapper']/text()").get()
#b_research = response.xpath("//p[@class='read-more-wrapper']/span[@class='read-more-text-hidden']/text()")
#b_join =     ''.join(elements.getall())


#
 #def parse(self, response):
 #     doctor = response.css('h2.h4 span.doctor-name::text')
 #     for i in range(1,4):
 #           url = f'https://www.hopkinsmedicine.org/profiles/search?count=10&Page={i}'
 #           profile_url = response.css('div.main-wrap a::attr(href)')
 #           yield response.follow(url, callback=self.parse_profile)


         