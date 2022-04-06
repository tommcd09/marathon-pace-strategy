import scrapy


class BostonSpider(scrapy.Spider):
    name = 'boston_spider'

    def start_requests(self):
        yield scrapy.Request(f'https://boston.r.mikatiming.com/2021/?page=1&event=R&event_main_group=runner&num_results=1000&pid=search&pidp=start&search%5Bage_class%5D={self.age}&search%5Bsex%5D={self.sex}&search%5Bnation%5D=%25&search_sort=time_finish_netto')

    def parse(self, response):
        for runner in response.xpath('//*[@id="cbox-main"]/div[2]/ul/li'):
            yield {
                'place_overall': runner.xpath('./div[1]/div/div[1]/text()').get(),
                'place_gender': runner.xpath('./div[1]/div/div[2]/text()').get(),
                'place_division': runner.xpath('./div[1]/div/div[3]/text()').get(),
                'sex': self.sex,
                'age_group': self.age,
                'name': runner.xpath('./div[1]/div/h4/a/text()').get(),
                'bib': runner.xpath('./div[2]/div[1]/div/div[2]/text()').get(),
                'half_split': runner.xpath('./div[2]/div[2]/div/div[1]/text()').get(),
                'finish_net': runner.xpath('./div[2]/div[2]/div/div[2]/text()').get(),
                'finish_gun': runner.xpath('./div[2]/div[2]/div/div[3]/text()').get(),
            }

        next_page = response.xpath('//li[@class="pages-nav-button"][last()]/a').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)