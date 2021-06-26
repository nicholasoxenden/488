import scrapy


class HousesSpider(scrapy.Spider):
    name = 'houses'
    allowed_domains = ['och.byu.edu']
    start_urls = ['https://och.byu.edu/all-facilities']

    def parse(self, response):
        
        table = response.xpath('//*[@id="myTable"]')

        for i in range(0,len(response.xpath("//*[@id='myTable']/tr[*]").getall()),2):
            apt_complexlist = response.xpath("//*[@id='myTable']/tr[" + str(i) + "]//text()").getall()
            apt_complex = []
            #Attempting to remove the 1st, 3rd, and 5th, element 
            #for i in range(0,len(response.xpath("//*[@id='myTable']/tr[" + str(i) + "]//text()").getall())):
                apt_complex.append(i)
                if ("\r\n"):
                    list.remove
            print(apt_complexlist) 
            

        
