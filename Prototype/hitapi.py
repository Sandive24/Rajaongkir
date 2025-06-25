import requests
import os
import json

# Ambil API key dari file eksternal
def get_apikey():
    path = r'C:/My DATA/Gitub Project/Rajaongkir/apikey.json'
    with open(path, 'r') as file:
        data = json.load(file)
    return data['rajaongkir']

# Setup API
api_key = get_apikey()
headers = {'key': api_key}
base_url = 'https://api.rajaongkir.com/starter'

# Ambil data provinsi
provinsi_response = requests.get(f'{base_url}/province', headers=headers)
provinsi_list = provinsi_response.json()['rajaongkir']['results']

# Ambil data kota
kota_response = requests.get(f'{base_url}/city', headers=headers)
kota_list = kota_response.json()['rajaongkir']['results']

# Menu utama
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Pilih Tindakan')
    print('1. Tampilkan Data Provinsi')
    print('2. Tampilkan Data Kota')
    print('3. Cari Provinsi')
    print('4. Cari Kota')
    print('5. Keluar')
    pilihan = input('Pilihan Anda: ')
    print()

    if pilihan == '1':
        print('DATA PROVINSI')
        for prov in provinsi_list:
            print(f"{prov['province_id']} - {prov['province']}")
        input('\nTekan Enter untuk melanjutkan...')

    elif pilihan == '2':
        print('DATA KOTA')
        for kota in kota_list:
            print(f"{kota['city_id']} - {kota['city_name']}")
        input('\nTekan Enter untuk melanjutkan...')

    elif pilihan == '3':
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Pilihan Cari Provinsi:')
            print('1. Berdasarkan Nama')
            print('2. Berdasarkan ID')
            print('3. Kembali')
            sub = input('Pilihan Anda: ')
            print()

            if sub == '1':
                cari = input('Masukkan Nama: ').upper()
                found = False
                for prov in provinsi_list:
                    if cari in prov['province'].upper():
                        if not found:
                            print('DAFTAR PROVINSI')
                        print(f"{prov['province_id']} - {prov['province']}")
                        found = True
                if not found:
                    print(f'Tidak ada provinsi dengan nama "{cari}"')
                input('\nTekan Enter untuk melanjutkan...')

            elif sub == '2':
                cari_id = input('Masukkan ID (1-34): ')
                found = False
                for prov in provinsi_list:
                    if prov['province_id'] == cari_id:
                        print(f"Provinsi dengan ID {cari_id} adalah: {prov['province']}")
                        found = True
                if not found:
                    print(f'Tidak ada provinsi dengan ID {cari_id}')
                input('\nTekan Enter untuk melanjutkan...')

            elif sub == '3':
                break

            else:
                input('Pilihan tidak valid, tekan Enter untuk kembali...')

    elif pilihan == '4':
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Menu Pencarian Kota')
            print('1. Berdasarkan Nama')
            print('2. Berdasarkan ID')
            print('3. Berdasarkan Huruf Awal')
            print('4. Kembali')
            sub = input('Pilihan Anda: ')
            print()

            if sub == '1':
                cari = input('Masukkan Nama Kota: ').upper()
                found = False
                for kota in kota_list:
                    if cari in kota['city_name'].upper():
                        if not found:
                            print('DATA KOTA')
                        print(f"{kota['city_id']} - {kota['city_name']}")
                        found = True
                if not found:
                    print(f'Tidak ada kota dengan nama {cari}')
                input('\nTekan Enter untuk melanjutkan...')

            elif sub == '2':
                cari_id = input('Masukkan ID Kota: ')
                found = False
                for kota in kota_list:
                    if kota['city_id'] == cari_id:
                        print(f"Kota dengan ID {cari_id} adalah: {kota['city_name']}")
                        found = True
                if not found:
                    print(f'Tidak ada kota dengan ID {cari_id}')
                input('\nTekan Enter untuk melanjutkan...')

            elif sub == '3':
                huruf = input('Masukkan Huruf Awal: ').upper()
                found = False
                for kota in kota_list:
                    if kota['city_name'].startswith(huruf):
                        print(f"{kota['city_id']} - {kota['city_name']}")
                        found = True
                if not found:
                    print('Tidak ada kota yang diawali huruf tersebut.')
                input('\nTekan Enter untuk melanjutkan...')

            elif sub == '4':
                break

            else:
                input('Pilihan tidak valid, tekan Enter...')

    elif pilihan == '5':
        break

    else:
        input('Pilihan tidak valid, tekan Enter...')
