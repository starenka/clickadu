import requests
import json

def getzones():
    
    zonelist = []
    
    headers = {'accept': 'application/json','Authorization': '068e22c96f57f5cf2495d8630d690799a21084d6',}

    params = (
        ('limit', '150'),
        ('page', '1'),  // TOHLE JE TEN CULPRIT SE KTERYM SI NEVIM RADY //
        ('dateFrom', '2021-12-26'),
        ('dateTill', '2022-01-26'),
        ('groupBy', 'zone'),
        ('campaignId', '1836584'),
    )

    response = requests.get('https://ssp.clickadu.com/v1.0/api/client/statistics/', headers=headers, params=params)
    data = json.loads(response.content)
    
    for i in data['result']['items']:
        zone = i['zone']
        zonelist.append(zone)
    
    return zonelist


def main():
    
    print(getzones())

    
if __name__ == '__main__':
    main()
