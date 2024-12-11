import stomp
import json

class Queues_Data_Geolocated(stomp.ConnectionListener):

    def on_message(self, data):
        self.process_data(data.body)

    def process_data(self, data):
        data = json.loads(data)
        formatted_data = {
            "indice": data['Indice'],
            "name": data['Name'],
            "type": data['Type'],
            "latitude": data['Latitude'],
            "longitude": data['Longitude'],
            "location": data['Location'],
            "WikipediaLink": data['WikipediaLink'],
            "PictureLink": data['PictureLink'],
            "BuildInYear": data['BuildInYear'],
        }
        print(formatted_data)

class Queues_Data_Tips(stomp.ConnectionListener):

    def on_message(self, data):
        print('\n\nNovo dado recebido:\n\n', data.body)
        self.process_data(data.body)

    def process_data(self, data):
        tips_List = json.loads(data)


connection_Data_Geolocated = stomp.Connection([('localhost', 61613)])  
connection_Data_Geolocated.set_listener('', Queues_Data_Geolocated())
connection_Data_Geolocated.connect(wait=True)
connection_Data_Geolocated.subscribe(destination='/queue/data_geolocated', id=1, ack='auto')
connection_Data_Geolocated.disconnect()

connection_Data_Tips = stomp.Connection([('localhost', 61613)])  
connection_Data_Tips.set_listener('', Queues_Data_Tips())
connection_Data_Tips.connect(wait=True)
connection_Data_Tips.subscribe(destination='/queue/data_tips', id=1, ack='auto')
connection_Data_Tips.disconnect()

while True:
    pass
