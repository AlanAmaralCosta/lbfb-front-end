import requests

url_base = 'http://localhost:5000'


def get_clubes(endpoint):
    response = requests.get(url_base + endpoint)
    clubes = response.json()
    return clubes['clubes']


def get_clube_by_id(id):
    endpoint = '/clube/{}'.format(id)
    response = requests.get(url_base + endpoint)
    clube = response.json()
    return clube


def gravar_clube(endpoint, clube):
    url = url_base + endpoint
    headers = {'Content-Type': 'application/json'}
    data = {
        'name': clube['name'],
        'city': clube['city'],
        'state': clube['state'],
        'logo': clube['logo']
    }
    print(data)
    response = requests.post(url, headers=headers, json=data)
    return response
    # return response.json()


def atualizar_clube(endpoint, clube_id, clube):
    url = url_base + endpoint + '/' + str(clube_id)
    headers = {'Content-Type': 'application/json'}
    data = {
        'name': clube['name'],
        'city': clube['city'],
        'state': clube['state'],
        'logo': clube['logo']
    }
    response = requests.put(url, headers=headers, json=data)
    return response


def excluir_clube(clube_id):
    url = url_base + f'/clube/{clube_id}'
    response = requests.delete(url)
    return response
