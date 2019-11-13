import json
import requests
import pathlib

userSettings = {
   'apiKey': 'SHB5CD-EFC6KL-59CBXL-48F5',
}
satelitesIds = [36516, 33591, 29155, 25338, 28654, 25544, 25994]

def main():
    generateFiles()


def generateFiles():
    
    for sateliteId in satelitesIds:
        print(sateliteId)

        paramSettings = {
        'id': sateliteId,
        'observer_lat': 41.702,
        'observer_lng': -76.014,
        'observer_alt': 0,
        'seconds': 3600,

        }
        dataParam = str(paramSettings['id']) + '/' + str(paramSettings['observer_lat']) + '/' + str(paramSettings['observer_lng']) + '/' + str(paramSettings['observer_alt']) + '/' + str(paramSettings['seconds']) + '/'

        url='https://www.n2yo.com/rest/v1/satellite/positions/' + dataParam
        resp = requests.get(url, params=userSettings)

        # if error
        if resp.status_code != 200:
            print('[ERROR] code: ' + resp.status_code)

        # if success
        response = resp.json()

        path = pathlib.Path(str(response['info']['satid']) + '.dat')
        
        if path.exists():
            update(response)

        save(response)


def save(response):
    fileName = str(response['info']['satid'])
    f = open(fileName +".dat","w+")

    f.write(json.dumps(response))
    f.close()

def update(response):
    fileName = str(response['info']['satid'])
    f = open(fileName + ".dat","w+")

    data = json.loads(f.read())

    data['positions'].append(response['positions'])

    f.write(str(data))

    f.close()

main()


