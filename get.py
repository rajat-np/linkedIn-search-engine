import requests,csv,time
from bs4 import BeautifulSoup

def get_result(query):

	num_query = query.count('+')

	query = query.replace(' ','+')

	url = "https://www.google.co.in/search?q=site:linkedin.com/pub+%7C+site:linkedin.com/in+"+query

	links = list()

	page = requests.get(url)

	soup = BeautifulSoup(page.content, "html.parser")

	a = soup.find_all("div", attrs={'class': 'f slp'})

	b = soup.find_all("h3", attrs={'class': 'r'})

	c = soup.find_all('a', attrs={'class': 'fl'})

	for i in c:
		links.append(i['href'])



	with open('temp.csv', 'w') as csvfile:
		spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)


	for i in range(len(b)):
		try:
			temp_desc=a[i].text
		except:
			continue
		num = temp_desc.count('-')
		if num>1:
			name = ((str(b[i].text).split('|'))[0]).strip()
			details = str(a[i].text).split('-')
			location = details[0].strip().replace(","," ")
			title = details[1].strip().replace(","," ")
			company = details[2].strip().replace(","," ")
			try:
				with open('temp.csv', 'a') as csvfile:
					spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
					spamwriter.writerow([name, location, title, company])
			except:
				pass

	for j in links:
		time.sleep(1)

		page = requests.get("https://www.google.co.in"+j)

		soup = BeautifulSoup(page.content, "html.parser")

		a = soup.find_all("div", attrs={'class': 'f slp'})

		b = soup.find_all("h3", attrs={'class': 'r'})

		for i in range(len(b)):
			try:
				temp_desc=a[i].text
			except:
				continue
			num = temp_desc.count('-')
			if num>1:
				name = ((str(b[i].text).split('|'))[0]).strip()
				details = str(a[i].text).split('-')
				location = details[0].strip().replace(","," ")
				title = details[1].strip().replace(","," ")
				company = details[2].strip().replace(","," ")
				try:
					with open('temp.csv', 'a') as csvfile:
						spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
						spamwriter.writerow([name, location, title, company])
				except:
					pass




if __name__ == "__main__":
	pass