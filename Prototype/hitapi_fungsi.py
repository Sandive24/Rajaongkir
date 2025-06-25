import requests, os, json

# Fungsi untuk mengambil API key dari file eksternal
def get_apikey():
    with open(r'C:/My DATA/Gitub Project/Rajaongkir/apikey.json', 'r') as f:
        data = json.load(f)
    return data['key']

# Inisialisasi
api_key_value = get_apikey()
api_key = {'key': api_key_value}
base_url = 'https://api.rajaongkir.com/starter'

# Fungsi umum untuk memanggil endpoint
def hit_api(endpoint):
    url = f"{base_url}{endpoint}"
    response = requests.get(url, headers=api_key)
    return response.json()

# Tampilkan data provinsi
def tampilkan_data_provinsi(data_provinsi):
    print('DATA PROVINSI')
    for prov in data_provinsi['rajaongkir']['results']:
        print(f"{prov['province_id']} - {prov['province']}")
    input('\nTekan Enter untuk melanjutkan... ')

# Tampilkan data kota
def tampilkan_data_kota(data_kota):
    for kota in data_kota['rajaongkir']['results']:
        print(f"{kota['city_id']} - {kota['city_name']}")
    input('\nTekan Enter untuk melanjutkan... ')

# Cari provinsi
def cari_provinsi(data_provinsi):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Pilihan Cari Provinsi:')
        print('1. Cari Berdasarkan Nama')
        print('2. Cari Berdasarkan ID')
        print('3. Kembali Ke Menu Awal')
        pilihan2 = input('Pilihan Anda: ')
        print('\n')

        if pilihan2 == '1':
            cari = input('Masukkan Nama : ').upper()
            found = False
            for prov in data_provinsi['rajaongkir']['results']:
                if cari in prov['province'].upper():
                    if not found:
                        print('DAFTAR PROVINSI')
                    print(f"{prov['province_id']} - {prov['province']}")
                    found = True
            if not found:
                print(f'Tidak ada provinsi dengan nama "{cari}"')
            input('\nTekan Enter untuk melanjutkan... ')

        elif pilihan2 == '2':
            cari_id = input('Masukkan ID (1-34): ')
            found = False
            for prov in data_provinsi['rajaongkir']['results']:
                if prov['province_id'] == cari_id:
                    print(f"Provinsi dengan ID {cari_id} adalah {prov['province']}")
                    found = True
            if not found:
                print(f'Tidak ada provinsi dengan ID {cari_id}')
            input('\nTekan Enter untuk melanjutkan... ')

        else:
            break

# Cari kota
def cari_kota(data_kota):
    while True:
        print('Menu Pencarian')
        print('1. Cari Kota Berdasarkan Nama')
        print('2. Cari Kota Berdasarkan ID')
        print('3. Cari Kota Berdasarkan Huruf Awal')
        print('4. Kembali Ke Menu Awal')
        pilih2 = input('Pilihanmu   : ')
        os.system('cls' if os.name == 'nt' else 'clear')

        if pilih2 == '1':
            cari_nama = input('Masukkan Nama Kota   : ').upper()
            found = False
            for kota in data_kota['rajaongkir']['results']:
                if cari_nama in kota['city_name'].upper():
                    if not found:
                        print('DATA KOTA')
                    print(f"{kota['city_id']} - {kota['city_name']}")
                    found = True
            if not found:
                print(f'Tidak ada kota dengan nama {cari_nama}')
            print('\n')

        elif pilih2 == '2':
            cari_id = input('Masukkan ID Kota: ')
            found = False
            for kota in data_kota['rajaongkir']['results']:
                if kota['city_id'] == cari_id:
                    print(f"Kota dengan ID {cari_id} adalah {kota['city_name']}")
                    found = True
            if not found:
                print(f'Tidak ada kota dengan ID {cari_id}')
            print('\n')

        elif pilih2 == '3':
            huruf_awal = input('Masukkan Huruf Awal : ').upper()
            found = False
            for kota in data_kota['rajaongkir']['results']:
                if kota['city_name'].startswith(huruf_awal):
                    print(f"{kota['city_id']} - {kota['city_name']}")
                    found = True
            if not found:
                print("Tidak ada kota yang memenuhi kriteria.")
            print('\n')

        elif pilih2 == '4':
            break
        else:
            print('Pilihan Salah!')
            print('\n')

# Main
if __name__ == "__main__":
    prov_res = hit_api('/province')
    kota_res = hit_api('/city')

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Pilih Tindakan')
        print('1. Tampilkan Data Provinsi')
        print('2. Tampilkan Data Kota')
        print('3. Cari Provinsi')
        print('4. Cari Kota')
        print('5. Keluar')
        pilihan = input('Pilihan Anda: ')
        print('\n')

        if pilihan == '1':
            tampilkan_data_provinsi(prov_res)
        elif pilihan == '2':
            tampilkan_data_kota(kota_res)
        elif pilihan == '3':
            cari_provinsi(prov_res)
        elif pilihan == '4':
            cari_kota(kota_res)
        elif pilihan == '5':
            break
        else:
            print('Pilihan tidak valid!')
