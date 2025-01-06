# PROJECT UAS


## PROGRAM KASIR SEDERHANA


### Step 1 : CLASS DATA

#### CLASS BARANG

Class Barang merupakan representasi dari barang yang tersedia untuk dijual. 
Class ini memiliki tiga atribut utama, yaitu:

- kode: sebuah string yang menjadi kode unik untuk setiap barang.
- nama: string yang mendeskripsikan nama barang.
- harga: sebuah integer yang menunjukkan harga barang dalam satuan mata uang.

Method __init__ digunakan untuk menginisialisasi ketiga atribut tersebut. Sementara itu, method __str__ memberikan representasi string dari objek Barang untuk menampilkan informasi barang dalam format kode | nama | harga.

<img width="395" alt="image" src="https://github.com/user-attachments/assets/3a79ea49-5464-4455-b968-fb54d90f8038" />


#### CLASS KERANJANG

Class Keranjang bertanggung jawab untuk mengelola daftar barang yang dimasukkan pengguna ke keranjang belanja. Class ini memiliki atribut barang_list, sebuah list yang menyimpan barang yang telah ditambahkan beserta jumlahnya. Berikut adalah metode pentingnya:

- tambah_barang: Menambahkan barang ke keranjang. Jika barang sudah ada di keranjang, jumlah barang akan diperbarui.
- hitung_total: Menghitung total harga semua barang dalam keranjang dengan mengalikan harga per item dengan jumlahnya.
- cetak_struk: Menampilkan daftar barang yang dibeli beserta total harganya dalam bentuk struk belanja.

Class ini bertindak sebagai representasi proses bisnis untuk menangani transaksi.

<img width="477" alt="image" src="https://github.com/user-attachments/assets/3bb25da5-6d06-40da-972e-fb7faa177ab7" />

### Step 2 : CLASS VIEW

#### FUNGSI tampilkan_menu

Fungsi tampilkan_menu bertugas untuk menampilkan daftar barang yang tersedia. Fungsi ini menerima parameter barang_list, yang merupakan daftar semua barang dari class Barang. Setiap barang akan ditampilkan dalam format tabel dengan kolom Kode, Nama, dan Harga. Fungsi ini bertindak sebagai antarmuka untuk pengguna agar dapat melihat barang yang tersedia sebelum memilih.

<img width="542" alt="image" src="https://github.com/user-attachments/assets/8c8f7846-5e61-4417-997f-f7ee2856ae15" />


#### FUNGSI keranjang_view

Fungsi dalam keranjang_view.py

- tampilkan_keranjang: Fungsi ini digunakan untuk menampilkan daftar barang yang ada di keranjang. Fungsi ini menerima parameter berupa objek Keranjang dan mencetak daftar barang yang telah dimasukkan.
- tampilkan_total: Fungsi ini digunakan untuk menampilkan total harga barang yang ada di keranjang. Fungsi ini memanggil method hitung_total dari class Keranjang untuk mendapatkan total harga.

Kedua fungsi ini berperan sebagai antarmuka untuk memberikan informasi tentang isi keranjang kepada pengguna.

<img width="357" alt="image" src="https://github.com/user-attachments/assets/d2c6e8fc-3007-4e95-acf9-865b20cd3805" />

### Step 3 : CLASS PROCESS

- Fungsi proses_pilih_barang
Fungsi ini menangani proses pemilihan barang oleh pengguna. Fungsi menerima input kode barang dari pengguna, kemudian mencocokkannya dengan daftar barang yang tersedia. Jika kode barang ditemukan, barang yang sesuai akan dikembalikan. Jika tidak, pengguna akan diminta untuk memasukkan kode ulang sampai barang yang valid dipilih, atau mereka dapat memasukkan exit untuk keluar.

![code](https://github.com/user-attachments/assets/985db5d9-a42a-426b-8d2a-932eb0757f3e)

- Fungsi proses_tambah_ke_keranjang
Fungsi ini menangani proses penambahan barang ke keranjang. Setelah pengguna memilih barang, mereka diminta untuk memasukkan jumlah barang yang ingin dibeli. Fungsi ini memvalidasi input jumlah agar tidak negatif atau nol, serta memeriksa apakah input yang dimasukkan valid sebagai bilangan bulat. Jika valid, barang beserta jumlahnya ditambahkan ke keranjang menggunakan method tambah_barang.

![code2](https://github.com/user-attachments/assets/9619ce29-6dd3-4c05-a3c0-30278a067694)

- Fungsi main
Fungsi ini adalah inti program yang mengatur alur utama aplikasi. Dimulai dengan membuat daftar barang menggunakan objek dari class Barang, lalu menginisialisasi keranjang menggunakan objek Keranjang. Program berjalan dalam loop yang menampilkan menu, memungkinkan pengguna memilih barang, memasukkannya ke keranjang, dan memutuskan apakah ingin melanjutkan atau keluar. Setelah pengguna selesai, keranjang ditampilkan, total harga dihitung, dan struk belanja dicetak.

<img width="257" alt="image" src="https://github.com/user-attachments/assets/48a58e92-6f0e-4461-89a5-5247b4b9ed6e" />

Alur Utama Program
1. Program dimulai dengan memanggil fungsi main.
2. Daftar barang ditampilkan kepada pengguna melalui fungsi tampilkan_menu.
3. Pengguna memilih barang dengan memasukkan kode melalui fungsi proses_pilih_barang.
4. Setelah barang dipilih, pengguna memasukkan jumlah barang yang ingin dibeli melalui fungsi proses_tambah_ke_keranjang.
5. Proses berulang sampai pengguna memutuskan untuk tidak menambahkan barang lagi.
6. Program menampilkan isi keranjang, menghitung total harga, dan mencetak struk belanja.

### Step 4 : RUNNING PROGRAM

Langkah terakhir yaitu pengujian code program, kita mencoba dengan menambahkan code 0012 dengan kuantitas 1 saja sebagai daftar barang ke keranjang, jika program meminta user untuk menginputkan perinta ingin menambahkan barang atau sudah selesai, maka kita coba menambahkan dengan 'y' sebagai perintahnya.

![Screenshot 2025-01-06 150203](https://github.com/user-attachments/assets/a3cb6eaf-8a35-4ddb-a9b6-051a9a5a6d62)

Lalu, kita akan coba menambahkan code 0020 dengan kuantitas 1, dan program akan menanyakan kembali kepada user, jika user perintahkan 'n' maka program akan menampilkan hitungan total berupa struk belanja/barang.

<img width="434" alt="image" src="https://github.com/user-attachments/assets/7ed64995-f46b-4052-9988-93699b686e29" />

## LINK YOUTUBE

( )
