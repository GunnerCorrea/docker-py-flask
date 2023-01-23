import pymongo


class Article:

    connection_str = "mongo_str"

    def find_url_by_id(self, id):
        client = pymongo.MongoClient(self.connection_str)

        print(id)
        db = client['article']

        col = db['pages']

        query = { "_id" : int(id) }

        result = col.find_one(query)

        return result

    def create_database(self):
        client = pymongo.MongoClient(self.connection_str)

        db = client['article']

    def create_collection(self):
        client = pymongo.MongoClient(self.connection_str)

        db = client['article']

        collection = client['pages']


    def insert_page(self):
        client = pymongo.MongoClient(self.connection_str)

        db = client['article']

        col = db['pages']

        page = { "_id": 25511207, "url": "https://oglobo.globo.com/mundo/erdogan-diz-delegacoes-da-suecia-finlandia-que-nao-precisam-se-incomodar-em-ir-turquia-nao-diremos-sim-entrada-na-otan-25511207", "product" : "oglobo" }

        line = col.insert_one(page)
