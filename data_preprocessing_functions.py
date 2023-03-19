import re

class Preprocessing():
    def price(self, p):

        p = p.lower()
        p = re.sub('\n', '', p)
        p = re.sub('\s+', ' ', p).strip()

        price = re.search('[0-9]*\.?[0-9]+', p)
        if price != None:
            price = float(price.group(0))

        if 'crore' in p:
            return int(price * 10000000)
        elif 'lakh' in p or 'lac' in p:
            return int(price * 100000)
        else:
            return int(price)
    def get_rooms_and_size(self, p):

        p = p.split('\n')

        sq_ft = re.search('[0-9]*,?[0-9]+', p[2])
        if sq_ft != None:
            sq_ft = sq_ft.group(0)

        sq_ft = re.sub('(?ism)sqft', '', sq_ft).strip()
        sq_ft = re.sub('(?ism),', '', sq_ft).strip()
        return [int(p[0]), int(p[1]), int(sq_ft)]

    def location(self):
        return None;