
from ast import keyword
from curses import meta
from statistics import median
import scrapy
import requests
import json

class olx(scrapy.Spider):
    name = "olx"
    start_urls = ["https://www.olx.in/mundikkal-thazham_g1000000000001428/q-ritz-2014?isSearchCall=true","https://www.olx.in/api/relevance/v2/search"]
    headers = {
    'authority': 'www.olx.in',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'accept': '*/*',
    'x-newrelic-id': 'VQMGU1ZVDxABU1lbBgMDUlI=',
    'sec-ch-ua-mobile': '?0',
    'x-panamera-fingerprint': '1b960633420024cc7b78f17821f3d734#1630392857162',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.olx.in/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'laquesis=pan-48200@a#pan-55076@b#pan-59446@b#pan-60601@b; laquesisff=pan-36788#pan-38000#pan-42665; _ga=GA1.2.348854798.1643714481; WZRK_G=7e5180886bc8448e97843dbdb6123df5; _gcl_au=1.1.15300131.1643714481; _fbp=fb.1.1643714481041.1006327212; ldTd=true; _gid=GA1.2.1700952412.1645202668; laquesissu=70@none|0#87@booking_location_exit|0; locationPath=%5B%7B%22id%22%3A1000000000001428%2C%22name%22%3A%22Mundikkal%20Thazham%22%2C%22type%22%3A%22NEIGHBOURHOOD%22%2C%22longitude%22%3A75.868871%2C%22latitude%22%3A11.2885213%2C%22parentId%22%3A4058877%7D%5D; _hjid=cd797b64-c2c0-44ce-ba60-96ba7aa90380; _hjSessionUser_1193424=eyJpZCI6IjRlYWNkN2RjLTc1ZjAtNTI0OS04ZjFmLWQxNDBiODk4MDNkNiIsImNyZWF0ZWQiOjE2NDUyMDI3ODg3MzQsImV4aXN0aW5nIjp0cnVlfQ==; _abck=F750280B3346162590B6D3FE849E5ED0~0~YAAQ3VI2F5u+Btp+AQAAOaaMEQfvAdvZKCAtiP5bDuQc1x8JTVN1b3RuxFdU6kJN72adA8zO+/lbJXhbev+C56meGGdA5VdGBVac+ZQee5De0rx5U+7+VtX5bdAZ5fDzYEeAZ1wYGGFgblww4Ql2O31w+pWBBs1J8LmFOge7BmrwxbN7xGa2ZNTfwadruOWmjsFsqUU2H8AU/0rkQcsD1UIe09+0t1gHmunOX770qee6T4YKaQG6b8QHraRKbvcjgvfvr0OB9gcMEuEcRw42w7dbge73U7qdP7VM6yt8/8mi/epihc3/kGkI5COJXP8ZaybXrry4fgJkKSCTeZmpEVoIdMRRQZd9ls0MfBB6NTWc9bZjzJqL0DgauVJNquRuvCp97nLCjN6sZN9tNVEXw3mghSc=~-1~-1~-1; bm_sz=805BDC96BEC394B7A9B7A817D60E3AA0~YAAQ3VI2F52+Btp+AQAAOaaMEQ5HD3QkuzC+VoDag5BCPgb09pPDIPN6YOj41KQ6IzMV7C9w2sz6XzOzvcoNOjAc9R9Vr61wyW5n/B/goLK5H41fJ6GGY5Casb8Mll4k006FfJmbJUW60MVZrDKfxxOQnj7ZyDmFCiVMYLPfMfA1CiTBSGgeEV2ZgaRbZwINyGz91ZeSF6OXXuL5xo6Xl5mkFaBfZribKtfjEZDsOWj0iIUBV9srd6gjMMuED1wlSB+4MchOefg9s3YJgLRW+EAwiYlkis110G+6golH+w==~3621170~4470595; bm_mi=AC908D5FECF9276C56CFB4E346A9F94B~O7eIkosFNtM+zxFYHf9CFroRYUXhNm+iIlmajlo6mp69cQ72hwFPIvh4mk6L19QsO1Unj3Pko2RqdsaRpVQrN+CPM3Hr4vLeiP/wKT2LTLoEIGA3GR3C9evCVpZecKSHqZzUSX+Egtvu4a8lzTO4ILEGPELdr4LsXUQ2GwivVResOpnxAga+SnuD0tqqXfbVhW5MLJ8jqum4XVP8Ar68IT818HLHpuAH3G8xUe0KqcEIT3B5NR5USpy+zq2jxsYcD+bwm9vCrtsXnawnt6xDNw==; _gat_clientNinja=1; lqstatus=1645268106|17f0db877b8x28fbb0f2|pan-60601||; AMP_TOKEN=%24NOT_FOUND; _gat_UA-88236416-1=1; __gads=ID=c5655b410cc07f8c:T=1643714481:S=ALNI_MZvWzWIM41Z_bJZOwnu5UWGwA8eMg; cto_bundle=YlbMal9yT2pQNDdYaFdVdnplV045JTJGV2Vqa3ZRVDM1dVBKWHRFVWRDYzlWSiUyQlR4R20lMkJLa0R6blN6Ulk5S1RGUVJKem96TDRGNmtHNG5XSkhVOGhDek03NU12aFhYWWtId0slMkJ6S1ZFVTBIbkZYako5ZGVNRmhhV2J5dldvZ3VWJTJGYmZVWk5mbzB4Ynl2NWI2b1luWG45SnNKWWR3JTNEJTNE; ak_bmsc=0012B9E160693138EDCEF4ABBD2ADADD~000000000000000000000000000000~YAAQ3VI2F7S/Btp+AQAA9LCMEQ59bfqk3+yAqrkMjXpEHEkfPKHYVUYaohlIPAKLK5pPCvHDe7DN7aYnqilkyE97zjjPfk4XZ3z512Wb5Jy9wGc3sEHeB0d/dEPeo46sslZqSTv29hAcCgfDU8X3AyfHJ6zboLx+4iJzN2mGjlfVJRRGFLgBZPgxt4Utw4PE4u2ijrtMpqM2qKp4WnehjmfV0juH45NaIc/YsFpMF8sbd0MLyfprVO6PtT+O5eE5GeNznXnS40d5S0gLy7DNuh7jNruOLlGgVjHK9w9ESKdCwAg8TX1jBHl5Eg+hKlXDOCD5f19msNfwsqCwCkuXbAt2SmP+2p0i7D2DsvkBuZnNEgWwE8cgkRKGuNvK8SJ2eclC0gmeac72C5a2vXRF41Smbl8KtuOq6rvjQsAHZlJSoqdTqJgVIVLrp+kQQlD+moXR40JnxkWhmJIQngy2swQsobI4xSzhTF7L+MPJL1+SHmF7tAQW9tursOyeGsVA; g_state={"i_p":1645274109195,"i_l":1}; WZRK_S_848-646-995Z=%7B%22p%22%3A1%2C%22s%22%3A1645266906%2C%22t%22%3A1645266921%7D; onap=17eb5047fecx39fb31ff-3-17f118cac16x21376ebc-19-1645268722; bm_sv=9E2899DF8246AC7CC18A80D0E8F35C07~rusTYl32PLLNSk4zg2qrq9KA6C50opgYKzu5ruesJKxSJ12FGmdCYd8mfR6xs5jtnE6Qsrr29VlMscC+FUx0xYA3TuO1J1fPeIZ0NE/MIG3Sb+WFslSwZ1dzGiYtXTRqTgXLlZcUOiJMDzDMBG5tEQ6WS6fDwAwAdUohIqZWee0=',
    }
    keywords = []
    item_url  = 'https://www.olx.in/item/'
    item_api = 'https://www.olx.in/api/bxp/v3/items/{}'

    params =lambda self,a: (
        ('facet_limit', '400'),
        ('location', '1000000000001428'),
        ('location_facet_limit', '40'),
        ('platform', 'web-desktop'),
        ('query', a),
        ('spellcheck', 'true'),
        ('user', '17eb5047fecx39fb31ff'),
        ('lang', 'en-IN'),
    )

    params2 =lambda self,a,b: (
        ('facet_limit', '400'),
        ('location', '1000000000001428'),
        ('location_facet_limit', '40'),
        ('platform', 'web-desktop'),
        ('query', a),
        ('page', b),
        ('spellcheck', 'true'),
        ('user', '17eb5047fecx39fb31ff'),
        ('lang', 'en-IN'),
    )
    my_array = []

    def __init__(self, name=None, **kwargs):
        self.keywords = ['ford ecosport 2015']
        super().__init__(name, **kwargs)

    def start_requests(self):
        for keyword in self.keywords:
            params  = self.params(keyword)
            meta = {'keyword': keyword,
                'page': 0,
            }
            yield scrapy.FormRequest(self.start_urls[1], callback=self.parse,method='GET',formdata=params, headers=self.headers,dont_filter=True,meta = meta)

    def parse(self, response, **kwargs):
        jsonresponse = json.loads(response.text)
        for i in jsonresponse['data']:
            my = {
                'id': i['id'],
                'price': i['price']['value']['raw'],
                'url': self.item_url + i['id'],
                'info': i['main_info'],
            }
            self.my_array.append(my)
        
        if jsonresponse['metadata']['total_ads'] >20:
            response.meta['page'] += 1
        
        if response.meta['page']<3 and jsonresponse['metadata']['total_ads'] >20:
            params = self.params2(response.meta['keyword'] , str(response.meta['page']))
            yield scrapy.FormRequest(self.start_urls[1], callback=self.parse,method='GET',formdata=params, headers=self.headers,dont_filter=True,meta = response.meta)
        else:
            price_average = 0
            for i in self.my_array:
                price_average += int(i['price'])
            price_average = price_average/len(self.my_array)
            price_median = median([i['price'] for i in self.my_array])

            self.my_array.sort(key=lambda x: int(x['price']))
            print(price_average)
            print(price_median)

        print(response.url)