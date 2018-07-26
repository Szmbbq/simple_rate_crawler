# Simple Rate Crawler

A simple rate crawler to get currency rate from [this](http://qq.ip138.com/hl.asp) website.

## Usage
Execute *rate_crawler.py* using terminal.
Default currency types are: 'CNY', 'HKD', 'TWD', 'EUR', 'GBP', 'AUD', 'JPY' and 'KRW'.
'python rate_crawler.py 1'
'''
{'美元': '1', '当前汇率': '6.786400', '人民币': '6.7864'}
{'美元': '1', '当前汇率': '7.846900', '港元': '7.8469'}
{'美元': '1', '当前汇率': '30.577999', '台币': '30.577999'}
{'美元': '1', '当前汇率': '0.857300', '欧元': '0.8573'}
{'美元': '1', '当前汇率': '0.760690', '英镑': '0.76069'}
{'美元': '1', '当前汇率': '1.352800', '澳元': '1.3528'}
{'美元': '1', '当前汇率': '111.096001', '日元': '111.096001'}
{'美元': '1', '当前汇率': '1121.300049', '韩元': '1121.300049'}
'''
Or indicate currency types you interested in:
'python rate_crawler.py 1 RUB THB'
'''
{'美元': '1', '当前汇率': '62.901001', '俄罗斯卢布': '62.901001'}
{'美元': '1', '当前汇率': '33.389999', '泰国铢': '33.389999'}
'''

## Implementation
Use 'urllib' to send request and get response. Decode html Markups and extract rate info using 'BeautifulSoup'.
