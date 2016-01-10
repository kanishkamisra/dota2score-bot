import scrapy
import datetime
from tutorial.items import broodmother_item
from scrapy.selector import Selector


today = datetime.date.today()
margin = datetime.timedelta( days = 3 )

class broodmother(scrapy.Spider):
	name = "broodmother"
	allowed_domains = ["datdota.com"]
	start_urls = [
		"http://www.datdota.com/teams.php"
	]
	def parse(self, response):
		# filename = response.url.split("/")[-2] + '.html'
		# with open(filename, 'wb') as f:
		#	  f.write(response.body)
		#i = []
		# for i_ret in response.xpath('//table/tbody/tr/td/a/@href'):
			# item = broodmother_item()
			# item['title'] = i_ret.xpath('a/text()').extract()
			# item['link'] = i_ret.xpath('a/@href').extract()
			# item['desc'] = i_ret.xpath('text()').extract()
			# yield item
		sel = Selector(response)
		links = []
		teams = []
		all_links = sel.xpath('//table/tbody/tr/td/a/@href').extract()
		for link in all_links:
			teams.append(link.split('&')[1].split('=')[1])
			links.append("http://www.datdota.com/%s" % (link))
			with open ("teams.txt",'wb') as f:
				f.write(str(teams))
				
			with open("links.txt", 'wb') as l:
				l.write(str(links))
				
				
		#print teams
		
		#print "Enter the name of a team, with absolutely NO SPELLING MISTAKES!"
		#team_name = raw_input()
		
		#with open('teams.txt', 'r') as inF:
			#for line in inF:
				#if team_name in line:
					#team_score = response.xpath('//th[@aria-label="Score: activate to sort column ascending"]').extract()
					#print "The team score is " + team_score + '.' 
					
				#else:
					#print "Looks like you didn't enter a valid team, try checking the spelling."
			
			#team_score = response.xpath('//th[@aria-label="Score: activate to sort column ascending"]').extract()
		
		
		
		
		
		# for link in response.xpath('//table/tbody/tr/td/a/@href'):
			# url = response.urljoin(link.extract())
			# yield scrapy.Request(url, callback = self.parse_dir_contents)
		# print teams
	
	
	# def parse_dir_contents(self, response):
		# for i_ret in response.xpath('//table/tbody/tr/td/a/@href'):
			# item = broodmother_item()
			# item['team'] = i_ret.xpath('a/text()').extract()
			# item['link'] = i_ret.xpath('a/@href').extract()
			# #item['desc'] = i_ret.xpath('text()').extract()
			# yield item