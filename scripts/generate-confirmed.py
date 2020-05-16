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
tanggal = dir[4:6] + "/" + dir[2:4] + "/20" + dir[0:2]

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

judul = "Confirmed Cases di Jawa Barat"
plt.title(judul)
plt.xlabel('Tanggal')
plt.ylabel("Jumlah")


# plt.show()
output = outputdir+"/confirmed.png"
try:
   plt.savefig(output)
except:
   print("Cannot save figure")
