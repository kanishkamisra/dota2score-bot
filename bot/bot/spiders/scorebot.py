import scrapy
import sys

team_link = ""
team_q = ""
print "Please enter a team name, with ABSOLUTELY NO SPELLING MISTAKES!"
team_name = raw_input('>')
#team_name = team_name.split('\'')[0]


# with open ("teams.txt",'r') as inT:
	# for line in inT:
		# if(team_name in line):
with open ("links.txt", 'r') as inL:
	for line_l in inL:
		if team_name in line_l:
			#team_link = line.split('=')[2]
			team_q = str((line_l.split('=')[1]).split('&')[0])
			break
		else:
			print "Please enter a valid team name. Check for any spelling mistakes, you noob."
			sys.exit(0)
	
link = "www.datdota.com/team.php?q="+team_q+"&team="+team_name
	
class scoreBot(scrapy.Spider):
	name = "scoreBot"
	allowed_domains = ["datdota.com/teams.php"]
	start_url = [link]
	print team_q
	print "Parsing this page" + str(start_url)
	def parse(self, response):
		all_scores = response.xpath('//table/th[@aria-label="Score: activate to sort column ascending"]').extract()
		
		for score in all_scores:
			with open("scores.txt",'wb') as s:
				s.write(str(score))
				break
		print "The latest score of " + team_name + "was" + score		
				
				