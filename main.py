import requests
import json
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from ttkthemes import ThemedStyle
from screeninfo import get_monitors

# Fungsi untuk mengambil API key dari file json dan endpoint
def get_apikey():
    with open('apikey.json', 'r') as f:
        data = json.load(f)
    apikey = data.get('key')
    if not apikey:
        raise ValueError("API key untuk RajaOngkir tidak ditemukan dalam apikey.json")
    return apikey

# Fungsi untuk mengambil data destinasi dan origin dari API RajaOngkir
def dapatkan_data_destinasi():
    apikey = get_apikey()
    url = "https://api.rajaongkir.com/starter/city"
    headers = {'key': apikey}
    response = requests.get(url, headers=headers)
    result = response.json()
    data_kota = result['rajaongkir']['results']
    nama_kota = [kota['city_name'] for kota in data_kota]
    return data_kota, nama_kota

# Fungsi untuk mencocokkan input pengguna dengan item dalam dropdown
def saat_dropdown_dipilih(var_input, dropdown):
    input_user = var_input.get()
    cocokan = [kota for kota in nama_kota if kota.lower().startswith(input_user.lower())]
    dropdown['values'] = cocokan

# Fungsi untuk mengonversi nama kota menjadi ID kota
def dapatkan_id_kota_berdasarkan_nama(nama_kota, data_kota):
    for kota in data_kota:
        if kota['city_name'] == nama_kota:
            return kota['city_id']
    return None

# Fungsi untuk menampilkan hasil perhitungan ongkir
def hitung_biaya_pengiriman():
    kota_asal, kota_tujuan, berat, kurir = var_asal.get(), var_tujuan.get(), var_berat.get(), var_kurir.get()
    if not kota_asal or not kota_tujuan or not berat or not kurir:
        hasil.delete(1.0, tk.END)
        hasil.insert(tk.END, "Semua input harus diisi.")
        return

    processing_label.config(text="Processing...", font=("Arial", 16, "bold"))
    processing_label.update()

    id_asal = dapatkan_id_kota_berdasarkan_nama(kota_asal, data_kota)
    id_tujuan = dapatkan_id_kota_berdasarkan_nama(kota_tujuan, data_kota)

    if id_asal is None or id_tujuan is None:
        hasil.delete(1.0, tk.END)
        hasil.insert(tk.END, "Kota asal atau kota tujuan tidak valid.")
        processing_label.config(text="", font=("Arial", 12))
        return

    apikey = get_apikey()
    url = "https://api.rajaongkir.com/starter/cost"
    headers = {'key': apikey}
    payload = {
        "origin": id_asal,
        "destination": id_tujuan,
        "weight": berat,
        "courier": kurir
    }
    response = requests.post(url, data=payload, headers=headers)

    try:
        hasil_hitung = response.json()
    except json.JSONDecodeError:
        hasil.delete(1.0, tk.END)
        hasil.insert(tk.END, "Terjadi kesalahan dalam pengambilan data ongkos kirim.")
        processing_label.config(text="", font=("Arial", 12))
        return

    processing_label.config(text="", font=("Arial", 12))
    hasil.delete(1.0, tk.END)

    if 'rajaongkir' in hasil_hitung:
        biaya = hasil_hitung['rajaongkir']['results'][0]['costs']
        hasil_text = ""
        for i, cost in enumerate(biaya):
            service = cost['service']
            description = cost['description']
            value = cost['cost'][0]['value']
            etd = cost['cost'][0]['etd']
            hasil_text += f"Layanan: {service}\nDeskripsi: {description}\nBiaya: Rp {value:,.0f}\nETD: {etd} hari\n"
            if i < len(biaya) - 1:
                hasil_text += "----------------------------------------\n"
        hasil.insert(tk.END, hasil_text)
    else:
        hasil.insert(tk.END, "Terjadi kesalahan dalam pengambilan data ongkos kirim.")

