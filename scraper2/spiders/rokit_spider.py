import scrapy
from scrapy.selector import Selector
from scraper2.items import RokitItem
import hashlib

class RokitSpider(scrapy.Spider):
    name = "rokit_spider"

    # The main start function which initializes the scraping URLs and triggers parse function
    def start_requests(self):
        urls = [
            'http://www.rokit.co.uk/vintage-mens/clothing/dungarees-and-overalls',
            'http://www.rokit.co.uk/vintage-mens/clothing/jackets-and-coats',
            'http://www.rokit.co.uk/vintage-mens/clothing/jeans-and-trousers',
            # 'http://www.rokit.co.uk/vintage-mens/clothing/jumpers-and-cardigans-and-knitwear',
            # 'http://www.rokit.co.uk/vintage-mens/clothing/poloshirts',
            # 'http://www.rokit.co.uk/vintage-mens/clothing/shirts',
            # 'http://www.rokit.co.uk/vintage-mens/clothing/shorts-and-trunks',
            # 'http://www.rokit.co.uk/vintage-mens/clothing/suits-and-suiting',
            # 'http://www.rokit.co.uk/vintage-mens/clothing/sweatshirts-and-hoodies',
            # 'http://www.rokit.co.uk/vintage-mens/clothing/t-shirts-and-vests',
            # 'http://www.rokit.co.uk/vintage-mens/clothing/waistcoats-and-gilets-and-tanks',
            # 'http://www.rokit.co.uk/vintage-mens/bags-and-accessories',
            # 'http://www.rokit.co.uk/vintage-mens/bags-and-accessories/bags-and-wallets-sportsbag-holdall-backpack-briefcase-satchel',
            # 'http://www.rokit.co.uk/vintage-mens/bags-and-accessories/-belts',
            # 'http://www.rokit.co.uk/vintage-mens/bags-and-accessories/braces',
            # 'http://www.rokit.co.uk/vintage-mens/bags-and-accessories/gloves-and-mittens',
            # 'http://www.rokit.co.uk/vintage-mens/bags-and-accessories/hats-and-beanies-and-biley-of-hollywood-and-porkpie-and-trilby-and-baseball',
            # 'http://www.rokit.co.uk/vintage-mens/bags-and-accessories/jewellery-and-rings-and-cufflinks-and-tiepins-and-badges',
            # 'http://www.rokit.co.uk/vintage-mens/bags-and-accessories/scarves-and-dinner-scarves-and-cravats',
            # 'http://www.rokit.co.uk/vintage-mens/bags-and-accessories/sunglasses-and-glasses-and-designer-sunglasses',
            # 'http://www.rokit.co.uk/vintage-mens/bags-and-accessories/ties-and-bowties-and-boloties',
            # 'http://www.rokit.co.uk/vintage-mens/shoes-and-boots-and-trainers',
            # 'http://www.rokit.co.uk/vintage-mens/-rokit-recycled-handmade-ethical-fashion-clothing-and-bags-and-accessories-1',
            # 'http://www.rokit.co.uk/vintage-mens/festival-mens',
            # 'http://www.rokit.co.uk/vintage-mens/vintage-military',
            # 'http://www.rokit.co.uk/vintage-mens/denim-and-workwear',
            # 'http://www.rokit.co.uk/vintage-mens/partywear-shirts-ties-bow-ties-tuxedos-blazers-jackets-shoes-braces-waistcoats-christmas-party',
            # 'http://www.rokit.co.uk/vintage-mens/classic-vintage-rare-and-collectible',
            # 'http://www.rokit.co.uk/vintage-mens/category-mens-street-brands',
            # 'http://www.rokit.co.uk/vintage-mens/designer-brands-clothing-and-accessories',
            # 'http://www.rokit.co.uk/vintage-mens/-90s-clothing-nineties-1990s-classic-vintage-collection',
            # 'http://www.rokit.co.uk/vintage-mens/-80s-clothing-eighties-1980s-classic-vintage-collection',
            # 'http://www.rokit.co.uk/vintage-mens/-70s-clothing-seventies-1970s-classic-vintage-collection',
            # 'http://www.rokit.co.uk/vintage-mens/-60s-clothing-sixties-1960s-classic-vintage-collection',
            # 'http://www.rokit.co.uk/vintage-mens/-50s-clothing-fifties-1950s-classic-vintage-collection',
            # 'http://www.rokit.co.uk/vintage-mens/-40s-clothing-forties-1940s-classic-vintage-collection',
            # 'http://www.rokit.co.uk/vintage-mens/mens-ski-snow',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/dresses',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/dungarees',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/-jackets-and-coats',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/jeans',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/-jumpers-and-cardigans-and-knitwear',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/lingerie-and-nightwear-and-kimonos-and-dressinggowns',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/playsuits-and-jumpsuits-and-onesies',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/shorts-and-culottes',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/skirts',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/wedding-dress-shop-bridal-gowns-bridesmaids-dresses-wedding-guests-outfits',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/suits',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/-sweatshirts-and-hoodies',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/swimwear-and-bikinis-and-swimsuits',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/tshirts-and-vests',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/tops-and-blouses-and-shirts',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/trousers',
            # 'http://www.rokit.co.uk/vintage-womens/-clothing/-waistcoats-and-gilets-and-tanks',
            # 'http://www.rokit.co.uk/vintage-womens/womens-bags-and-accessories',
            # 'http://www.rokit.co.uk/vintage-womens/womens-bags-and-accessories/bags-and-purses-shoppers-totes-handbags-holdalls-backpacks-clutches',
            # 'http://www.rokit.co.uk/vintage-womens/womens-bags-and-accessories/belts',
            # 'http://www.rokit.co.uk/vintage-womens/womens-bags-and-accessories/-gloves-and-mittens',
            # 'http://www.rokit.co.uk/vintage-womens/womens-bags-and-accessories/hats-and-beanies',
            # 'http://www.rokit.co.uk/vintage-womens/womens-bags-and-accessories/jewellery-and-necklaces-rings-and-bracelets-and-brooches-and-badges',
            # 'http://www.rokit.co.uk/vintage-womens/womens-bags-and-accessories/silk-scarves-and-knitted-scarves',
            # 'http://www.rokit.co.uk/vintage-womens/womens-bags-and-accessories/-sunglasses-and-glasses-and-designer-sunglasses',
            # 'http://www.rokit.co.uk/vintage-womens/womens-shoes-and-boots-and-trainers',
            # 'http://www.rokit.co.uk/vintage-womens/rokit-recycled-handmade-ethical-fashion-clothing-and-bags-and-accessories',
            # 'http://www.rokit.co.uk/vintage-womens/festival-womens',
            # 'http://www.rokit.co.uk/vintage-womens/womens-denim-collection',
            # 'http://www.rokit.co.uk/vintage-womens/party-tops-sequins',
            # 'http://www.rokit.co.uk/vintage-womens/womens-classic-vintage-rare-and-collectible',
            # 'http://www.rokit.co.uk/vintage-womens/category-womens-street-brands',
            # 'http://www.rokit.co.uk/vintage-womens/womens-designer-brands-clothing-and-accessories',
            # 'http://www.rokit.co.uk/vintage-womens/90s-clothing-nineties-1990s-vintage-collection',
            # 'http://www.rokit.co.uk/vintage-womens/80s-clothing-eighties-1980s-classic-vintage-collection',
            # 'http://www.rokit.co.uk/vintage-womens/70s-clothing-seventies-1970s-classic-vintage-collection',
            # 'http://www.rokit.co.uk/vintage-womens/60s-clothing-sixties-1960s-classic-vintage-collection',
            # 'http://www.rokit.co.uk/vintage-womens/50s-clothing-fifties-1950s-classic-vintage-collection',
            # 'http://www.rokit.co.uk/vintage-womens/40s-clothing-forties-1940s-classic-vintage-collection',
            # 'http://www.rokit.co.uk/vintage-womens/20s-30s-clothing-twenties-thirties-1920s-1930s-classic-antique-vintage-collection',
            # 'http://www.rokit.co.uk/vintage-womens/womens-ski-snow',
            # 'http://www.rokit.co.uk/vintage-childrens/clothing-kidswear',
            # 'http://www.rokit.co.uk/vintage-childrens/accessories-kids',
            # 'http://www.rokit.co.uk/vintage-childrens/shoes-and-boots-and-trainers-kids',
            # 'http://www.rokit.co.uk/trends/stranger-things-vintage-style',
            # 'http://www.rokit.co.uk/trends/70s-luxe-vintage',
            # 'http://www.rokit.co.uk/trends/the-student-edit',
            # 'http://www.rokit.co.uk/trends/street-smart',
            # 'http://www.rokit.co.uk/trends/the-zoe-edit',
            # 'http://www.rokit.co.uk/trends/staff-edit-fia',
            # 'http://www.rokit.co.uk/trends/denim-jackets',
            # 'http://www.rokit.co.uk/trends/i-do-want-that-dress',
            # 'http://www.rokit.co.uk/trends/fresh-prince-edit',
            # 'http://www.rokit.co.uk/trends/retro-sportswear',
            # 'http://www.rokit.co.uk/rokit-recycled/clothing',
            # 'http://www.rokit.co.uk/rokit-recycled/accessories'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # The response is a single html file with several sets, need to have xpath selector that is common for all sets
        products = Selector(response).xpath('.//div[@class = "product product-0"]')
        print(products)
        for product in products:

            # Write out xpath and css selectors for all fields to be retrieved
            item = RokitItem()
            NAME_SELECTOR = 'normalize-space(.//h4/text())'
            PRICE_SELECTOR = 'normalize-space(.//p[@class = "price"]/text())'
            PRODURL_SELECTOR = './/a[@class = "product-list-link"]/@href'
            IMAGE_SELECTOR = 'img ::attr(src)'

            # Assemble the item object which will be passed then to pipeline
            item['name'] = product.xpath(NAME_SELECTOR).extract_first()
            item['price'] = product.xpath(PRICE_SELECTOR).re('[.0-9]+')
            item['prod_url'] = response.urljoin(product.xpath(PRODURL_SELECTOR).extract_first())
            item['image_urls'] = product.css(IMAGE_SELECTOR).extract()

            # Calculate SHA1 hash of image URL to make it easy to find the image based on hash entry and vice versa
            # Add the hash to item
            img_string = product.css(IMAGE_SELECTOR).extract_first()
            hash_object = hashlib.sha1(img_string.encode('utf8'))
            hex_dig = hash_object.hexdigest()
            item['image_hash'] = hex_dig

            yield item

        # Find URL in response HTML to which navigate next and then if such url exists do another request and pass to
        #  parse func
        NEXT_PAGE_SELECTOR = './/a[@class = "next"][last()]/@href'
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
