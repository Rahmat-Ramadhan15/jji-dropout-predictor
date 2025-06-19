# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi yang menghadapi tingkat dropout mahasiswa yang cukup tinggi. Hal ini menjadi perhatian serius karena berdampak pada reputasi institusi, akreditasi program studi, serta efisiensi operasional dan finansial. Dengan demikian, dibutuhkan solusi prediktif berbasis data untuk mendeteksi potensi mahasiswa dropout agar tindakan preventif seperti bimbingan atau dukungan tambahan dapat segera dilakukan.

### Permasalahan Bisnis
1. Tingginya tingkat dropout mahasiswa setiap semester: Banyak mahasiswa yang keluar dari kampus setiap semester tanpa penyebab yang terpantau sejak dini. Proyek ini mencoba mengidentifikasi pola-pola umum dari mahasiswa yang berisiko tinggi untuk DO (dropout) berdasarkan data akademik, demografi, dan ekonomi.
2. Tidak adanya sistem prediksi untuk mendeteksi mahasiswa yang berisiko tinggi mengalami dropout: Saat ini, institusi belum memiliki alat bantu berbasis machine learning yang dapat memberikan peringatan dini terhadap mahasiswa yang berpotensi mengalami dropout. Sistem ini akan menjadi solusi tersebut.
3. Sulitnya memantau performa mahasiswa secara efisien: Dengan banyaknya jumlah mahasiswa, sulit bagi pihak kampus untuk memantau perkembangan tiap individu secara manual. Sistem prediksi ini akan membantu memprioritaskan perhatian pada mahasiswa yang membutuhkan intervensi lebih awal.

### Cakupan Proyek
1. Melakukan eksplorasi dan pembersihan data.
2. Mengembangkan model machine learning untuk memprediksi kemungkinan mahasiswa dropout.
3. Membangun business dashboard interaktif untuk memantau performa dan risiko mahasiswa.
4. Mengimplementasikan sistem inferensi sederhana berbasis antarmuka pengguna.

### Persiapan

Sumber data: [https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:

Proyek ini dikembangkan menggunakan Python dan disarankan untuk dijalankan dalam lingkungan virtual (virtual environment) untuk mengelola dependensi secara terisolasi.

Membuat dan Mengaktifkan Virtual Environment (venv) Buka terminal atau command prompt, lalu ikuti langkah-langkah berikut:

1. Buka terminal atau PowerShell.
2. Jalankan perintah berikut.
    ```
     conda create --name prediksi_dropout python=3.12
    ```
3. Aktifkan virtual environment dengan menjalankan perintah berikut.
    ```
    conda activate prediksi_dropout
    ```
4. Menginstal Dependensi dari requirements.txt Pastikan telah mengaktifkan virtual environment.
    ```
    pip install -r requirements.txt
    ```

## Business Dashboard
Email dan password Metabase

Email: root@mail.com

Password: root123

### Student Dropout Monitoring
Dashboard ini dirancang untuk memberikan wawasan strategis mengenai fenomena dropout mahasiswa di institusi pendidikan tinggi. Melalui visualisasi data interaktif yang dibangun menggunakan Metabase dan terkoneksi ke database PostgreSQL melalui Docker, dashboard ini menyajikan analisis menyeluruh terhadap faktor-faktor utama yang memengaruhi kemungkinan mahasiswa mengalami dropout.

1. Student Status Distribution
Menampilkan distribusi keseluruhan 4.424 mahasiswa berdasarkan status akademik:
- Gr (Graduate): 50% → Mahasiswa yang telah lulus.
- Do (Dropout): 32% → Mahasiswa yang mengalami dropout.
- Er (Enrolled atau masih aktif): 18% → Mahasiswa yang masih terdaftar dan belum menyelesaikan studi.

  ![Student Status Distribution]([assets/dashboard-prediksi.png](https://github.com/Rahmat-Ramadhan15/jji-dropout-predictor/blob/1a20a8a0fcda74cb3e05cfff7f502fd5e77fc6a4/assets/student-status-distribution.png))

  Interpretasi: Mayoritas mahasiswa berhasil lulus, tetapi sekitar 1/3 mengalami dropout, dan sisanya masih aktif belajar.

## Menjalankan Sistem Machine Learning
Cara Menjalankan file app.py. Setelah virtual environment diaktifkan dan semua dependensi terinstal, maka dapat menggunakan perintah berikut.
  ```
  streamlit run app.py
  ```
  Secara default, Streamlit akan menjalankan aplikasi di alamat berikut:
   
  http://localhost:8501
   
  Namun, jika port 8501 sedang digunakan oleh aplikasi lain, Streamlit akan secara otomatis beralih ke port lain seperti 8502, 8503, dan seterusnya.
   
  Untuk menjalankan aplikasi pada port tertentu secara manual, Anda dapat menggunakan perintah:
  ```
  streamlit run app.py --server.port 8501
  ```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
