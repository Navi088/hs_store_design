import os

urlfiles = 'static/css/imgs'
img_list = list(os.listdir(urlfiles))

# PRODUCTS ITEM 1
urlfile_1 = 'static/css/products/product 1'
img_list_1 = list(os.listdir(urlfile_1))

items = {
    "items": {

        "item 1": {
            "image": img_list[0],
            "name": "product 1",
            "price": 54.05,
            "status": "available",
            "gallery": img_list_1
        },
        "item 2": {
            "image": img_list[1],
            "name": "product 2",
            "price": 123.05,
            "status": "not available"
        },
        "item 3": {
            "image": img_list[2],
            "name": "product 3",
            "price": 987.05,
            "status": "not available"
        },
        "item 4": {
            "image": img_list[3],
            "name": "product 4",
            "price": 001.05,
            "status": "available"
        },
        "item 5": {
            "image": img_list[4],
            "name": "product 5",
            "price": 65.05,
            "status": "available"
        },
        "item 6": {
            "image": img_list[5],
            "name": "product 6",
            "price": 98.05,
            "status": "pending"
        }
    }
}



class GetItems:
    def paginate_items():
        lista = []

        for x in items["items"].values():
            lista.append(x)

        return lista