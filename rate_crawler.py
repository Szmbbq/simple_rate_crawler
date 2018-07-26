from urllib import request, parse
from bs4 import BeautifulSoup
import chardet
import sys

def get_rate_query(amount, currency):
    amount = amount if amount else 1
    currency = currency if currency else ['CNY', 'HKD', 'TWD', 'EUR', 'GBP', 'AUD', 'JPY', 'KRW']
    return [parse.urlencode({"from": "USD", "to": curr, "q": amount}) for curr in currency]

def get_query_url(url, query_list):
    return [url + "?%s" % encoded_query for encoded_query in query_list]

def get_rate(query_url):
    for url in query_url:
        # send request and get response
        response = request.urlopen(url)
        html = response.read()

        # detect html encode type and feed the decoded markup to bs4
        encode_type = chardet.detect(html)
        soup = BeautifulSoup(html.decode(encode_type["encoding"]), "lxml")

        # the target table
        rate_table = soup.find("table", attrs={"class": "rate"})

        # parsing the table and final result as dict form
        table_rows = rate_table.find_all("tr")
        labels = [label.get_text() for label in table_rows[1].find_all("td")]
        values = [value.get_text() for value in table_rows[2].find_all("td")]
        result = dict(zip(labels, values))
        
        # further improve this
        print(result)


if __name__ == "__main__":

    # prepare query list
    query_list = get_rate_query(sys.argv[1], sys.argv[2:])
    # get query url list
    query_url = get_query_url("http://qq.ip138.com/hl.asp", query_list)
    # get rate
    get_rate(query_url)