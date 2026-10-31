# -*-coding:utf-8 -*-

from glob import glob
import cfgrib
import subprocess

from meteofetch import Arome0025 as source
typefic = 'arome'

# from meteofetch import Arpege025 as source
# typefic = 'arpege'

#variables :
# 10u, 10v, si10 = composantes du vent à 10 m, vent à 10m
# gust = intensité des rafales
# prmsl = pression au niveau de la mer
# 2t, tp = temperature à 2 m et précipitations totales
# CAPE : orage dans le paquet SP2

##datasets=source.get_latest_forecast(paquet='SP1', variables=variables)

source.get_latest_forecast(paquet='SP1', path='.')
source.get_latest_forecast(paquet='SP2', path='.')

print(f'fin extraction meteofetch')


fichiers = sorted(glob(f'{typefic}__*.grib2'))

subprocess.run(
    ['grib_copy', *fichiers, f'{typefic}-all.grib2'],
    check=True)

subprocess.run(['wgrib2', f'{typefic}-all.grib2',
                '-small_grib', '5.0:7.0',  '42.0:43.5',
                f'{typefic}-toulon.grib2'], check=True)
print(f'{typefic}-toulon.grib2 géneré')

# #### ATENTION si le grib est trop gros xygrib refuse de l'afficher ####
print(f'grib_copy -w shortName=10u/10v/si10/gust/prmsl/2t/tp/CAPE_INS {typefic}-toulon.grib2 {typefic}-toulon-short.grib2')



# datasets = cfgrib.open_datasets(lstfic[0],engine="cfgrib")
# ds = datasets[0]
# print(ds.latitude.min().values)
# print(ds.latitude.max().values)





