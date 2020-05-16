# Rekap RATE
# Budi Rahardjo (@rahard)
# Mei 2020

outputdir = "../output/"

# list directories and find the latest date
from glob import glob
# nama file hanya yang berbentuk angka  "200515" => 2020/05/15
f = glob("../[0-9][0-9][0-9][0-9][0-9][0-9]")
dir = sorted(f, reverse=True)[0]
# print(dir)
tanggal = dir[4:6] + "/" + dir[2:4] + "/20" + dir[0:2]

# proses "csv_rekap_rate_provinsi*"
# ambil nama file
frekap = glob(dir + "/" + "csv_rekap_rate_provinsi*")[0]
print(frekap)

# plot
import pandas as pd

import sys

try:
   df = pd.read_csv(frekap)
   # print(df.head())
except:
   print("Cannot open " + frekap)

# convert the column to datetime
df['Datetime'] = pd.to_datetime(df['Tanggal'])
#print(df.Datetime)

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#ax = df.plot(x='Tanggal', y='West Java', xticks=df.index)
ax = df.plot(x='Datetime', y='West Java')

plt.grid(True)

judul = "Rate COVID-19 di Jawa Barat"
plt.title(judul)
plt.xlabel('Tanggal')


#plt.show()
output = outputdir+"/rate.png"
try:
   plt.savefig(output)
except:
   print("Cannot save figure")
