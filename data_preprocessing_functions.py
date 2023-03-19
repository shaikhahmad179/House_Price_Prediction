import re

class Preprocessing():

    def preprocess(self, string):
        string = string.lower()
        string = re.sub('\n', '', string)
        string = re.sub('\s+', ' ', string)
        string = string.strip()

        return string
    def price(self, p):

        p = Preprocessing.preprocess(self, p)
        price = re.search('[0-9]*\.?[0-9]+', p)
        if price != None:
            price = price.group(0)
        price = float(price)

        if 'crore' in p:
            return price * 10000000
        elif 'lakh' in p or 'lac' in p:
            return price * 100000
        else:
            return price
    def features(self):
        return None

    def location(self):
        return None;