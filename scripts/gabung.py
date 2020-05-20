# Plot AKTIF
# Budi Rahardjo (@rahard)
# Mei 2020

outputdir = "../output/"

# list directories and find the latest date
from glob import glob
# nama file hanya yang berbentuk angka  "200515" => 2020/05/15
# ".." itu karena direktori di atas ini
f = glob("../[0-9][0-9][0-9][0-9][0-9][0-9]")
dir = sorted(f, reverse=True)[0]
#print(dir)
# karena format dir adalah "../200515" - sesuaikan dengan lokasi direktori
# maka ambil tanggal dari nama direktori tersebut
tanggal = dir[7:9] + "/" + dir[5:7] + "/20" + dir[3:5]
#print(tanggal)

# ambil nama file
frekap = glob(dir + "/" + "csv_tabel_aktif_*")[0]
grekap = glob(dir + "/" + "csv_tabel_confirmed_cases_*")[0]
hrekap = glob(dir + "/" + "csv_tabel_meninggal_*")[0]
irekap = glob(dir + "/" + "csv_tabel_sembuh_*")[0]


# plot
import pandas as pd

import sys

try:
   df = pd.read_csv(frekap)
   dg = pd.read_csv(grekap)
   dh = pd.read_csv(hrekap)
   di = pd.read_csv(irekap)
   # print(df.head())
except:
   print("Cannot open " + frekap)

# convert the column to datetime
df['Datetime'] = pd.to_datetime(df['Tanggal'])
dg['Datetime'] = pd.to_datetime(dg['Tanggal'])
dh['Datetime'] = pd.to_datetime(dh['Tanggal'])
di['Datetime'] = pd.to_datetime(di['Tanggal'])
#print(df.Datetime)
# add dg,dh,di to df
df['Confirmed'] = dg['WestJava']
df['Meninggal'] = dh['WestJava']
df['Sembuh'] = di['WestJava']
#print(df[['Datetime', 'WestJava', 'Confirmed', 'Meninggal', 'Sembuh']])

df = df.rename(columns={'WestJava':'Active'})

import matplotlib.pyplot as plt

ax = df.plot(x='Datetime', y=['Confirmed','Active', 'Sembuh', 'Meninggal'])

plt.grid(True)

judul = "COVID-19 di Jawa Barat sd. " + tanggal
plt.title(judul)
plt.xlabel('Tanggal')
plt.ylabel("Jumlah")

#plt.show()

output = outputdir+"/gabungan.png"
try:
   plt.savefig(output)
except:
   print("Cannot save figure")
