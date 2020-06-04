from scrapy import Selector
import request

url = "https://github.com/hatmahat"
html2 = request.get(url).content

html = '''
<html>
    <body>
        <div class="hello datacamp">
            <p>Hello World!</p>
        </div>
        <p>Enjoy DataCamp!</p>
    </body>
</html>
'''

sel = Selector(text=html)

sel.xpath("//p") # Selec all p

sel.xpath("//p").extract() # Print Array yg miliki tag p

sel.xpath("//p").extract_first()

ps = sel.xpath("//p") # Selec all p
first_p = ps[0]
second_p = ps[1]
first_p.extract()
second_p.extract()

