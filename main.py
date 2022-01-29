from transcriber import transcriber

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print('PyCharm')
# a = transcriber(r"C:\Users\Admin\Downloads\segmentation.mp4")
# print(a)
# a.wait()
import requests


def getparagraphs(foo):
    endpoint = "https://api.assemblyai.com/v2/transcript/" + foo + "sentences"
    headers = {
        "authorization": "74806487cd224a64819840e848bccf88",
    }
    response = requests.get(endpoint, headers=headers)
    print(response.json())
    with open("ptest", 'w') as f:
        f.write(response.json()['text'])
    print('Transcript saved')

getparagraphs("o6ztyecn4y-c513-492b-86f2-36f965e148f1")

