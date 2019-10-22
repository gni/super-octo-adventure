import os
import pandas as pd
import numpy as np
from joursferies import JoursFeries
import yaml
import argparse

with open('config.yml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

def les_jours_feries():
    debut = cfg['feries']['debut']
    fin = cfg['feries']['fin']
    cal = JoursFeries()
    jours_feries = cal.holidays(start=debut, end=fin)
    print (jours_feries)


def generer_delta():
    debut_detla = input('Veuillez saisir une date de début format aaaa jj/mm/aaaa: ') 
    fin_detla = input('Veuillez saisir une date de fin aaaa jj/mm/aaaa: ') 
    intervales = pd.date_range(start=debut_detla, end=fin_detla, tz='Europe/Paris')
    print(intervales)

def de_lundi_a_dimanche():
    debut_lad = input('Veuillez saisir une date de début sur une semaine format jj/mm/aaaa hh:mm: ')
    lad = pd.date_range(start=debut_lad, periods=5)
    print(lad)

def date_precise():
    debut_date_precise = input('Veuillez saisir une date de début format jj/mm/aaaa: ') 
    debut_date_precise = pd.Timestamp(debut_date_precise).date()
    nombre_de_mois = input('Nombres de mois format mm: ') 
    mois_range = pd.date_range(start=debut_date_precise, periods=int(nombre_de_mois), freq='M')
    mois_jour = mois_range.day.values
    mois_jour[debut_date_precise.day < mois_jour] = debut_date_precise.day
    c_date_precise = pd.to_datetime(mois_range.year*10000+mois_range.month*100+mois_jour, format='%Y%m%d')
    print(c_date_precise.replace(hour=0))

parser = argparse.ArgumentParser()
parser.add_argument('--feries', action='store_true', help='Pour avoir les jours féries configurés')
parser.add_argument('--intervales', action='store_true', help='Genere des dates entre 2 intervales de temps')
parser.add_argument('--lad', action='store_true', help='De lundi à vendredi')
parser.add_argument('--date_precise', action='store_true', help='Une date précise sur plusieurs mois')

args = parser.parse_args()
if args.feries:
    les_jours_feries()
if args.intervales:
    generer_delta()
if args.lad:
    de_lundi_a_dimanche()
if args.date_precise:
    date_precise()