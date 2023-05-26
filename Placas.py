def verificaCeara(placa):
    prefixo = placa[:3]
    
    intervalos = [
        ('HTX', 'HZA'),
        ('NQL', 'NRE'),
        ('NUM', 'NVF'),
        ('OCB', 'OCU'),
        ('OHX', 'OIQ'),
        ('ORN', 'OSV'),
        ('OZA', 'OZA'),
        ('PMA', 'POZ'),
        ('RIA', 'RIN'),
        ('SAN', 'SBV')
    ]
    
    for inicio, fim in intervalos:
        if inicio <= prefixo <= fim:
            return True
    
    return False


def verificaMaranhao(placa):
    prefixo = placa[:3]
    
    intervalos = [
        ('HOL', 'HQE'),
        ('NHA', 'NHT'),
        ('NMP', 'NNI'),
        ('NWS', 'NXQ'),
        ('OIR', 'OJQ'),
        ('OXQ', 'OXZ'),
        ('PSA', 'PTZ'),
        ('ROA', 'ROZ')
    ]
    
    for inicio, fim in intervalos:
        if inicio <= prefixo <= fim:
            return True
    
    return False


def verificaPiaui(placa):
    prefixo = placa[:3]
    
    intervalos = [
        ('LVF', 'LWQ'),
        ('NHU', 'NIX'),
        ('ODU', 'OEI'),
        ('OUA', 'OUE'),
        ('OVW', 'OVY'),
        ('PIA', 'PIZ'),
        ('QRN', 'QRZ'),
        ('RSG', 'RST')
    ]
    
    for inicio, fim in intervalos:
        if inicio <= prefixo <= fim:
            return True
    
    return False


"""
argumento = input("Qual o número da placa? ")

if verificaCeara(argumento):
    print("A placa é do Ceará")

elif verificaMaranhao(argumento):
    print("A placa é do Maranhão")

elif verificaPiaui(argumento):
    print("A placa é do Piauí")

else: 
    print("Aplaca não é da região Nordeste 1")
"""


argumentos = ["HTX","HZA","OZA","RIN","SBN","RIO", "HPF","NMA","NNA","PTA", "LWA", "OVA","QRT","RSU"]

for i in argumentos:
    if verificaCeara(i):
        print("A placa é do Ceará")

    elif verificaMaranhao(i):
        print("A placa é do Maranhão")

    elif verificaPiaui(i):
        print("A placa é do Piauí")

    else: 
        print("A placa não é da região Nordeste 1")



