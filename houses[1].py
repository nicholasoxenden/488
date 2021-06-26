import scrapy


class HousesSpider(scrapy.Spider):
    name = 'houses'
    allowed_domains = ['och.byu.edu']
    start_urls = ['https://och.byu.edu/all-facilities']
    
    def parse(self, response):

        for i in range(0,len(response.xpath("//*[@id='myTable']/tr[*]").extract()),2):
            apt_complex = yield {
                'apt_complexlist':response.xpath("//*[@id='myTable']/tr[" + str(i) + "]//text()").getall()
            }

       
