import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


    def test_getDataPoint_calculatePriceBidEqualToAsk(self):
        quote = {'top_ask': {'price': 120.48, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}

        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                               (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidIsZero(self):
        quote = {'top_ask': {'price': 120.48, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}

        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                               (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceAskIsZero(self):
        quote = {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}

        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                               (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getRatio_calculateRatioIfPricesAreTheSame(self):
        price_a = 120.48
        price_b = 120.48
        self.assertEqual(getRatio(price_a, price_b), 1)

    def test_getRatio_calculateRatioIfPriceBIsZero(self):
        price_a = 120.48
        price_b = 0
        self.assertEqual(getRatio(price_a, price_b), None)

    def test_getRatio_calculateRatioIfPriceAIsZero(self):
        price_a = 0
        price_b = 120.48
        self.assertEqual(getRatio(price_a, price_b), 0)

    def test_getRatio_calculateRatioIfPriceAIsGreaterThanPriceB(self):
        price_a = 120.48
        price_b = 120.47
        self.assertGreater(getRatio(price_a, price_b), 1)

    def test_getRatio_calculateRatioIfPriceBIsGreaterThanPriceA(self):
        price_a = 120.47
        price_b = 120.48
        self.assertLess(getRatio(price_a, price_b), 1)


if __name__ == '__main__':
    unittest.main()
