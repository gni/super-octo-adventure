import os
import pandas as pd
import numpy as np
from joursferies import JoursFeries
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

dbprod = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="mysql-secret-pw",
                                  db="dbprod"))

Session = sessionmaker(bind=dbprod)
session = Session()
session.execute('CREATE DATABASE IF NOT EXISTS {db};'.format(db="dbprod"))
session.execute('USE {db};'.format(db="dbprod"))


def de_lundi_a_dimanche():
    debut_lad = input('Veuillez saisir une date de début sur une semaine format jj/mm/aaaa hh:mm: ')
    lad = pd.date_range(start=debut_lad, periods=5)
    return lad

lad = de_lundi_a_dimanche()

df = pd.DataFrame({'dates' : lad})

df['indx'] = '5'
df['deb'] = df['dates'] - pd.DateOffset(hours=1)
df['fin'] = df['dates'] + pd.DateOffset(hours=2)

df.to_sql('tests', con=dbprod, if_exists='replace', index=False) #index_label='id'
session.execute("SELECT * FROM tests").fetchall()

def date_precise():
    debut_date_precise = input('Veuillez saisir une date de début format jj/mm/aaaa: ') 
    debut_date_precise = pd.Timestamp(debut_date_precise).date()
    nombre_de_mois = input('Nombres de mois format mm: ') 
    mois_range = pd.date_range(start=debut_date_precise, periods=int(nombre_de_mois), freq='M')
    mois_jour = mois_range.day.values
    mois_jour[debut_date_precise.day < mois_jour] = debut_date_precise.day
    c_date_precise = pd.to_datetime(mois_range.year*10000+mois_range.month*100+mois_jour, format='%Y%m%d')
    return c_date_precise

dateprc = date_precise()

dateprc
df1 = pd.DataFrame({'dates' : dateprc})


df1['indx'] = '6'
df1['deb'] = df1['dates'] - pd.DateOffset(hours=1)
df1['fin'] = df1['dates'] + pd.DateOffset(hours=2)

df1.to_sql('tests', con=dbprod, if_exists='append', index=False) # index_label='id'


session.execute("SELECT * FROM tests").fetchall()

session.close





