import scrapy

class DotaSpider(scrapy.Spider):
    name = "broodmother"
    allowed_domains = ["datdota.com"]
    start_urls = [
        "http://www.datdota.com/teams.php"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        links = []
        teams = []
        all_links = response.xpath('//table/tbody/tr/td/a/@href').extract()
        for link in all_links:
            teams.append(link.split('&')[1].split('=')[1])
            links.append("http://www.datdota.com/%s" % (link))
            with open ("teams.txt",'wb') as f:
				f.write(str(teams))

        print teams
