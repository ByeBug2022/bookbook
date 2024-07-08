import json
import urllib2
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
    
def token_post():
    auth = {"auth":{"identity":{"methods":["password"],"password":{"user":{"domain":{"id":"default"},"name":"admin","password":"passw0rd"}}},"scope":{"project":{"domain":{"id":"default"},"name":"admin"}}}}
    content = json.dumps(auth)
    headers = {"Content-type":"application/json","Accept": "application/json;charset=UTF-8"}
    auth_url = 'http://192.168.1.12:35357/v3/'
    token_url = auth_url+"auth/tokens"
    req = urllib2.Request(token_url, content, headers)
    response = urllib2.urlopen(req)
    token = response.info().getheader("X-Subject-Token")
    response.encoding='utf-8'
    response_json = json.loads(response.read())
    response_json = byteify(response_json)
    response_json['authtoken'] = token
    return response_json

def service_list(response):
    auth_url = 'http://192.168.1.12:35357/v3/'
    service_url = auth_url+"services"
    req = urllib2.Request(service_url)
    tokenid = response['authtoken']
    req.add_header('X-Auth-Token', tokenid)
    response = urllib2.urlopen(req)
    response_json = json.loads(response.read())
    return response_json
    
def get_nova_endpoint(response):
    services = response['token']['catalog']
    for i in range(0, len(services)):
        if services[i]['name'] == 'nova':
            nova_endpoint = services[i]['endpoints'][0]['url']
    return nova_endpoint

def image_list(response):
    novaurl = get_nova_endpoint(response)
    servers_url = novaurl+'/'+'images'
    req = urllib2.Request(servers_url)
    tokenid = response['authtoken']
    req.add_header('X-Auth-Token', tokenid)
    response = urllib2.urlopen(req)
    response_json = json.loads(response.read())
    return response_json
    
if __name__ == '__main__':
    response = token_post()
    print service_list(response)
    print image_list(response)

