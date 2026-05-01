import numpy as np
import matplotlib.pyplot as plt
from math import * 

print("=== Kalkulator Regula Falsi dengan Grafik ===\n")
print("Info: gunakan '**' untuk pangkat (contoh: x**3 - 3*x + 1)")
print("Contoh rumus trigonometri: sin(x) - 5*x + 2")
print("Gunakan standard format: exp(x) untuk e^x, log(x) untuk ln(x)\n")

rumus = input("Masukkan persamaan f(x)    = ")
x1 = float(input("Masukkan batas x1      = "))
x2 = float(input("Masukkan batas x2      = "))
toleransi = float(input("Masukkan toleransi error (contoh: 0.0001) = "))

def f(x):
    return eval(rumus)

print("\nIterasi | x1 \t\t| x2 \t\t| x3\t\t| f(x3)")
print("-" * 80)

i = 1
while True:
    fx1 = f(x1)
    fx2 = f(x2)
    x3 = (x1 * fx2 - x2 * fx1) / (fx2 - fx1)
    fx3 = f(x3)
    
    print(f"{i}\t| {x1:.4f}\t| {x2:.4f}\t| {x3:.4f}\t| {fx3:.4f}")
    
    if abs(fx3) <= toleransi:
        print("-" * 80)
        print(f"AKAR DITEMUKAN! Pada iterasi ke-{i}, nilai x ≈ {x3:.4f}")
        akar_numerik = x3 
        break
        
    if fx1 * fx3 < 0:
        x2 = x3
    else:
        x1 = x3
        
    i += 1


print("\nMenampilkan grafik...")

def plot_grafik(rumus_input, start_x, end_x, akar_found):
    # Buat range X yang sedikit lebih lebar dari interval masukan agar grafik terlihat jelas
    interval_lebar = abs(end_x - start_x)
    
    # Sequence numerical creation menggunakan NumPy
    x_vector = np.linspace(start_x - 0.5 * interval_lebar, end_x + 0.5 * interval_lebar, 1000)
    
    local_scope = {"x": x_vector, "np": np}
    
    local_scope.update({
        "sin": np.sin, "cos": np.cos, "tan": np.tan,
        "exp": np.exp, "log": np.log, "pi": np.pi
    })

    try:
        y_vector = eval(rumus_input, local_scope)
    except Exception as e:
        print(f"Gagal menggambar grafik: {e}")
        return

    plt.figure(figsize=(10, 6)) # Ukuran Jendela
    
    # Plot kurva biru halus f(x)
    plt.plot(x_vector, y_vector, label=f'f(x) = {rumus_input}', color='blue', linewidth=2)
    
    # Plot garis merah horizontal standard sumbu-x di y=0
    plt.axhline(0, color='red', linestyle='-', linewidth=1.5)
    
    # Plot titik hijau untuk hasil akhir
    plt.plot(akar_found, 0, marker='o', color='green', markersize=10, label=f'Akar (x={akar_found:.4f})')
    
    # Menambahkan Labels, Title, standard Grid
    plt.title(f'Grafik Fungsi: {rumus_input}', fontsize=14)
    plt.xlabel('Nilai X', fontsize=12)
    plt.ylabel('Nilai f(X)', fontsize=12)
    plt.grid(True)
    plt.legend()
    
    plt.show() # Tab grafik akan terbuka

plot_grafik(rumus, x1, x2, akar_numerik)
