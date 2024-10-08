import numpy as np
import matplotlib.pyplot as plt

v0 = 0  
g = 9.8 
h0 = 15

t_jatuh = np.sqrt(2 * h0 / g)
print("Waktu Jatuh Benda =", t_jatuh, "s")
v_akhir = g * t_jatuh
print("Kecepatan Akhir Benda =", v_akhir, "m/s")
h_akhir = h0 - 0.5 * g * t_jatuh**2
print("Ketinggian Akhir Benda =", h_akhir, "m") 

t = np.linspace(0, t_jatuh, 1000)
v = g * t 
h = h0 - 0.5 * g * t**2  

fig, ax = plt.subplots()
ax.plot(t, v)
ax.set(xlabel='Waktu (s)', ylabel='Kecepatan (m/s)', title='Grafik Kecepatan sebagai Fungsi Waktu selama Benda Jatuh')
ax.grid()

fig, ax = plt.subplots()
ax.plot(t, h)
ax.set(xlabel='Waktu (s)', ylabel='Ketinggian (m)', title='Grafik Posisi Benda sebagai Fungsi Waktu selama Benda Jatuh')
ax.grid()

plt.show()
