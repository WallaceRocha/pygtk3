import json
import requests
import http.client
import urllib.parse
id_sw = ""
nw_src = ""
nw_dst = ""
actions = ""
nw_proto = ""
priority = ""

def setting(origem,destino,action,prioridade,id_switch, protocolo):
    global id_sw
    global nw_src
    global nw_dst
    global actions
    global nw_proto
    global priority
    
    id_sw = id_switch
    nw_src = origem
    nw_dst = destino
    actions = action
    nw_proto = protocolo
    priority = prioridade
    return priority, nw_proto, actions, nw_dst, nw_src, id_sw


#def identi_sw (id_s):
#    complemento = "000000000000000"
#    id_sw = id_s
#    id_sw = 16 - len(id_s)
#    lendo = complemento[0:id_sw]
#    id_sw = (str(lendo) + str(id_s))
#    return id_sw

def urls ():
    url = {}
    url ["url_rules"] = ('http://localhost:8080/firewall/rules/%s' %id_sw)
    url ["url_initial_status"] = "/firewall/module/enable/0000000000000001"
    url ["url_status_switche"] = "/firewall/module/status"
    url ["url_delete"] = "http://localhost:8080/firewall/rules/0000000000000001"
    url ["url_all_rules"] = "/firewall/rules/0000000000000001"
    url ["url_acquiring_log"] =  "/firewall/log/status"
    url ["url_changing_log"] = "/firewall/log/enable/0000000000000001"
    return url


def parametros_firewall (nw_src, nw_dst, actions, priority):
    newConditions = {}
    newConditions ["nw_src"] = nw_src
    newConditions ["nw_dst"] = nw_dst
    newConditions ["nw_proto"] = nw_proto
    newConditions ["actions"] = actions
    newConditions ["priority"] = priority
    return newConditions

def parametros_servidor ():
    socket = {}
    socket ["ip"]= "localhost"
    socket ["port"] = 8080
    return socket

def initial_status ():
    url_initial_status = urls ()
    url = url_initial_status ["url_initial_status"]
    socket = parametros_servidor ()
    ip = socket ["ip"]
    port = socket ["port"]
    comment = http.client.HTTPConnection (ip, port)
    comment.request("PUT", url)
    response = comment.getresponse()

    status = response.status
    reacao = response.reason
    dados = response.read ()
    comment.close()
    print (dados)

def rules ():
    url_rules = urls ()
    newConditions = parametros_firewall (nw_src, nw_dst, actions, priority)
    conditionsSetURL = url_rules ["url_rules"]
    params = json.dumps(newConditions).encode('utf8')
    req = urllib.request.Request(conditionsSetURL, data=params,
                                headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(req)

    saida = response.read().decode('utf8')

    print (saida)

def status_switche ():
    url_status_switche = urls ()
    url = url_status_switche ["url_status_switche"]
    socket = parametros_servidor ()
    ip = socket ["ip"]
    port = socket ["port"]
    comment = http.client.HTTPConnection (ip, port)
    comment.request ("GET", url)
    response = comment.getresponse()

    status = response.status
    reacao = response.reason
    dados = response.read ()
    print (dados)
def delete ():
    print ("`")

def acquiring_all_rules ():
    all_rules = urls ()
    url = all_rules ["url_all_rules"]
    socket = parametros_servidor ()
    ip = socket ["ip"]
    port = socket ["port"]
    comment = http.client.HTTPConnection (ip, port)
    comment.request ("GET", url)
    response = comment.getresponse()

    dados = response.read ()
    status = response.status
    reacao = response.reason

    print (dados)

def acquiring_log_output ():
    acquiring_log = urls()
    url = acquiring_log ["url_acquiring_log"]
    socket = parametros_servidor ()
    ip = socket ["ip"]
    port = socket ["port"]
    comment = http.client.HTTPConnection (ip, port)
    comment.request ("GET", url)
    response = comment.getresponse()

    status = response.status
    reacao = response.reason
    dados = response.read ()
    print (dados)
    
def changing_log_output ():
    changing_log = urls ()
    url = changing_log ["url_changing_log"]
    socket = parametros_servidor ()
    ip = socket ["ip"]
    port = socket ["port"]
    comment = http.client.HTTPConnection (ip, port)
    comment.request("PUT", url)
    response = comment.getresponse()

    status = response.status
    reacao = response.reason
    dados = response.read ()
    comment.close()
    print (dados)


