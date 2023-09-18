# Link Domain :
- [Aplikasi Adaptable](https://tedskinventory.adaptable.app)
- [Domain PBP CSUI](theodoore-kasyfillah-tedskinventory.pbp.cs.ui.ac.id)

# TUGAS 2
## Langkah-Langkah untuk Mengerjakan Tugas 2
1. Buat Repo di local sama github dengan nama proyek (nama project saya = tedskinventory)
2. Buka CMD dari repo localnya
3. Inisialisasi git dulu di reponya trus verifikasi akun github
4. Inisialiasi Virtual Environment yang akan digunakan
5. Inisialisasi django dengan install requirements yang diperlukan seperti django untuk membuat aplikasinya dan requirements lain seperti Psycopg2-binary yang berguna nantinya untuk database postgreSQL yang kita pilih saat deployment nanti
6. Kemudian mulai proyeknya dengan memberi command (django-admin startproject tedskinventory) biar nanti akan dibuat file projek didalam repo kita
7. Kemudian karena django udah diinisialisasi kita bisa mulai ngebikin aplikasinya
8. Untuk inisialisai si aplikasinya pertama kita start projectnya dlu dengan command (python manage.py startapp main) untuk membuat sebuah project files bernama main
9. Kemudian kita isi si aplikasi main tersebut dengan folder templates yang nanti isinya adalah file html yang bisa kita kostumisasi sebagai template aplikasi kita dengan style sesuka kita
10. Konfigurasi urls.py pada folder proyek untuk melakukan routing dengan memberikan command path('main/', include('main.urls')) dengan tujuan memastikan bahwa ketika kita mengakses URL ke main, fungsi yang sesuai akan dijalankan.
11. Kemudian di main kita bakal konfigurasi data yang diperlukan di aplikasi kita nanti
12. Isi models.py dengan tipe data yang kita perlukan sebagai contoh saya menggunakan 5 atribut, yaitu: 
    name = models.CharField(max_length=255) (untuk mengisi nama dari item yang saya masukkan kedalam aplikasi saya nantinya, menggunakan tipe data charfield namun saya beri batasan untuk banyak karakternya sebanyak 255 karakter, alasan saya tidak menggunakan textfield adalah karena tidak perlu menggunakan banyak character)
    image = models.ImageField(upload_to='products/', null=True, blank=True)(untuk mengisi gambar dari item, menggunakan tipe data imagefields dan memprosesnya menggunakan sebuah library dari python yang bernama pillow)
    price = models.CharField(max_length=255)(untuk mengisi harga dari item yang saya masukkan kedalam aplikasi saya nantinya, menggunakan tipe data charfield namun saya beri batasan untuk banyak karakternya sebanyak 255 karakter, alasan saya tidak menggunakan textfield adalah karena tidak perlu menggunakan banyak character dan saya tidak menggunakan integerfield karena ada string Rp pada bagian tersebut)
    description = models.TextField()(untuk mengisi deskripsi dari item, menggunakan tipe data TextFields agar bisa memuat string lebih banyak)
    amount = models.IntegerField()(untuk mengisi berapa jumlah stok yang tersedia dari item, menggunakan tipe data IntegerFields)
13. Isi context pada views.py dengan isian sesuai dengan atribut yang diperlukan dari template untuk dirender ke file main.html dengan fungsi show_main.
14. setelah mengisi template,models,dan views. kita lakukan routing pada folder main untuk memastikan bahwa permintaan ke URL main akan ditangani oleh fungsi show_main.
15. Setelah itu kita akan melakukan testing local
16. jika testing berhasil kia akan push projek kita ke repo github yang sudah kita hubungkan sebelumnya
17. Setelah berhasil dipush ke github kita akan melakukan deployment ke adaptable dengan memilih repo yang kita gunakan untuk proyek kali ini dengan deployment, database, dan server http wsgi yang sudah kita install pada saat inisialiasi yang terletak pada requirements.txt
18. Setelah deployment berjalan dengan lancar kita dapat mengecek domain aplikasi main yang sudah kita deploy

## Bagan Penjelasan
Berikut adalah bagan penjelasan yang berisikan request client dan kaitan antara urls.py, views.py, models.py, dan berkas html.
![BAGAN_PENJELASAN](Bagan.png)

## Mengapa Menggunakan Virtual Environment?
Mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
=> Kita menggunakan virtual environment dalam pengembangan Django supaya workspace kita lebih terorganisir untuk masing masing proyek. Virtual Environment berperan juga supaya tidak terjadi masalah seperti tabrakan versi dan juga berguna untuk menjaga dependensi jadi lebih teratur . Sebenarnya kita bisa saja kita membuat Aplikasi tanpa virtual environment, tetapi disarankan untuk menggunakannya agar proyek-proyek kita lebih terorganisir.

## Penjelasan Mengenai MVC, MVT, dan MVVM
Berikut adalah penjelasan tentang MVC, MVT, dan MVVM:
MVC (Model-View-Controller): MVC adalah konsep arsitektur aplikasi yang umum digunakan untuk mengimplementasikan UI, data, dan controller. konsep ini menekankan pemisahan antara logika bisnis aplikasi dan tampilan. Pemisahan ini memberikan pembagian kerja yang lebih baik dan pemeliharaan yang lebih baik.

MVT (Model View Template): MVT adalah konsep arsitektur  aplikasi yang terdiri dari tiga komponen: Model, View, dan Template. Model menangani informasi , View menampilkan data, dan Template mendefinisikan tata letak halaman web. Meskipun mirip dengan MVC, MVT memiliki perbedaan dalam cara kerjanya.

MVVM (Model-View-ViewModel): MVVM adalah konsep arsitektur  dalam aplikasi komputer yang memfasilitasi pemisahan pengembangan GUI dari pengembangan logika bisnis atau logika back-end (model) sehingga tampilan tidak bergantung pada platform model tertentu. ViewModel bertindak sebagai konverter nilai, yang bertanggung jawab untuk mengonversi objek data dari model sedemikian rupa sehingga dapat dengan mudah dikelola dan disajikan.

Perbedaan utama antara ketiganya adalah komponen yang digunakan dalam arsitektur tersebut. MVC memisahkan aplikasi menjadi Model, View, dan Controller, dengan komunikasi antara mereka melalui pengamatan dan pengontrolan. Di sisi lain, MVT, yang umumnya digunakan dalam kerangka kerja web Django, memiliki komponen Template tambahan yang mengatur tampilan halaman web. Sementara itu, MVVM memisahkan aplikasi menjadi Model, View, dan ViewModel, dengan ViewModel berperan sebagai perantara antara Model dan View, memungkinkan pemisahan yang lebih jelas antara tampilan dan logika aplikasi. Setiap konsep ini memiliki karakteristiknya sendiri dan digunakan sesuai kebutuhan proyek dan teknologi yang digunakan.

## Referensi Tugas 2:
https://code.visualstudio.com/docs/python/tutorial-django
https://stackoverflow.com/questions/62181396/django-does-the-virtual-environment-have-to-be-on-every-time-i-develop-my-djang
https://developer.mozilla.org/en-US/docs/Glossary/MVC
https://www.javatpoint.com/django-mvt
https://learn.microsoft.com/en-us/dotnet/architecture/maui/mvvm

# TUGAS 3
## Apa perbedaan antara form POST dan form GET dalam Django?
Dalam Django, form POST dan form GET mengacu pada dua metode HTTP yang berbeda yang digunakan dalam pengiriman data dari form.

Metode GET digunakan untuk meminta data dari server. Dalam konteks form, data yang dihasilkan dari form akan ditambahkan ke URL dalam bentuk query string. Namun, karena data tersebut ditampilkan di URL, metode GET sebaiknya tidak digunakan untuk mengirim data sensitif seperti password. Selain itu, karena keterbatasan panjang URL, metode GET mungkin tidak cocok untuk mengirim data yang besar 

Sebaliknya, metode POST digunakan untuk mengirim data ke server. Data yang dihasilkan dari form dikirim sebagai bagian dari body request, bukan sebagai bagian dari URL. Oleh karena itu, metode POST lebih aman dan dapat digunakan untuk mengirim data sensitif serta data yang besar. Dalam Django, data yang dikirim melalui metode POST biasanya diakses melalui atribut request.POST 

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML, JSON, dan HTML adalah tiga format data yang berbeda yang sering digunakan dalam pengiriman data di web.
HTML (HyperText Markup Language) adalah bahasa markup yang digunakan untuk membuat struktur dan tampilan halaman web. HTML bukan format yang ideal untuk pengiriman data antara aplikasi karena strukturnya yang kompleks dan berorientasi tampilan 
XML (eXtensible Markup Language) adalah bahasa markup yang digunakan untuk menyimpan dan mengangkut data. XML mendukung struktur data yang kompleks dan dapat mendefinisikan skema sendiri. Namun, XML cenderung lebih verbose dan rumit dibandingkan dengan JSON 
JSON (JavaScript Object Notation) adalah format yang digunakan untuk menyimpan dan mengangkut data. JSON lebih ringan dan lebih mudah dibaca dan ditulis oleh manusia dibandingkan dengan XML. JSON juga mudah untuk di-parse dan di-generate oleh mesin. Oleh karena itu, JSON sering menjadi pilihan yang disukai untuk pertukaran data antara aplikasi web.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena beberapa alasan:
Ringan dan Efisien: JSON memiliki sintaks yang lebih sederhana dan lebih ringan dibandingkan dengan format lain seperti XML. Hal ini membuatnya lebih efisien dalam hal bandwidth dan waktu parsing.
Mudah dibaca dan ditulis: Baik oleh manusia maupun mesin, membuat JSON ideal untuk pengembangan dan debugging.
Dukungan Luas: Hampir semua bahasa pemrograman modern memiliki dukungan bawaan untuk parsing dan menghasilkan JSON.
Kompatibilitas dengan JavaScript: JSON dapat di-parse dengan mudah oleh JavaScript, bahasa yang digunakan di hampir semua aplikasi web modern. Dengan demikian, JSON menjadi pilihan alami untuk pertukaran data antara client dan server dalam aplikasi web 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Cara Saya Mengimplementasikan Checklist
1. Membuat forms.py dengan fields dari forms berasal dari products yang dideklarasikan pada class Product models.py
2. Jika ingin menambahkan indikator kita bisa migrate dulu
3. Buat Fungsi baru di views bernama create_product untuk merender tampilan dari forms pada sebuah template html
4. Buat file html sebagai template dari forms yang dirender oleh fungsi create_product
5. Buat sebuah button pada main html yang akan redirect kepada page yang berisikan forms untuk menambahkan product
6. Setelah membuat fungsi untuk melihat dalam bentuk HTML kita akan membuat 4 fungsi lain yaitu XML,XMLByID, JSON, JSONByID
7. Untuk membuat fungsi untuk melihat dalam XML dan JSON kita harus membuat fungsi dengan serializers untuk mentranslate data pada database kita kepada format XML atau JSON
8. Untuk membuat fungsi untuk melihat dalam XML dan JSON per ID kita harus membuat fungsi yang sama seperti pada saat membuat fungsi untuk melihat XML dan JSON seperti langkah 7, tetapi kita harus menerapkan filter terhadap pk(primary key) dari data yang disimpan dari database untuk ID dari data yang kita ingin akses
9. Setelah membuat 5 fungsi tersebut kita dapat melakukan routing dengan menambahkan url dari masing masing fungsi yang ingin kita terapkan pada urls py
10. Setelah melakukan routing kita dapat mengecek masing2 fungsi tersebut pada localhost kita

## Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md
### HASIL AKSES URL PADA POSTMAN
#### Postman HTML
![Hasil Screenshot POSTMAN HTML](PostmanHTML.png)

#### Postman XML
![Hasil Screenshot POSTMAN XML](PostmanXML.png)

#### Postman XML By ID
![Hasil Screenshot Postman XML By ID](PostmanXMLByID.png)

#### Postman JSON
![Hasil Screenshot Postman JSON](PostmanJSON.png)

#### Postman JSON By ID 
![Hasil Screenshot Postman JSON By ID](PostmanJSONByID.png)

## Referensi Tugas 3
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction