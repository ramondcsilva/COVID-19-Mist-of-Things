# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 00:12:16 2021

@author: Ramon Silva
"""

#import random
import time

from paho.mqtt import client as mqtt_client

import random

# numero randomico para simular dados do oximetro
rndTemperatura = random.randint(36,39) #ºCelsius
rndSaturacao = random.randint(85,97) # Porcetagem
rndRespiratorio = random.randint(9,29) #movimento/minuto
rndCardiaco = random.randint(51,120) #b/minuto
rndArterial = random.randint(61,130) #mmHg

broker = '127.0.0.1'
port = 1883

topic = "paciente"
topicTemperatura = "temperatura"
topicSaturacao = "saturacao"
topicRespiratoria = "respiratoria"
topicCardiaca = "cardiaco"
topicArterial = "arterial"

# generate client ID with pub prefix randomly
id = str(random.randint(0,1000))
client_id = f'paciente'+str(id)
msg_count = 0
# username = 'emqx'
# password = 'public'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    def data_patient():
        i = 0
        if i == 0:
            valueTemp = rndTemperatura
            valueSatu = rndSaturacao
            valueResp = rndRespiratorio
            valueCard = rndCardiaco
            valueArte = rndArterial
            pontuacao = 0
            estado = ''
        
        # Soma com valores randomicos -1 a 1 gerando uma media longiqua
        valueTemp = valueTemp + random.randint(-1,1)
        valueSatu = valueSatu + random.randint(-1,1)
        valueResp = valueResp + random.randint(-1,1)
        valueCard = valueCard + random.randint(-1,1)
        valueArte = valueArte + random.randint(-1,1)
        
        #Limita os valores maximos
        if valueTemp == 40:
            valueTemp = valueTemp + random.randint(-1,0)
        if valueSatu == 98:
            valueSatu = valueSatu + random.randint(-1,0)
        if valueResp == 30:
            valueResp = valueResp + random.randint(-1,0)
        if valueCard == 121:
            valueCard = valueCard + random.randint(-1,0)
        if valueArte == 131:
            valueArte = valueArte + random.randint(-1,0)
            
        #Limita os valores minimos
        if valueTemp == 35:
            valueTemp = valueTemp + 1
        if valueSatu == 84:
            valueSatu = valueSatu + 1
        if valueResp == 8:
            valueResp = valueResp + 1
        if valueCard == 50:
            valueCard = valueCard + 1
        if valueArte == 70:
            valueArte = valueArte + 1
        
        
        #Temperatura
        if valueTemp >= 38:   
            x = pontuacao
            x = x + 1
            pontuacao = x                
        else:
           x = pontuacao
           x = x + 0
           pontuacao = x
        
        # Saturacao Sanguinea
        if valueSatu < 86:
            x = x + 3
            pontuacao = x
        elif valueSatu < 90: 
            x = x + 2
            pontuacao = x
            
        elif valueSatu < 93:
            x = x + 1
            pontuacao = x
        else:
            x = x + 0
            pontuacao = x    
                
        # Frequencia Respiratoria
        if valueResp > 25:
            x = x + 3
            pontuacao = x
        elif valueResp > 20: 
            x = x + 2
            pontuacao = x
            
        elif valueResp > 15:
            x = x + 1
            pontuacao = x
            
        else:
            x = x + 0
            pontuacao = x
        
        
        # Frequencia Cardiaca
        if valueCard > 120:
            x = x + 3
            pontuacao = x
        elif valueCard > 110: 
            x = x + 2
            pontuacao = x
            
        elif valueCard > 100:
            x = x + 1
            pontuacao = x
            
        else:
            x = x + 0
            pontuacao = x
        
        
        # Pontuacao Pressao Arterial
        if valueArte < 72:
            x = x + 3
            pontuacao = x
        elif valueArte < 81: 
            x = x + 2
            pontuacao = x
        elif valueArte < 100:
            x = x + 1
            pontuacao = x
        else:
            x = x + 0
            pontuacao = x
        
        # Informa o Estado do paciente de acordo com os seus dados
        if x >= 5:
            estado = 'Grave'
        elif x > 2:    
            estado = 'Alerta'
        else:
            estado = 'Estavel'
        
        
        message = [str(id)+",Nome,paciente_"+str(id)+",idade,22,Estado,"+estado+",Pontuacao,"+str(pontuacao),
                   str(id)+",Temperatura,"+str(valueTemp),
                   str(id)+",SaturacaoSanguinea,"+str(valueSatu),
                   str(id)+",FrequenciaRespiratoria,"+str(valueResp),
                   str(id)+",FrequenciaCardiaca,"+str(valueCard),
                   str(id)+",PressaoArterialMaxima,"+str(valueArte)]
        
        #+",PressaoArterialMaxima,"+str(valueArte)+",FrequenciaRespiratoria,"+str(valueResp)+",FrequenciaCardiaca,"+str(valueCard)+",SaturacaoSanguinea,"+str(valueSatu)+",Estado,x,Pontuacao,00"
            
        return message
    
    while True:
        time.sleep(1)
        msg = data_patient()
        
        result = client.publish(topic, msg[0])
        time.sleep(0.2)
        result = client.publish(topicTemperatura, msg[1])
        time.sleep(0.2)
        result = client.publish(topicSaturacao, msg[2])
        time.sleep(0.2)
        result = client.publish(topicRespiratoria, msg[3])
        time.sleep(0.2)
        result = client.publish(topicCardiaca, msg[4])
        time.sleep(0.2)
        result = client.publish(topicArterial, msg[5])
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        # msg_count += 1

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()