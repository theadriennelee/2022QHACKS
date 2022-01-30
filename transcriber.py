import requests
from time import sleep
import json
class transcriber:

    auth_key = '74806487cd224a64819840e848bccf88'
    headers = {"authorization": auth_key, "content-type": "application/json"}
    transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
    upload_endpoint = 'https://api.assemblyai.com/v2/upload'

    def __init__(self,videolink):
        self.videolink = videolink
        print('Added vid link')
        self.upload_response = requests.post(
            self.upload_endpoint,
            headers=self.headers, data=self.read_file(self.videolink)
        )
        self.transcript_request = {'audio_url': self.upload_response.json()['upload_url']}
        self.transcript_response = requests.post(self.transcript_endpoint, json=self.transcript_request, headers=self.headers)
        print('Transcription Requested')
        print(self.transcript_response.json())
        self.polling_response = requests.get(self.transcript_endpoint + "/" + self.transcript_response.json()['id'],
                                        headers=self.headers)
        self.filename = self.transcript_response.json()['id'] + '.txt'
        print('Done Initializing')

    def __str__(self):
        return f"{self.videolink} is the video link"

    def read_file(self, filename):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(5242880)
                if not data:
                    break
                yield data


    def wait(self):
        while self.polling_response.json()['status'] != 'completed':
            sleep(30)
            self.polling_response = requests.get(self.transcript_endpoint + "/" + self.transcript_response.json()['id'],
                                            headers=self.headers)
            print("File is", self.polling_response.json()['status'])
            if self.polling_response.json()['status'] == "error":
                print("Error is", self.polling_response.json()['error'])
        with open(self.videolink, 'w') as f:
            f.write(self.polling_response.json()['text'])
        print('Transcript saved to', self.filename)

    def getparagraphs(self):
        endpoint = "https://api.assemblyai.com/v2/transcript/" + self.transcript_response.json()['id'] + "/paragraphs"
        headers = {
            "authorization": "74806487cd224a64819840e848bccf88",
        }
        response = requests.get(endpoint, headers=headers)
        with open("ptest.json", 'w') as f:
            f.write(json.dumps(response.json(), indent=2))
        print('Transcript saved')
        with open('ptest.json') as json_file:
            data = json.load(json_file)
        list_of_lists = []
        for x in range(len(data['paragraphs'])):
            list_of_lists.append(data['paragraphs'][x]['text'] + '\n')
        return list_of_lists

    def gettstamps(self):
        endpoint = "https://api.assemblyai.com/v2/transcript/" + self.transcript_response.json()['id']  + "/paragraphs"
        headers = {
            "authorization": "74806487cd224a64819840e848bccf88",
        }
        response = requests.get(endpoint, headers=headers)
        # print(json.dumps(response.json(), indent =2))
        # print(response.json())
        with open("ptest.json", 'w') as f:
            f.write(json.dumps(response.json(), indent=2))
        #print('Transcript saved')
        with open('ptest.json') as json_file:
            data = json.load(json_file)
        list_of_start = []
        list_of_end = []
        for x in range(len(data['paragraphs'])):
            list_of_start.append(data['paragraphs'][x]['start'])
            list_of_end.append(data['paragraphs'][x]['end'])
            #print('Start: ', list_of_start[-1])
            #print('End: ', list_of_end[-1])
        return list_of_start,list_of_end