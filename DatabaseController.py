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
                   (id unique, nome, estado, pontuacao)''')
    cur.execute('''Create table temperatura 
                   (id unique, valor)''')
    cur.execute('''Create table saturacao 
                   (id unique, valor)''')
    cur.execute('''Create table respiracao 
                   (id unique, valor)''')
    cur.execute('''Create table cardiaca 
                   (id unique, valor)''')
    cur.execute('''Create table arterial 
                   (id unique, valor)''')
    
    con.commit()
    con.close()
    
def updateTableFicha(data):
    # variavel que salva o id do paciente
    
    dataSave = data.split(",")
    print(dataSave)
    #inicia a escrito no documento JSON  
    
    con = sql.connect('dbPaciente.db')
    cur = con.cursor()
    
    
    cur.execute("update ficha set nome='"+dataSave[2]+"', estado='"+dataSave[4]+"', pontuacao='"+dataSave[6]+"' where id='"+dataSave[0]+"'")
    
    cur.execute("insert or ignore into ficha values ('"+dataSave[0]+"','"+dataSave[2]+"','"+dataSave[4]+"','"+dataSave[6]+"')")
    
    con.commit()
    con.close()
    
def updateTableTemperatura(data):
    # variavel que salva o id do paciente
    
    dataSave = data.split(",")
    #print(dataSave)
    #inicia a escrito no documento JSON  
    
    con = sql.connect('dbPaciente.db')
    cur = con.cursor()
    
    cur.execute("update temperatura set valor="+dataSave[2]+" where id='"+dataSave[0]+"'")
    
    cur.execute("Insert or ignore into temperatura values ('"+dataSave[0]+"','"+dataSave[2]+"')")
    
    con.commit()
    con.close()
    
def updateTableSaturacao(data):
    # variavel que salva o id do paciente
    
    dataSave = data.split(",")
    print(dataSave)
    #inicia a escrito no documento JSON  
    
    con = sql.connect('dbPaciente.db')
    cur = con.cursor()
    
    
    cur.execute("update temperatura set valor="+dataSave[2]+" where id='"+dataSave[0]+"'")
    
    cur.execute("Insert or ignore into saturacao values ('"+dataSave[0]+"','"+dataSave[2]+"')")
    
    con.commit()
    con.close()
    
def updateTableRespiracao(data):
    # variavel que salva o id do paciente
    
    dataSave = data.split(",")
    print(dataSave)
    #inicia a escrito no documento JSON  
    
    con = sql.connect('dbPaciente.db')
    cur = con.cursor()
    
    cur.execute("update temperatura set valor="+dataSave[2]+" where id='"+dataSave[0]+"'")
    
    cur.execute("Insert or ignore into respiracao values ('"+dataSave[0]+"','"+dataSave[2]+"')")
    
    con.commit()
    con.close()
    
def updateTableCardiaca(data):
    # variavel que salva o id do paciente
    
    dataSave = data.split(",")
    print(dataSave)
    #inicia a escrito no documento JSON  
    
    con = sql.connect('dbPaciente.db')
    cur = con.cursor()
    
    cur.execute("update temperatura set valor="+dataSave[2]+" where id='"+dataSave[0]+"'")
    
    cur.execute("Insert or ignore into cardiaca values ('"+dataSave[0]+"','"+dataSave[2]+"')")
    
    con.commit()
    con.close()
    
def updateTableArterial(data):
    # variavel que salva o id do paciente
    
    dataSave = data.split(",")
    print(dataSave)
    #inicia a escrito no documento JSON  
    
    con = sql.connect('dbPaciente.db')
    cur = con.cursor()
    
    cur.execute("update temperatura set valor="+dataSave[2]+" where id='"+dataSave[0]+"'")
    
    cur.execute("Insert or ignore into arterial values ('"+dataSave[0]+"','"+dataSave[2]+"')")
    
    con.commit()
    con.close()
    
if __name__ == '__main__':
    createDatabase()
