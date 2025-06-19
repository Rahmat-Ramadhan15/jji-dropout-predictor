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

  ![Student Status Distribution](https://github.com/Rahmat-Ramadhan15/jji-dropout-predictor/blob/1a20a8a0fcda74cb3e05cfff7f502fd5e77fc6a4/assets/student-status-distribution.png)

  Interpretasi: Mayoritas mahasiswa berhasil lulus, tetapi sekitar 1/3 mengalami dropout, dan sisanya masih aktif belajar.

2. Dropout Rate dan Graduate Rate
   
- Dropout Rate: 32,120% (kemungkinan ada kesalahan format, seharusnya 32.12%)

  ![Dropout Rate](https://github.com/Rahmat-Ramadhan15/jji-dropout-predictor/blob/1a20a8a0fcda74cb3e05cfff7f502fd5e77fc6a4/assets/do-rate.png)
- Graduate Rate: 49,930% (kemungkinan seharusnya 49.93%)

  ![Graduation Rate](https://github.com/Rahmat-Ramadhan15/jji-dropout-predictor/blob/1a20a8a0fcda74cb3e05cfff7f502fd5e77fc6a4/assets/gr-rate.png)

  Catatan: Angka ini merepresentasikan persentase mahasiswa yang dropout dan yang lulus dari seluruh populasi mahasiswa.

3. Graduate vs Dropout
   
Fokus pada mahasiswa yang sudah tidak aktif (tidak dalam status Enrolled).

Total data: 3.630 mahasiswa
- Gr (Graduate): 61%
- Do (Dropout): 39%

  ![Graduate vs Dropout](https://github.com/Rahmat-Ramadhan15/jji-dropout-predictor/blob/1a20a8a0fcda74cb3e05cfff7f502fd5e77fc6a4/assets/gr-vs-do.png)

  Interpretasi: Dari mahasiswa yang sudah menyelesaikan atau berhenti studi, 61% lulus dan 39% mengalami dropout.

4.  Feature Importance Top 10
   
Bagian ini menampilkan 10 fitur terpenting yang paling memengaruhi prediksi model terhadap status mahasiswa (dropout atau lulus).
Visualisasi ini menggunakan grafik horizontal bar dan menggambarkan tingkat importance setiap fitur dalam model machine learning.

Fitur paling penting:
- Curricular_units_2nd_sem_approved → jumlah mata kuliah semester 2 yang disetujui sangat berpengaruh pada prediksi.
- Curricular_units_1st_sem_approved dan Curricular_units_2nd_sem_grade → performa akademik di semester awal sangat menentukan.
- Faktor lainnya seperti Tuition_fees_up_to_date dan Scholarship_holder juga signifikan, menunjukkan bahwa faktor finansial turut berdampak.

  ![Feature Importance Top 10](https://github.com/Rahmat-Ramadhan15/jji-dropout-predictor/blob/1a20a8a0fcda74cb3e05cfff7f502fd5e77fc6a4/assets/faeture-omportance-top10.png)

5. Distribution of Approved 2nd Semester Courses by Status
   
Visualisasi ini menunjukkan distribusi jumlah mata kuliah semester 2 yang disetujui (Curricular_units_2nd_sem_approved) dibedakan berdasarkan status akhir mahasiswa: Dropout atau Graduate.

- Mahasiswa Graduate secara signifikan memiliki lebih banyak mata kuliah yang disetujui di semester 2 dibandingkan mahasiswa Dropout.

- Artinya, semakin banyak mata kuliah yang diselesaikan dengan baik di semester 2, semakin besar kemungkinan mahasiswa akan lulus.

  ![Distribution of Approved 2nd Semester Courses by Status](https://github.com/Rahmat-Ramadhan15/jji-dropout-predictor/blob/1a20a8a0fcda74cb3e05cfff7f502fd5e77fc6a4/assets/s1.png)

6. Distribution of Approved 1st Semester Courses by Status
   
Sama seperti grafik sebelumnya, namun untuk semester 1 (Curricular_units_1st_sem_approved).
- Mahasiswa yang Graduate juga jauh lebih banyak menyelesaikan mata kuliah semester 1 dibanding yang Dropout.
- Menunjukkan bahwa kinerja akademik sejak semester awal menjadi indikator penting terhadap kelulusan.

  ![Distribution of Approved 1st Semester Courses by Status](https://github.com/Rahmat-Ramadhan15/jji-dropout-predictor/blob/1a20a8a0fcda74cb3e05cfff7f502fd5e77fc6a4/assets/s2.png)

## Menjalankan Sistem Machine Learning
1. Cara Menjalankan file app.py. Setelah virtual environment diaktifkan dan semua dependensi terinstal, maka dapat menggunakan perintah berikut.
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

2. Masukkan data-data yang diperlukan di antarmuka streamlit untuk mendapatkan hasil prediksi status (dropout atau graduate).

   ![UI1](https://github.com/Rahmat-Ramadhan15/jji-dropout-predictor/blob/1a20a8a0fcda74cb3e05cfff7f502fd5e77fc6a4/assets/ui1.png)
   
   ![UI2](https://github.com/Rahmat-Ramadhan15/jji-dropout-predictor/blob/1a20a8a0fcda74cb3e05cfff7f502fd5e77fc6a4/assets/ui2.png)

## Conclusion
Proyek ini berhasil membangun sistem prediksi risiko dropout mahasiswa berbasis data akademik, demografis, dan finansial. Dengan memanfaatkan algoritma machine learning dan visualisasi interaktif melalui dashboard Metabase, institusi pendidikan seperti Jaya Jaya Institut kini dapat:

1. Mengidentifikasi mahasiswa yang berisiko tinggi mengalami dropout secara lebih dini.
2. Mengetahui faktor-faktor utama yang memengaruhi dropout, seperti performa akademik di semester awal, keterlambatan pembayaran biaya kuliah, dan status beasiswa.
3. Memantau kondisi dan tren dropout mahasiswa secara real-time melalui dashboard interaktif.
4. Mengoptimalkan pengambilan keputusan dan alokasi sumber daya untuk intervensi yang lebih tepat sasaran.

Dengan adanya sistem prediktif ini, diharapkan pihak kampus dapat mengambil langkah-langkah strategis untuk menekan angka dropout dan meningkatkan angka kelulusan mahasiswa.

### Rekomendasi Action Items
Berikut adalah beberapa rekomendasi tindakan yang dapat dilakukan oleh pihak institusi berdasarkan hasil analisis dan sistem yang telah dibangun:

1. Implementasi Sistem Peringatan Dini (Early Warning System)
- Gunakan model prediktif ini secara berkala (misal setiap akhir semester) untuk mendeteksi mahasiswa yang berisiko dropout.
- Kirimkan laporan ke dosen wali atau bagian akademik untuk segera dilakukan intervensi seperti konseling atau pendampingan belajar.

2. Fokus pada Mahasiswa dengan Performa Rendah di Semester Awal
- Berdasarkan analisis, performa di semester 1 dan 2 sangat memengaruhi kemungkinan dropout.
- Berikan program remedial, kelas tambahan, atau mentoring kepada mahasiswa dengan nilai rendah atau banyak mata kuliah tidak lulus di semester awal.

3. Pemantauan dan Dukungan Finansial
- Mahasiswa yang menunggak biaya kuliah dan tidak memiliki beasiswa menunjukkan risiko dropout yang lebih tinggi.
- Lakukan pendekatan personal atau sediakan skema keringanan pembayaran bagi mahasiswa yang kesulitan finansial.

4. Evaluasi dan Optimalisasi Beasiswa
- Perluasan akses beasiswa berpotensi menurunkan dropout, karena mahasiswa penerima beasiswa cenderung memiliki risiko dropout lebih rendah.
- Jadikan status beasiswa sebagai salah satu indikator intervensi preventif.

5. Integrasi Sistem Prediksi ke Portal Akademik
- Integrasikan model prediksi ke sistem informasi akademik (SIAKAD) sehingga pihak kampus dapat memantau status risiko setiap mahasiswa secara langsung.

6. Evaluasi Kurikulum Semester Awal
- Jika banyak mahasiswa gagal atau kesulitan di semester awal, bisa jadi kurikulum terlalu berat. Lakukan evaluasi terhadap metode pengajaran, sistem evaluasi, dan beban mata kuliah.


