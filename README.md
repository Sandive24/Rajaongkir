# 📦 Panduan Aplikasi Cek Ongkir (GUI Python + API RajaOngkir)

Aplikasi GUI berbasis Python (Tkinter) untuk menghitung ongkos kirim berdasarkan kota asal, tujuan, berat, dan kurir (JNE, POS, TIKI) menggunakan API dari RajaOngkir.

---

## 🧰 Prasyarat

* Python 3.7 atau lebih baru
* Virtual environment (disarankan)
* Koneksi internet aktif
* API Key dari [rajaongkir.com](https://rajaongkir.com)

---

## 🚀 Langkah Menjalankan Program

### 1. Unduh & Buka Project

* Clone/download folder `API`, contoh lokasi: `C:\PROJEK\API`
* Buka di VS Code:

  ```bash
  cd "C:\PROJEK\API"
  ```

### 2. Aktifkan Virtual Environment

```bash
API\Scripts\activate
```

Jika berhasil:

```bash
(API) PS C:\PROJEK\API>
```

### 3. Simpan API Key dengan Aman

1. Buat file `apikey.json`:

   ```json
   {
     "rajaongkir_api_key": "ISI_API_KEY_ANDA"
   }
   ```
2. Jangan upload file ini ke publik/repository

> Script sudah otomatis membaca API key dari file ini.

### 4. Jalankan Aplikasi

```bash
py cekongkir.py
```

---

## 🧪 Folder Prototype (Opsional)

Lokasi: `API\Project\Rajaongkir\Prototype\`

| File               | Fungsi                           |
| ------------------ | -------------------------------- |
| `hitapi.py`        | Contoh API call langsung         |
| `hitapi_fungsi.py` | Versi fungsi API call            |
| `ongkir.py`        | Request biaya ongkir (`/cost`)   |
| `last_test.py`     | Uji coba tampilan akhir aplikasi |

---

## 🌐 Endpoint API yang Digunakan

| Endpoint       | Deskripsi                   |
| -------------- | --------------------------- |
| `/city`        | Mendapatkan daftar kota     |
| `/cost`        | Menghitung biaya kirim      |
| `/province`    | Mendapatkan daftar provinsi |
| `/subdistrict` | (PRO) Daftar kecamatan      |
| `/waybill`     | (PRO) Cek resi pengiriman   |

> \*Endpoint bertanda PRO hanya tersedia pada akun premium.

---

## 🛠️ Instalasi Dependencies

```bash
pip install -r requirements.txt
```

Isi `requirements.txt`:

```
requests==2.32.3
ttkthemes==3.2.2
screeninfo==0.8.1
```

---

## ✨ Fitur Utama

### 🔄 Auto-Load Kota

* Secara otomatis menampilkan daftar kota asal & tujuan dari API

### ⚖️ Cek Ongkir Akurat

* Berdasarkan kota asal, tujuan, berat (gram), dan kurir (JNE, POS, TIKI)

### 📋 Hasil Detail

* Menampilkan nama layanan, biaya kirim, dan estimasi waktu (ETD)

### 🧭 Menu Bantuan & Tentang

* Fitur informasi & petunjuk penggunaan

### 🎨 Antarmuka Modern

* Menggunakan `ttkthemes` untuk tampilan bersih & responsif

---

## ⚠️ Catatan Penting

* Jangan membuka Excel/API Key di editor saat aplikasi berjalan
* File `apikey.json` **harus disimpan lokal & bersifat pribadi**
* Butuh koneksi internet aktif saat menjalankan program

---

*Dibuat oleh: **Ahmad Nur Ikhsan***