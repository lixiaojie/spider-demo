import scrapy
from movie.items import MovieItem

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = (
        'http://movie.douban.com/top250',
    )
    url = 'http://movie.douban.com/top250'

    def parse(self, response):
        item = MovieItem()
        Movies = response.xpath('//div[@class="item"]')
        for eachMovie in Movies:
            movieTitle = eachMovie.xpath('div[@class="pic"]/a/img/@alt').extract()[0].encode('utf-8')
            link = eachMovie.xpath('div[@class="pic"]/a/@href').extract()
            nameList = eachMovie.xpath('div[@class="info"]/div[@class="hd"]/a/span/text()').extract()
            alterName =''
            for each in nameList:
                alterName += each
            playable = eachMovie.xpath('div[@class="info"]/div[@class="hd"]/span[@class="playable"]/text()').extract()
            if playable:
                playable = playable[0]
            else:
                playable = ''
            desc = eachMovie.xpath('div[@class="info"]/div[@class="bd"]/p/text()').extract()
            star = eachMovie.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/em/text()').extract()[0]
            starNum = eachMovie.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/text()').extract()
            quote = eachMovie.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()').extract()
            if quote:
                quote = quote[0]
            else:
                quote = ''

            # movieTitle = movieTitle[0].encode('utf-8')
            # desc = desc[0].encode('utf-8')
            # starNum = starNum[0].encode('utf-8')
            # quote = quote[0].encode('utf-8')


            item['movieTitle'] = movieTitle
            item['link'] = link
            item['alterName'] = alterName
            item['playable'] = playable
            item['desc'] = desc
            item['star'] = star
            item['starNum'] = starNum
            item['quote'] = quote
            yield item

        nextLink = response.xpath('//div[@class="paginator"]/span[@class="next"]/link/@href').extract()
        if nextLink:
            nextLink = nextLink[0]
            print nextLink
            yield scrapy.Request(self.url + nextLink, callback = self.parse)
