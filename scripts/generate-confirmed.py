# Rekap CONFIRMED CASES
# Budi Rahardjo (@rahard)
# Mei 2020

outputdir = "../output/"

# list directories and find the latest date
from glob import glob
# nama file hanya yang berbentuk angka  "200515" => 2020/05/15
f = glob("../[0-9][0-9][0-9][0-9][0-9][0-9]")
dir = sorted(f, reverse=True)[0]
# print(dir)
# karena format dir adalah "../200515" - sesuaikan dengan lokasi direktori
# maka ambil tanggal dari nama direktori tersebut
tanggal = dir[7:9] + "/" + dir[5:7] + "/20" + dir[3:5]
#print(tanggal)

# ambil nama file
frekap = glob(dir + "/" + "csv_tabel_confirmed_cases_*")[0]
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

ax = df.plot(x='Datetime', y='WestJava')

plt.grid(True)

judul = "Confirmed Cases di Jawa Barat sd. " + tanggal
plt.title(judul)
plt.xlabel('Tanggal')
plt.ylabel("Jumlah")


# plt.show()
output = outputdir+"/confirmed.png"
try:
   plt.savefig(output)
except:
   print("Cannot save figure")
