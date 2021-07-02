import scrapy
import numpy as np


class HousesSpider(scrapy.Spider):
    name = 'houses'
    allowed_domains = ['och.byu.edu']
    start_urls = ['https://och.byu.edu/all-facilities']

    def parse(self, response):
        
        table = response.xpath('//*[@id="myTable"]')

        for i in range(2,len(response.xpath("//*[@id='myTable']/tr[*]").getall()),2):
            
            yield {
                # 'complex_list': response.xpath("//*[@id='myTable']/tr[" + str(i) + "]//text()").getall(),
                'complex_name': response.xpath("//*[@id='myTable']/tr[" + str(i) + "]/td[1]//text()").get(),
                'complex_type' : response.xpath("//*[@id='myTable']/tr[" + str(i) + "]/td[2]//text()").get(),
                'complex_address' : response.xpath("//*[@id='myTable']/tr[" + str(i) + "]/td[3]//text()").get(),
                'approximate_units': np.array([1 if (x[0] or x[1]) in '123456789' else 0 for x in response.xpath('//*[@id="myTable"]//tr['+ str(i + 1) +']/td[1]//table[1]//tr[*]/td//text()').getall()]).sum()
                }


