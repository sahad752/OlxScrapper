import scrapy 
import json

class Vegvendors(scrapy.Spider):
    name = "vegVendors"
    start_urls = [
        "https://www.food1.com/vegetable-suppliers/saudi-arabia?page=1",
    ]

    headers = {
    'authority': 'www.food1.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': '_ga=GA1.2.904351118.1645887542; _gid=GA1.2.582788488.1645974735; _gat_gtag_UA_38166649_56=1; _gat_gtag_UA_653818_21=1; XSRF-TOKEN=eyJpdiI6IkMwOTQ4UTBmcER0NTFhV2Z5WHUzdHc9PSIsInZhbHVlIjoiUVJwZldJVUZOOHk0eDhrWllDQU9sOFBHWTZjVE0waG4reXZ0ZWxxR3Uyd3NUNnJCT0dmY0N5K21oOVVRZnlJNDNqNUJlYjUzQ2JRV1NSeHJ0ZURJQklRNm02dk80RmlVTUpMa3k1SU1maTg0aUltK2FKUWRManFUbmVxUkJqazYiLCJtYWMiOiJmZmI1MTU2NjJlNjJkZmJlY2NlZWU5Y2NhNWQyNDA1NThkNGJiOTk1NmU1ODBjY2FiMzcxNzAyZDg5YjRlMGViIiwidGFnIjoiIn0%3D; business1com_frontend_session=eyJpdiI6InpPZzhicGpJY0Vtd01tazB1anRvU2c9PSIsInZhbHVlIjoidzFJazd4OGJYK1N4M2ZGZ3NBYzRlUVpwaXRkRUxWam14RmJtUHBLa3JZYnVmQmlPS0JuS3plRUxEdjJKcHIyWTNRK3YwTGNiT2VKR0ZmM1h1OFJPbkdwdVNFNnNwVGRSZjNDOFk4ZmFDNWtwc0ZjUDJuT2FrVmZiQWtnek44ZXkiLCJtYWMiOiJjNTBmNGQwZTRmYTUxNmZkZjk3Y2QyNzhjNzNmMDlkZjk3N2E2ZDlkMzAxNmEyOTUzYzFjMGViY2E3NDAyNmM3IiwidGFnIjoiIn0%3D',
    }

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], headers=self.headers,callback=self.parse)

    def parse(self, response):


        links = []
        articles = response.xpath("//div[@class='col-xs-12']/section[@class='section-list border-layout']/article")
        for article in articles:
            links.append(article.xpath(".//a/@href").get())
        
        for link in links:
            yield scrapy.Request(link, callback=self.parse_article)

    def parse_article(self, response):
       
        # for address in response.xpath("//div[@class='col-xs-12 col-sm-6 col-md-12']").xpath(".//div[@class='set-collection']")[0].xpath(".//div[@class='collection-value']"):
        #     print( bcolors.OKBLUE + address.get() + bcolors.ENDC)
        #     print("\n")

        data =  {
            'name': response.xpath("//h1/text()").get(),
            'address2':response.xpath("//div[@class='col-xs-12 col-sm-6 col-md-12']").xpath(".//div[@class='set-collection']")[0].xpath(".//div[@class='collection-value']/text()")[1].get(),
            'city/Region':response.xpath("//div[@class='col-xs-12 col-sm-6 col-md-12']").xpath(".//div[@class='set-collection']")[0].xpath(".//div[@class='collection-value']/text()")[3].get(),

            'phone': response.xpath("//div[@class='col-xs-12 col-sm-6 col-md-12']//a/@href").get().replace("tel:",""),
            'email': response.xpath("//div[@class='email']/text()").get(),
            'website': response.xpath("//div[@class='website']/text()").get(),
        }
        # print(data)
        print(bcolors.OKBLUE + json.dumps(data,indent=3) + bcolors.ENDC)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
        
        
        

    
