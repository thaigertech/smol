```python
import scrapy

class AreaCodeItem(scrapy.Item):
    # define the fields for your item here like:
    place = scrapy.Field()
    area_code = scrapy.Field()
```