# 📦 Panduan Menjalankan Aplikasi Cek Ongkir (GUI Python + API RajaOngkir)

Aplikasi ini adalah antarmuka grafis (GUI) yang dibangun menggunakan Python Tkinter dan RajaOngkir API.  
Dengan aplikasi ini, pengguna bisa menghitung ongkos kirim berdasarkan kota asal, tujuan, berat, dan kurir (JNE, POS, TIKI).

---

## 🧰 Prasyarat

- Python 3.7 atau lebih baru
- Virtual Environment (opsional tapi disarankan)
- Koneksi internet aktif
- API Key dari [rajaongkir.com](https://rajaongkir.com)

---

## 📝 Langkah-Langkah Menjalankan Program

### 1. Download Folder Project

Unduh atau clone folder `API` ke komputer Anda. Folder ini bisa disimpan di mana saja, contoh: `C:\PROJEK\API`.

### 2. Buka Folder di VS Code

- Jalankan Visual Studio Code
- Klik **File > Open Folder...**, lalu pilih folder `API`
- Pastikan terminal berada di direktori project:
  - Klik kanan folder `API` → **Copy as Path**
  - Di terminal VS Code:
    ```bash
    cd "C:\PROJEK\API"
    ```

### 3. Aktifkan Virtual Environment

Misalnya, nama environment yang digunakan adalah `API`.

Aktifkan environment:
```bash
API\Scripts\activate
```

Jika berhasil, prompt akan berubah menjadi:
```bash
(API) PS C:\PROJEK\API>
```

### 4. Menyimpan API Key Secara Aman

Untuk menjaga privasi, **API Key** tidak lagi ditulis langsung di dalam kode.  
Gunakan file `apikey.json` di direktori project Anda.

1. Buat file baru bernama `apikey.json` di folder project.
2. Isi file tersebut dengan format berikut:
    ```json
    {
      "rajaongkir_api_key": "ISI_API_KEY_ANDA_DI_SINI"
    }
    ```
3. **Jangan upload atau membagikan file `apikey.json` ke publik atau repository.**

> **Catatan:**  
> File `cekongkir.py` sudah otomatis membaca API Key dari `apikey.json`.  
> Jika Anda ingin mencoba aplikasi ini, cukup dapatkan API Key dari [rajaongkir.com](https://rajaongkir.com) dan masukkan ke file tersebut.

### 5. Jalankan Aplikasi

File utama adalah `cekongkir.py` (versi final), atau `edit.py` (untuk versi yang bisa diedit).

Jalankan dengan:
```bash
py cekongkir.py
```

---

## 🧪 Folder Prototype

Berisi bagian eksperimen awal aplikasi, lokasi: `API\Project\Rajaongkir\Prototype\`

| File               | Deskripsi                                                   |
|--------------------|-------------------------------------------------------------|
| `hitapi_fungsi.py` | Contoh pemanggilan API dengan fungsi                        |
| `hitapi.py`        | Contoh pemanggilan API secara langsung                      |
| `ongkir.py`        | Request ongkir (cost) dengan parameter wajib                |
| `last_test.py`     | Versi pengujian akhir aplikasi                              |
 

---

---

## 🌐 Endpoint API RajaOngkir

Aplikasi ini menggunakan endpoint dari [RajaOngkir API](https://rajaongkir.com/dokumentasi).  
Berikut beberapa endpoint utama yang digunakan:

| Endpoint                | Keterangan                        |
|-------------------------|-----------------------------------|
| `/city`                 | Mendapatkan daftar kota           |
| `/cost`                 | Menghitung ongkos kirim           |
| `/province`             | Mendapatkan daftar provinsi       |
| `/subdistrict`*         | Mendapatkan daftar kecamatan (pro)|
| `/waybill`*             | Melacak resi pengiriman (pro)     |

> *Endpoint bertanda bintang hanya tersedia pada paket PRO.

Semua request API menggunakan metode **POST** atau **GET** sesuai dokumentasi RajaOngkir, dan membutuhkan API Key yang valid.

---

## 🛠 Dependencies

Install library yang dibutuhkan:
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

## ⚠️ Catatan Tambahan

- Simpan **API Key** Anda di file `apikey.json` (bukan di dalam kode).
- Jangan membagikan **API Key** ke publik.
- Pastikan koneksi internet aktif saat menjalankan aplikasi ini.

---

## ✨ Fitur Utama

### 🔄 Auto-load Kota Asal & Tujuan
- Aplikasi secara otomatis memuat daftar kota dari API RajaOngkir tanpa input manual.

### ⚖️ Cek Ongkir Akurat
- Menghitung ongkos kirim berdasarkan:
  - Kota asal
  - Kota tujuan
  - Berat kiriman (dalam gram)
  - Kurir: **JNE**, **POS**, **TIKI**

### 📋 Hasil Detail Pengiriman
- Menampilkan:
  - Nama layanan kurir
  - Deskripsi layanan
  - Biaya pengiriman
  - Estimasi waktu pengiriman (ETD)

### 🧭 Menu Bantuan & Tentang Aplikasi
- Menyediakan dokumentasi cara pakai dan informasi tentang tim pengembang.

### 🎨 Tampilan Modern & Responsif
- Antarmuka dibuat dengan tema menarik dari `ttkthemes` dan mendukung tampilan bersih dan user-friendly.

---

> Dibuat oleh: **Ahmad Nur Ikhsan