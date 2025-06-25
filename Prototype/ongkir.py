import requests
import json

# Fungsi untuk membaca API Key dari file JSON
def get_api_key():
    try:
        with open("apikey.json", "r") as f:
            data = json.load(f)
            return data["key"]
    except Exception as e:
        print("Gagal membaca API Key:", e)
        exit()

# Fungsi untuk mengambil data kota dari RajaOngkir
def ambil_kota(api_key):
    url = "https://api.rajaongkir.com/starter/city"
    headers = {'key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    kota_list = data["rajaongkir"]["results"]
    return kota_list

# Fungsi untuk menampilkan daftar kota (ID - Nama Kota)
def tampilkan_kota(kota_list):
    print("\nDaftar Kota:")
    for kota in kota_list:
        print(f"{kota['city_id']:>5} - {kota['city_name']}, {kota['province']}")

# Fungsi utama untuk menghitung ongkir
def hitung_ongkir(api_key, origin, destination, weight, courier):
    url = "https://api.rajaongkir.com/starter/cost"
    headers = {'key': api_key}
    parameter = {
        'origin': origin,
        'destination': destination,
        'weight': weight,
        'courier': courier
    }

    response = requests.post(url, headers=headers, data=parameter)
    data = response.json()

    print("\n=== Hasil Perhitungan Ongkir ===")
    if data['rajaongkir']['status']['code'] == 200:
        for result in data['rajaongkir']['results']:
            kurir = result['name']
            for cost in result['costs']:
                service = cost['service']
                biaya = cost['cost'][0]['value']
                etd = cost['cost'][0]['etd']
                print(f"\nKurir              : {kurir}")
                print(f"Jenis Layanan      : {service}")
                print(f"Biaya              : Rp{biaya:,.0f}")
                print(f"Estimasi Pengiriman: {etd} hari")
    else:
        print("Gagal menghitung ongkir. Periksa parameter input Anda.")

# ==============================
# Main Program
# ==============================

api_key = get_api_key()
kota_list = ambil_kota(api_key)

# Tampilkan daftar kota
tampilkan_kota(kota_list)

# Input user
origin = input("\nMasukkan ID Kota Asal       : ").strip()
destination = input("Masukkan ID Kota Tujuan     : ").strip()
weight = input("Masukkan Berat (gram)       : ").strip()
courier = input("Masukkan Kurir (jne/pos/tiki): ").strip().lower()

# Jalankan fungsi ongkir
hitung_ongkir(api_key, origin, destination, weight, courier)
