from scrapy import Spider
class ItunesSpider(Spider): #way to extend from spider
    name = 'itunes'
    # start_urls is predifined list to pass more than one address and 'parse' is also predefined
    start_urls = [
        'https://www.bigbasket.com/ps/?q=popular%20food%20items#!page=2'
        

    ]
    def parse(self,response): #response is predefined and parse get executed whenever we run the code and it takes input from starts_url variable
        #select each item for all songs
        songs = response.xpath('//a[@class="ng-binding"]/text()') # to write the class we use '.' notation
        # loop over each song item
        for item in songs:
            # generate a clean dictionary
            yield {
                'title':item# to obtain property such as text is with '::'
                
            # yield manages the returnes 
            }
        #yield is advance return type system
        # that wait for the loop to finish and then
        # give back a list in python
# run on terminal using any one command 
# scrapy runspider itunesspider.py -o out.csv
# scrapy runspider itunesspider.py -o out.json (this is prefferably for those who use html)
# scrapy runspider itunesspider.py -o out.xml

