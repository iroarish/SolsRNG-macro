class Item:
    def __init__(self, name, amount, img):
        self.item_name = name
        self.amount = amount
        self.button_img = img

class Potion:
    def __init__(self, potion_name, potion_button):
        self.potion_name = potion_name
        self.potion_button = potion_button

class Merchant:
    def __init__(self, seller, item):
        self.seller = seller
        self.item_buy = item