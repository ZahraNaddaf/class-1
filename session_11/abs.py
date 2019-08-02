
import pprint
import time
import urllib.request

def beautify(list_of_btc):
    beauty_list = []
    for i in list_of_btc:
        beauty_list.append({
            "time": time.asctime(time.localtime(i[0])),
            "open": i[1],
            "highest": i[2],
            "lowest": i[3],
            "closed": i[3]
        })
    return beauty_list


class CoinPrice:
    link = "https://api.pro.coinbase.com/products/BTC-USD/candles/"
    valid_intervals = ['1m', '5m', '15m', '1h', '1d']

    def __init__(self, intervals='5m'):
        if not intervals in self.valid_intervals:
            raise ValueError(f'invalid interval {intervals}')

        self.intervals = intervals
        self.__data = None

    @property
    def url(self):
        return self.link + self.intervals

    @property
    def data(self):
        if self.__data is None:
            req = urllib.request.Request(self.url, headers={'User-Agent': 'Mozilla/66.0.2'})
            req = urllib.request.urlopen(req)
            html = req.read()
            text = html.decode('utf-8')

            self.__data = beautify(eval(text))

        return self.__data


if __name__ == '__main__':
    btc = CoinPrice('1m')

    lst = btc.data

    print(lst)

    # {'time': 'Fri Aug  2 10:17:00 2019', 'open': 10468.39, 'highest': 10486.5, 'lowest': 10468.39, 'closed': 10468.39}
    f = lambda x: x['highest'] - x['lowest']
    out = sorted(lst, key=f)

    pprint.pprint(out[-10:])