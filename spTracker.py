from snowplow_tracker import Tracker, AsyncEmitter, Subject
import socket
from random import randint

class spTracker:

    def __init__(self):
        self.e = AsyncEmitter("d3rkrsqld9gmqf.cloudfront.net", thread_count=10)
        self.t = Tracker(self.e)
        self.t.subject.set_platform("app").set_user_id(socket.gethostname())

    def add_to_cart(self,itemid,itemname,price):
        self.t.track_add_to_cart(itemid,1,name=itemname,unit_price=price)

    def bought_items(self,basket,total):
        items = []
        for i in basket:
            itemdict = {"sku":    i[2],
                        "price":  i[1],
                        "quantity": 1
                       }
            items += [itemdict]
        self.t.track_ecommerce_transaction(str(randint(1,2000)), total, items=items)
        

    def clear_cart(self,basket):
        for i in basket:
            self.t.track_remove_from_cart(i[2],1,name=i[0],unit_price=i[1])

    def all_items_bought(self,basket):
        a_i_b = True
        allids = ['001','002','003','004','005','006','007','008','009']
        basketids = []
        for i in basket:
            basketids.append(i[2])
        for i in allids:
            if i not in basketids:
                a_i_b = False
                break;
        if a_i_b:
            self.t.track_struct_event('shop','all-items-bought')
            

if __name__ == "__main__":
    pass
    #tracker = spTracker()
    #tracker.bought_items([("Bacon",2.5,"001"),('Cheese',3,'003')])
