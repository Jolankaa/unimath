import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Şekil ve Eksen Ayarları
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Çemberin gerçekten yuvarlak görünmesi için oranları eşitliyoruz
ax.set_aspect('equal')

# Başlık ve ızgara
ax.set_title("Matplotlib ile Çembersel Hareket")
ax.grid(True, linestyle='--', alpha=0.6)

# 2. Grafik Elemanlarını Tanımlama
# a) Sabit Yörünge (Arka plandaki çember izi)
theta_vals = np.linspace(0, 2*np.pi, 100)
x_orbit = np.cos(theta_vals)
y_orbit = np.sin(theta_vals)
ax.plot(x_orbit, y_orbit, 'k--', alpha=0.3, label='Yörünge') # Silik siyah çizgi

# b) Hareketli Parçalar (Başlangıçta boş tanımlıyoruz)
point, = ax.plot([], [], 'ro', markersize=12, label='Cisim') # Kırmızı top
line, = ax.plot([], [], 'b-', lw=1)  # Merkeze bağlanan yarıçap çizgisi

ax.legend(loc='upper right')

# 3. Güncelleme Fonksiyonu (Her karede çağrılır)
def update(frame):
    # frame değeri değiştikçe açıyı değiştiriyoruz
    # 0'dan 2pi'ye kadar sürekli döngü
    angle = frame
    
    # Polar koordinattan kartezyene geçiş
    x = np.cos(angle)
    y = np.sin(angle)
    
    # Noktanın yeni konumunu set et
    point.set_data([x], [y])
    
    # Yarıçap çizgisini set et (Merkezden [0,0] -> Noktaya [x,y])
    line.set_data([0, x], [0, y])
    
    return point, line

# 4. Animasyonu Oluşturma
# frames: np.linspace ile açı değerlerini üretiyoruz (0'dan 2pi'ye)
frames = np.linspace(0, 2*np.pi, 120) 

ani = FuncAnimation(
    fig, 
    update, 
    frames=frames, 
    interval=30, # Her kare arası milisaniye (hız ayarı)
    blit=True,    # Sadece değişen yerleri çiz (performans için)
    repeat=True   # Animasyon bitince başa sar
)

plt.show()