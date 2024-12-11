import stomp
import json

class Queues_Data_Geolocated(stomp.ConnectionListener):

    def on_message(self, data):
        print('\n\nNovo dado recebido:\n\n', data.body)
        self.process_data(data.body)

    def process_data(self, data):
        data = json.loads(data)
        formatted_data = {
            "indice": data['indice'],
            "name": data['name'],
            "type": data['type'],
            "latitude": data['latitude'],
            "longitude": data['longitude'],
            "location": data['location'],
            "wikipedia_Link": data['wikipedia_Link'],
            "picture_Link": data['picture_Link'],
            "build_Year": data['build_Year'],
        }

    def close_connection(self):
        self.connect_ActiveMQ.disconnect()

class Queues_Data_Tips(stomp.ConnectionListener):

    def on_message(self, data):
        print('\n\nNovo dado recebido:\n\n', data.body)
        self.process_data(data.body)

    def process_data(self, data):
        data = json.loads(data)
        formatted_data = {
            "muralha_China": data['muralha_China'],
            "petra": data['petra'],
            "cristo_Redentor": data['cristo_Redentor'],
            "machu_Picchu": data['machu_Picchu'],
            "chichen_Itza": data['chichen_Itza'],
            "coliseu": data['coliseu'],
            "taj_Mahal": data['taj_Mahal'],
        }


    def close_connection(self):
        self.connect_ActiveMQ.disconnect()

connection_Data_Geolocated = stomp.Connection([('localhost', 61613)])  
connection_Data_Geolocated.set_listener('', Queues_Data_Geolocated())
connection_Data_Geolocated.connect(wait=True)
connection_Data_Geolocated.subscribe(destination='/queue/data_geolocated', id=1, ack='auto')
connection_Data_Geolocated.close_connection()

connection_Data_Tips = stomp.Connection([('localhost', 61613)])  
connection_Data_Tips.set_listener('', Queues_Data_Tips())
connection_Data_Tips.connect(wait=True)
connection_Data_Tips.subscribe(destination='/queue/data_tips', id=1, ack='auto')
connection_Data_Tips.close_connection()

