import api
import datetime

from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
db = client.fashion                                                                             
#db.create_collection('product')  or  ('test')                                                 # create new db.name

date = datetime.datetime.today().strftime('%m-%d-%y')
api = api.Api()
total_pages = api.get_listings()['listingPagination']['totalPages']



### IF YOU ARE NEW HERE
def run_get_pages():
    for page in range(1, total_pages + 1):
        # print(page)
        ff_json = api.get_listings(page=page)      #All pages
    
        for i in range(len(ff_json['listingItems']['items'])):
            product = ff_json['listingItems']['items'][i]                         
        
            db.product.insert_one(product)                                                         
            
            
### IF JUST WANT TO RE-SCRAP
def run_get_new():
    ff_json_new = api.get_listings()               #only first page

    database_id = [dict_item['id'] for dict_item in list(db.product.find({},{'_id':0, 'id':1}))]  

    new_item = 0

    for item in ff_json_new['listingItems']['items']:

        if item['id'] not in database_id:
            new_item += 1
            db.prodcut.insert_one(item)                                                           
                
    if new_item == 0:
        print("nothing new")
    else:
        print(new_item)


if __name__ == '__main__':
    #run_get_pages()   ## unblock this code IF YOU ARE NEW HERE
    run_get_new()
    