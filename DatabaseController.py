# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 00:10:18 2021

@author: Ramon Silva
"""

import sqlite3 as sql

def createDatabase():
    # variavel que salva o id do paciente
    
    #dataSave = data.split(",")
    #print(dataSave)
    #inicia a escrito no documento JSON  
    
    con = sql.connect('dbPaciente.db')
    cur = con.cursor()
    
    cur.execute("drop table if exists ficha")
    cur.execute("drop table if exists temperatura")
    cur.execute("drop table if exists saturacao")
    cur.execute("drop table if exists respiracao")
    cur.execute("drop table if exists cardiaca")
    cur.execute("drop table if exists arterial")
    
    cur.execute('''Create table ficha 
                   (id int unique, nome, estado, pontuacao int)''')
    cur.execute('''Create table temperatura 
                   (id int unique, valortemperatura int)''')
    cur.execute('''Create table saturacao 
                   (id int unique, valorsaturacao int)''')
    cur.execute('''Create table respiracao 
                   (id int unique, valorrespiracao int)''')
    cur.execute('''Create table cardiaca 
                   (id int unique, valorcardiaca int)''')
    cur.execute('''Create table arterial 
                   (id int unique, valorarterial int)''')
    
    con.commit()
    con.close()
    
def updateTableFicha(data):
    # variavel que salva o id do paciente
    
    dataSave = data.split(",")
    print(dataSave)
    #inicia a escrito no documento JSON  
    
    con = sql.connect('dbPaciente.db')
    cur = con.cursor()
    
    cur.execute("update ficha set nome='"+dataSave[2]+"', estado='"+dataSave[6]+"', pontuacao="+dataSave[8]+" where id='"+dataSave[0]+"'")
        
    cur.execute("insert or ignore into ficha values ("+dataSave[0]+",'"+dataSave[2]+"','"+dataSave[6]+"',"+dataSave[8]+")")
    
    con.commit()
    con.close()
    
def updateTableTemperatura(data):
    # variavel que salva o id do paciente
    
    dataSave = data.split(",")
    #print(dataSave)
    #inicia a escrito no documento JSON  
    
    con = sql.connect('dbPaciente.db')
    cur = con.cursor()
    
    cur.execute("update temperatura set valortemperatura="+dataSave[2]+" where id="+dataSave[0])
    
    cur.execute("insert or ignore into temperatura values ("+dataSave[0]+","+dataSave[2]+")")
    
    con.commit()
    con.close()
    
def updateTableSaturacao(data):
    # variavel que salva o id do paciente
    
    dataSave = data.split(",")
    print(dataSave)
    #inicia a escrito no documento JSON  
    
    con = sql.connect('dbPaciente.db')
    cur = con.cursor()
    
    
    #cur.execute("if not exists(SELECT * from saturacao where id="+dataSave[0]+")"+             
    #                " update saturacao set valor_saturacao="+dataSave[2]+" where id="+dataSave[0]+         
    #                " else "+   
    #                "insert into saturacao values ("+dataSave[0]+","+dataSave[2]+ 
    #                ")")
    
    cur.execute("update saturacao set valorsaturacao="+dataSave[2]+" where id="+dataSave[0])
    
    cur.execute("insert or ignore into saturacao values ("+dataSave[0]+","+dataSave[2]+")")
    
    con.commit()
    con.close()
    
def updateTableRespiracao(data):
    # variavel que salva o id do paciente
    
    dataSave = data.split(",")
    print(dataSave)
    #inicia a escrito no documento JSON  
    
    con = sql.connect('dbPaciente.db')
    cur = con.cursor()
    
    cur.execute("update respiracao set valorrespiracao="+dataSave[2]+" where id="+dataSave[0])
    
    cur.execute("insert or ignore into respiracao values ("+dataSave[0]+","+dataSave[2]+")")
    
    con.commit()
    con.close()
    
def updateTableCardiaca(data):
    # variavel que salva o id do paciente
    
    dataSave = data.split(",")
    print(dataSave)
    #inicia a escrito no documento JSON  
    
    con = sql.connect('dbPaciente.db')
    cur = con.cursor()
    
    cur.execute("update cardiaca set valorcardiaca="+dataSave[2]+" where id="+dataSave[0])
    
    cur.execute("insert or ignore into cardiaca values ("+dataSave[0]+","+dataSave[2]+")")
    
    con.commit()
    con.close()
    
def updateTableArterial(data):
    # variavel que salva o id do paciente
    
    dataSave = data.split(",")
    print(dataSave)
    #inicia a escrito no documento JSON  
    
    con = sql.connect('dbPaciente.db')
    cur = con.cursor()
    
    cur.execute("update arterial set valorarterial="+dataSave[2]+" where id="+dataSave[0])
    
    cur.execute("insert or ignore into arterial values ("+dataSave[0]+","+dataSave[2]+")")
    
    con.commit()
    con.close()
    
if __name__ == '__main__':
    createDatabase()