# Fungsi bantuan dan tentang kami
def tampilkan_bantuan():
    hasil.delete(1.0, tk.END)
    try:
        with open("doc/help.md", "r", encoding="utf-8") as f:
            konten = f.read()
        hasil.insert(tk.END, konten)
    except FileNotFoundError:
        hasil.insert(tk.END, "File help.md tidak ditemukan.")

def tampilkan_tentang_kami():
    hasil.delete(1.0, tk.END)
    try:
        with open("doc/about.md", "r", encoding="utf-8") as file:
            isi = file.read()
            hasil.insert(tk.END, isi)
    except FileNotFoundError:
        hasil.insert(tk.END, "File 'about.md' tidak ditemukan.")

# Setup GUI
def atur_ukuran_dan_posisi_jendela():
    monitor = get_monitors()[0]
    x_pos = (monitor.width - 1000) // 2
    y_pos = (monitor.height - 600) // 2
    app.geometry(f"1000x600+{x_pos}+{y_pos}")

app = tk.Tk()
app.title("Aplikasi Cek Ongkir")
app.geometry("1200x800")
app.resizable(False, False)
style = ThemedStyle(app)
style.set_theme("plastik")
app.configure(bg="#F5F5F5")
atur_ukuran_dan_posisi_jendela()

frame_judul = tk.Frame(app, bg="#4CAF50", pady=10)
frame_judul.pack(fill="x")
label_judul = tk.Label(frame_judul, text="Aplikasi Cek Ongkir", font=("Arial", 20), fg="white", bg="#4CAF50")
label_judul.pack()

frame_input = tk.Frame(app, bg="#F5F5F5")
frame_input.pack(pady=10)

# Ambil data kota
data_kota, nama_kota = dapatkan_data_destinasi()

# Input GUI
var_asal, var_tujuan, var_berat, var_kurir = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
var_asal.trace('w', lambda *args: saat_dropdown_dipilih(var_asal, dropdown_asal))
var_tujuan.trace('w', lambda *args: saat_dropdown_dipilih(var_tujuan, dropdown_tujuan))

def buat_input(label, var, row, values=None):
    tk.Label(frame_input, text=label, font=("Arial", 12), bg="#F5F5F5").grid(row=row, column=0, padx=10, pady=5, sticky='w')
    entry = ttk.Combobox(frame_input, textvariable=var, values=values) if values else ttk.Entry(frame_input, textvariable=var)
    entry.grid(row=row, column=1, padx=10, pady=5)
    return entry

dropdown_asal = buat_input("Kota Asal (Origin):", var_asal, 0, nama_kota)
dropdown_tujuan = buat_input("Kota Tujuan (Destination):", var_tujuan, 1, nama_kota)
buat_input("Berat (gram):", var_berat, 2)
dropdown_kurir = buat_input("Kurir (JNE/POS/TIKI):", var_kurir, 3, ["jne", "pos", "tiki"])

# Menu
menu_bar = tk.Menu(app)
app.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu Utama", menu=file_menu)
file_menu.add_command(label="Bantuan", command=tampilkan_bantuan)
file_menu.add_command(label="Tentang Kami", command=tampilkan_tentang_kami)
file_menu.add_separator()
file_menu.add_command(label="Keluar", command=app.quit)

# Tombol
tk.Button(app, text="Hitung Ongkir", command=hitung_biaya_pengiriman, bg="#009688", fg="white", font=("Arial", 14)).pack(pady=10)

# Hasil
frame_hasil = tk.Frame(app, bg="#F5F5F5")
frame_hasil.pack(padx=10, pady=10, fill='both', expand=True)
processing_label = tk.Label(frame_hasil, text="", font=("Arial", 12), bg="#F5F5F5")
processing_label.pack()

frame_hasil_scroll = tk.Frame(frame_hasil, bg="#F5F5F5", borderwidth=1, relief='solid')
frame_hasil_scroll.pack(fill='both', expand=True, padx=10, pady=10)

hasil = scrolledtext.ScrolledText(frame_hasil_scroll, wrap=tk.WORD, font=("Arial", 12), bg="#F5F5F5", relief="flat")
hasil.pack(fill='both', expand=True)

app.mainloop()
