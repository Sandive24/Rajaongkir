import requests
import json
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from ttkthemes import ThemedStyle
from screeninfo import get_monitors

# Fungsi untuk membaca API Key dari file
def get_apikey():
    try:
        with open("apikey.json", "r") as f:
            data = json.load(f)
            return data["key"]
    except (FileNotFoundError, KeyError):
        raise RuntimeError("Gagal membaca API Key dari apikey.json")

# Fungsi untuk mengambil data destinasi dan origin dari API RajaOngkir
def dapatkan_data_destinasi():
    url = "https://api.rajaongkir.com/starter/city"
    headers = {'key': get_apikey()}
    response = requests.get(url, headers=headers)
    result = response.json()
    data_kota = result['rajaongkir']['results']
    nama_kota = [kota['city_name'] for kota in data_kota]
    return data_kota, nama_kota

# Fungsi untuk mencocokkan input pengguna dengan item dalam dropdown

def saat_dropdown_asal_dipilih(*args):
    input_user = var_asal.get()
    cocokan = [kota for kota in nama_kota if kota.lower().startswith(input_user.lower())]
    dropdown_asal['values'] = cocokan

def saat_dropdown_tujuan_dipilih(*args):
    input_user = var_tujuan.get()
    cocokan = [kota for kota in nama_kota if kota.lower().startswith(input_user.lower())]
    dropdown_tujuan['values'] = cocokan

# Fungsi untuk mengonversi nama kota menjadi ID kota
def dapatkan_id_kota_berdasarkan_nama(nama_kota, data_kota):
    for kota in data_kota:
        if kota['city_name'] == nama_kota:
            return kota['city_id']
    return None

# Fungsi untuk menghitung ongkir
def hitung_biaya_pengiriman():
    kota_asal = var_asal.get()
    kota_tujuan = var_tujuan.get()
    berat = var_berat.get()
    kurir = var_kurir.get()

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

    url = "https://api.rajaongkir.com/starter/cost"
    headers = {'key': get_apikey()}
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
            bantuan = f.read()
        hasil.insert(tk.END, bantuan)
    except FileNotFoundError:
        hasil.insert(tk.END, "File doc/help.md tidak ditemukan.")

def tampilkan_tentang_kami():
    hasil.delete(1.0, tk.END)
    try:
        with open("doc/about.md", "r", encoding="utf-8") as f:
            tentang = f.read()
        hasil.insert(tk.END, tentang)
    except FileNotFoundError:
        hasil.insert(tk.END, "File doc/about.md tidak ditemukan.")

# Atur posisi jendela

def atur_ukuran_dan_posisi_jendela():
    monitor = get_monitors()[0]
    x_pos = (monitor.width - 1000) // 2
    y_pos = (monitor.height - 600) // 2
    app.geometry(f"1000x600+{x_pos}+{y_pos}")

# GUI Utama
app = tk.Tk()
app.title("Aplikasi Cek Ongkir")
app.geometry("1200x800")
app.resizable(False, False)
style = ThemedStyle(app)
style.set_theme("plastik")

warna_utama = "#4CAF50"
warna_teks = "#333333"
warna_latar = "#F5F5F5"
warna_tombol = "#009688"

app.configure(bg=warna_latar)
atur_ukuran_dan_posisi_jendela()

frame_judul = tk.Frame(app, bg=warna_utama, pady=10)
frame_judul.pack(fill="x")

data_kota, nama_kota = dapatkan_data_destinasi()

label_judul = tk.Label(frame_judul, text="Aplikasi Cek Ongkir", font=("Arial", 20), fg="white", bg=warna_utama)
label_judul.pack()

frame_input = tk.Frame(app, bg=warna_latar)
frame_input.pack(pady=10)

label_asal = tk.Label(frame_input, text="Kota Asal:", font=("Arial", 12), fg=warna_teks, bg=warna_latar)
label_asal.grid(row=0, column=0, padx=10, pady=5, sticky='w')
var_asal = tk.StringVar()
var_asal.trace('w', saat_dropdown_asal_dipilih)
dropdown_asal = ttk.Combobox(frame_input, textvariable=var_asal)
dropdown_asal['values'] = nama_kota
dropdown_asal.grid(row=0, column=1, padx=10, pady=5)

label_tujuan = tk.Label(frame_input, text="Kota Tujuan:", font=("Arial", 12), fg=warna_teks, bg=warna_latar)
label_tujuan.grid(row=1, column=0, padx=10, pady=5, sticky='w')
var_tujuan = tk.StringVar()
var_tujuan.trace('w', saat_dropdown_tujuan_dipilih)
dropdown_tujuan = ttk.Combobox(frame_input, textvariable=var_tujuan)
dropdown_tujuan['values'] = nama_kota
dropdown_tujuan.grid(row=1, column=1, padx=10, pady=5)

label_berat = tk.Label(frame_input, text="Berat (gram):", font=("Arial", 12), fg=warna_teks, bg=warna_latar)
label_berat.grid(row=2, column=0, padx=10, pady=5, sticky='w')
var_berat = tk.StringVar()
input_berat = ttk.Entry(frame_input, textvariable=var_berat)
input_berat.grid(row=2, column=1, padx=10, pady=5)

label_kurir = tk.Label(frame_input, text="Kurir:", font=("Arial", 12), fg=warna_teks, bg=warna_latar)
label_kurir.grid(row=3, column=0, padx=10, pady=5, sticky='w')
var_kurir = tk.StringVar()
dropdown_kurir = ttk.Combobox(frame_input, textvariable=var_kurir, values=["jne", "pos", "tiki"])
dropdown_kurir.grid(row=3, column=1, padx=10, pady=5)

menu_bar = tk.Menu(app)
app.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu Utama", menu=file_menu)
file_menu.add_command(label="Bantuan", command=tampilkan_bantuan)
file_menu.add_command(label="Tentang Kami", command=tampilkan_tentang_kami)
file_menu.add_separator()
file_menu.add_command(label="Keluar", command=app.quit)

tombol_hitung = tk.Button(app, text="Hitung Ongkir", command=hitung_biaya_pengiriman, bg=warna_tombol, fg="white", font=("Arial", 14))
tombol_hitung.pack(pady=10)

frame_hasil = tk.Frame(app, bg=warna_latar)
frame_hasil.pack(padx=10, pady=10, fill='both', expand=True)

processing_label = tk.Label(frame_hasil, text="", font=("Arial", 12), fg=warna_teks, bg=warna_latar, justify='left')
processing_label.pack(fill='both', expand=True)

frame_hasil_scroll = tk.Frame(frame_hasil, bg=warna_latar, borderwidth=1, relief='solid')
frame_hasil_scroll.pack(fill='both', expand=True, padx=10, pady=10)

hasil = scrolledtext.ScrolledText(frame_hasil_scroll, wrap=tk.WORD, width=40, height=20, padx=10, pady=10)
hasil.config(font=("Arial", 12), bg=warna_latar, relief="flat")
hasil.pack(fill='both', expand=True)

app.mainloop()
