class Stock():
    def __init__(self, id, provider, product, purchaseCost, stock_quantity, lastPurchase, salePrice):
        self.id = id
        self.provider = provider
        self.product = product
        self.purchaseCost = purchaseCost
        self.stock_quantity = stock_quantity
        self.lastPurchase = lastPurchase
        self.salePrice = salePrice
