# shoesStoreProductScraping

This is a Scrapy project to scrape product information from  https://www.asos.com/men/shoes-boots-trainers/boots/cat/?cid=5774&nlid=mw%7Cshoes%7Cshop%20by%20product&page=1.

This project is only meant for educational purposes.

## Selection 

Main Site


![Image of ShoppingSite](https://github.com/Aniruddhsinh03/shoesStoreProductScraping/blob/master/screenshots/1.jpg)

Product Url Selection

![Image of Product Url Selection](https://github.com/Aniruddhsinh03/shoesStoreProductScraping/blob/master/screenshots/2.jpg)

Next Page Url Selection

![Image of Next Page Url](https://github.com/Aniruddhsinh03/shoesStoreProductScraping/blob/master/screenshots/3.jpg)

Product Title Selection

![Image of Product Title](https://github.com/Aniruddhsinh03/shoesStoreProductScraping/blob/master/screenshots/4.jpg)

Product Price Json Response

![Image of Product Price Json](https://github.com/Aniruddhsinh03/shoesStoreProductScraping/blob/master/screenshots/5.jpg)

Product Details Selection

![Image of Product Details Selection](https://github.com/Aniruddhsinh03/shoesStoreProductScraping/blob/master/screenshots/6.jpg)



## Extracted data

This project extracts product title,price,product details,product code,brand,show after me,about me.
The extracted data looks like this sample:

      {
      "product_title": "ASOS DESIGN Wide Fit chelsea boots in black faux suede",
       "product_details": " – your go-to for all the latest trends, no matter who you are, where you’re from and what you’re up to.     Exclusive to ASOS, our universal brand is here for you, and comes in Plus and Tall. Created by us, styled by you.",
       "product_code": "1495062",
      "brand": " – your go-to for all the latest trends, no matter who you are, where you’re from and what you’re up to. Exclusive to   ASOS, our universal brand is here for you, and comes in Plus and Tall. Created by us, styled by you.",
      "look_after_me": [
       "Show your shoes a bit of TLC",
       "See below for full care instructions",
       "Remove light marks with a clean damp sponge"
       ],
      "about_me": [
       "Textile upper",
       "A versatile, everyday fabric"
        ],
       "product_price": "€38.71"
       }


## Spiders

This project contains one spider and you can list them using the `list`
command:

    $ scrapy list
    shoesStoreProductScrapingSpider

Spider extract the data from product page.




## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl shoesStoreProductScrapingSpider

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl shoesStoreProductScrapingSpider -o output.json
