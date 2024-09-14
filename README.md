# Peonies Site
Welcome to Peonies Site, your one-stop shop for fresh, beautiful flowers!

[Peonies Site Website](https://rizki-amani-peoniessite.pbp.cs.ui.ac.id)

## Daftar Tugas:
- **[Tugas 2](#tugas-2)**<br>
- **[Tugas 3](#tugas-3)**<br>

## Tugas 2

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

1. **Membuat Proyek Django Baru:**
    - Membuat direktori baru yang sesuai dengan nama aplikasi, peonies-site
    - Aktifkan virtual environment
    - Buat proyek baru dengan perintah: `django-admin startproject`

2. **Membuat Aplikasi:**
    - Buat aplikasi baru dengan perintah `python3 manage.py startapp main`
    - Menamakannya dengan main sesuai perintah tugas

3. **Melakukan routing pada proyek:**
    - Tambahkan aplikasi `main` ke dalam `INSTALLED_APPS` di `settings.py` proyek:
     ```python
     INSTALLED_APPS = [
         ...
         'main',
     ]
     ```

    - Konfigurasikan routing dengan menambahkan `main.urls` ke `urls.py` proyek:
     ```python
     from django.contrib import admin
     from django.urls import path, include

     urlpatterns = [
         path('admin/', admin.site.urls),
         path('', include('main.urls')),
     ]
     ```
4. **Membuat Models:**
    - Mendefinisikan model pada `models.py` yang sesuai dengan aplikasi.
     ```python
    from django.db import models

    class Product(models.Model):
        BOUQUET_TYPE_CHOICES = [
            ('single', 'Single'),
            ('small', 'Small'),
            ('medium', 'Medium'),
            ('big', 'Big')
        ]

        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        bouquet_type = models.CharField(max_length=10, choices=BOUQUET_TYPE_CHOICES, default='single')  # Type of bouquet
        wrap_color = models.CharField(max_length=50, default='')  # Wrap color

        def __str__(self):
            return self.name
        
        @property
        def is_in_stock(self):
            return self.stock > 0
     ```
    - Jalankan migrasi untuk membuat tabel `Product` di database, menggunakan perintah `python manage.py makemigrations` dan `python manae.py migrate`

5. **Membuat Fungsi pada Views dan Template HTML:**
    - Tambahkan fungsi pada `views.py` di aplikasi `main`:
     ```python
    from django.shortcuts import render
    from .models import Product

    def product_list(request):
        context = {
            'name': 'Rizki Amani Hasanah',  
            'npm': '2306213376', 
            'class_name': 'PBP B',  
            'app_name': 'Peonies Site'
        }

        return render(request, 'main.html', context)
     ```
    - Lalu membuat html yang sesuai dengan keinginan

6. **Routing pada urls.py Aplikasi Main:**
   - Tambahkan konfigurasi routing pada `urls.py` aplikasi `main`:
     ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.product_list, name='main'),
    ]
     ```

7. **Deployment ke PWS:**
   - Gunakan `python manage.py runserver` untuk pengujian pada server lokal
   - Memasukkan url pws di `settings.py`, tepatnya ALLOWED_HOSTS
   - Deploy aplikasi ke platform hosting PWS 

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan](bagan.jpeg)

- **urls.py**: Mengarahkan URL dari client ke fungsi yang sesuai di `views.py`.
- **views.py**: Menangani logika bisnis dan memproses data, termasuk mengambil data dari model (jika diperlukan) dan mengirimkan ke template.
- **models.py**: Mengelola interaksi dengan database (misalnya, mengambil atau menyimpan data).
- **Template HTML**: Menyediakan format tampilan yang dikirimkan sebagai respon ke client.

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git adalah sistem kontrol versi terdistribusi yang memungkinkan pengembang untuk mengelola perubahan dalam kode sumber proyek perangkat lunak. Fungsinya meliputi melacak perubahan dengan menyimpan riwayat dalam repositori, sehingga bisa kembali ke versi sebelumnya jika diperlukan. Selain itu, Git memfasilitasi kolaborasi tim dengan mengelola perubahan yang dilakukan oleh beberapa pengembang secara bersamaan melalui cabang (branches) dan merge. Git juga berfungsi sebagai cadangan kode, memungkinkan pemulihan jika terjadi masalah dengan menyimpan salinan kode yang dikendalikan oleh sistem.

### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering dipilih sebagai framework pemula karena beberapa alasan:
- **Kemudahan Penggunaan:** Django memiliki dokumentasi yang lengkap dan komunitas yang aktif
- **Batteries Included:** Django menyediakan banyak fitur bawaan yang memudahkan pengembangan aplikasi web, seperti ORM, sistem autentikasi, dan admin interface.
- **Struktur yang Jelas:** Django mengikuti pola desain Model-View-Template (MVT) yang memisahkan logika aplikasi dari presentasi

### 5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena menyediakan cara untuk berinteraksi dengan database menggunakan objek Python daripada menulis query SQL secara langsung. ORM memungkinkan pemetaan antara kelas Python dan tabel database, membuat pengembangan lebih intuitif dan mengurangi kebutuhan untuk penulisan query SQL yang rumit.


## Tugas 3

### 1. Mengapa Kita Memerlukan Data Delivery dalam Pengimplementasian Sebuah Platform?
Data delivery diperlukan untuk mentransfer informasi antar sistem atau antar bagian dalam suatu platform, sehingga memungkinkan komunikasi yang efektif antara backend dan frontend atau antar aplikasi yang berbeda. Pada pengembangan suatu platform, data delivery akan memastikan bahwa informasi dapat "dipertukarkan" dengan cara yang terstruktur dan juga konsisten. Hal ini penting terutama dalam aplikasi yang membutuhkan integrasi berbagai komponen atau layanan, seperti API, supaya pengguna bisa menerima data yang relevan dengan cepat dan aman.

### 2. Menurutmu, Mana yang Lebih Baik antara XML dan JSON? Mengapa JSON Lebih Populer Dibandingkan XML?
Menurut aku, JSON lebih baik berdasarkan alasan yang aku pahami: 
- Mudah dibaca: JSON lebih ringkas dan lebih mudah dipahami oleh manusia dibandingkan XML yang memiliki tag yang lebih panjang.
- Dukungan di penggunaan bahasa pemrograman: JSON lebih mudah diintegrasikan di sebagian besar bahasa pemrograman modern, termasuk JavaScript dan Python, karena formatnya menyerupai struktur objek pada bahasa tersebut.
- Efisiensi: JSON lebih ringan dibandingkan XML dalam hal ukuran data yang dikirim, sehingga lebih cepat di jaringan dan lebih hemat bandwidth.

Dari apa yang aku baca, JSON lebih "populer" karena alasan-alasan di atas, terutama dalam konteks aplikasi web dan API modern di mana kecepatan dan efisiensi sangat penting. Namun, XML sendiri masih digunakan dalam aplikasi tertentu yang membutuhkan skema data yang lebih kompleks atau validasi yang ketat.

### 3. Jelaskan Fungsi dari Method is_valid() pada Form Django dan Mengapa Kita Membutuhkan Method Tersebut?
Method `is_valid()` pada form Django digunakan untuk memvalidasi data yang di-input oleh pengguna sebelum data tersebut diproses atau disimpan ke dalam database. Fungsi ini akan memeriksa apakah semua field yang diisikan sesuai dengan aturan yang telah ditentukan pada form, seperti validasi tipe data, batasan panjang karakter, dan apakah field tersebut wajib diisi atau tidak. Jika data valid, method ini akan mengembalikan nilai True, dan jika tidak valid, method ini akan mengembalikan nilai False serta menampilkan pesan kesalahan secara otomatis.

Alasan mengapa kita membutuhkan `is_valid()` adalah untuk memastikan bahwa data yang di-input pengguna sesuai dengan harapan, sehingga mencegah kesalahan atau kerusakan data pada database serta memberikan feedback yang tepat kepada pengguna jika terdapat kesalahan.

### 4. Mengapa Kita Membutuhkan csrf_token Saat Membuat Form di Django? Apa yang Dapat Terjadi Jika Kita Tidak Menambahkan csrf_token Pada Form Django? Bagaimana Hal Tersebut Dapat Dimanfaatkan oleh Penyerang?
`csrf_token` menjadi token keamanan yang digunakan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Saat membuat form di Django, csrf_token memastikan bahwa setiap request yang dikirim berasal dari pengguna yang sah dan tidak dimanipulasi oleh pihak ketiga. Jika implementasi tanpa csrf_token, penyerang dapat memanfaatkan celah ini untuk melakukan tindakan yang tidak sah (seperti mengirim form atau memodifikasi data).

Jika tidak menggunakan csrf_token, aplikasi menjadi rentan terhadap serangan CSRF, di mana penyerang dapat membuat pengguna mengirim request tanpa disadari. Hal ini dapat dimanfaatkan oleh penyerang untuk mengubah data, membuat transaksi palsu, atau bahkan menjalankan aksi berbahaya lainnya atas nama pengguna yang sah.

### 5. Jelaskan Bagaimana Cara Kamu Mengimplementasikan Checklist di Atas Secara Step-by-Step (Bukan Hanya Sekadar Mengikuti Tutorial)?
Berikut adalah langkah-langkah yang saya lakukan dalam mengimplementasikan checklist pada proyek ini:
1. **Implementasi Skeleton dan UUID:**
 Langkah ini memang tidak diwajibkan, namun saya tetap mengimplementasikan supaya bisa lebih terbiasa dan mendafaptakn benefit nya.

2. **Membuat Model:**
 Saya memulai dengan membuat model untuk menyimpan data yang diperlukan, dan saya namakan sebagai Product. Saya menentukan field apa saja yang dibutuhkan serta tipe datanya.

3. **Membuat Form**: 
 Selanjutnya, saya membuat form berbasis model (ModelForm) untuk menerima input pengguna terkait produk yang akan ditambahkan.

4. **Membuat Views:**
 Saya menambahkan fungsi view yang meng-handle form, menggunakan method `is_valid()` untuk memvalidasi data yang masuk. Jika data valid, saya menyimpan data tersebut ke dalam database dan melakukan redirect ke halaman utama.

5. **Menambahkan URL Patterns:**
 Saya menambahkan URL pattern untuk menghubungkan view dengan URL yang spesifik, sehingga pengguna dapat mengakses form dan mengirim data.

6. **Membuat Template:**
 Saya membuat file HTML untuk menampilkan form dan data yang telah diinput pengguna dalam bentuk tabel, serta memastikan penggunaan csrf_token untuk keamanan.
7. **Testing:**
 Terakhir, saya menguji seluruh fitur yang telah dibuat, seperti menambah produk baru, menampilkan produk yang telah di-input, dan memvalidasi form, untuk memastikan semua berjalan sesuai harapan.
    
### Bukti Postman
![Postman XML](PostmanXML.png)
![Postman JSON](PostmanJSON.png)
![Postman with ID](PostmanwithID.png)
