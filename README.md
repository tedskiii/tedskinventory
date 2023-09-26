# TUGAS PBP Theodore Kasyfillah

<details>
<summary>TUGAS 2</summary>

## Langkah-langkah Membuat Proyek Django dan Deployment ke Adaptablle

1. **Buat Repo di Local dan GitHub**
   * Buat repositori dengan nama proyek (contoh: `tedskinventory`) di GitHub.
   * Clone repo tersebut.

2. **Buka CMD di Repo Local**
   * Buka terminal (CMD) dan navigasikan ke direktori repo local.

3. **Inisialisasi Git**
   * Inisialisasi Git di dalam repo local dengan perintah: 
    ```shell
        git init
     ```
   * Verifikasi akun GitHub dengan perintah: 
     ```shell
     git config user.name "tedskiii"
     git config user.email "theodorekasyfillah06@gmail.com"
     ```

4. **Inisialisasi Virtual Environment**
   * Buat dan aktifkan virtual environment dengan perintah: 
     ```shell
     python -m venv env
     env\Scripts\activate
     ```

5. **Inisialisasi Django dan Install Requirements**
   * Install Django dan dependencies yang diperlukan (misalnya, Psycopg2-binary untuk PostgreSQL) dengan perintah:
     ```shell
     pip install -r requirements.txt
     ```

6. **Mulai Proyek Django**
   * Inisialisasi proyek Django dengan perintah:
     ```shell
     django-admin startproject tedskinventory
     ```

7. **Buat Aplikasi Django Main**
   * Buat aplikasi Main Django  dengan perintah: 
     ``` shell
     python manage.py startapp main
     ```

8. **Isi Aplikasi Main**
   * Buat folder `templates` di dalam aplikasi `main` dan tambahkan file HTML yang akan digunakan sebagai template aplikasi.
     ``` html
     <body>
     <h1>Selamat Datang Di Tedskinventory</h1>
     <h3>Website Inventaris Pakaian Local Pride Idaman Kamu</h3>
     {% for product in products %}
     <div class="card">
      <div class = "name">
        <h4>{{ product.name }}</h4>
      </div>
      <img src="{{ product.image_url }}" alt="{{ product.name }}" >
      <div class = "credit">
        <p>(Source: uniqlo.com)</p>
      </div>
      <h5>{{ product.price }}</h5>
      <p>{{ product.description }}</p>
      <p>Jumlah Stok: {{ product.amount }}</p>
     </div>
     {% endfor %}
     </body>
     ```

   * Konfigurasi `models.py` dengan atribut yang diperlukan (name, image, price, description, amount).
   
     ```python
     from django.db import models
     from django.contrib.auth.models import User
     class Product(models.Model):
        name = models.CharField(max_length=255)
        image = models.ImageField(upload_to='products/', null=True, blank=True)
        price = models.CharField(max_length=255)
        description = models.TextField()
        amount = models.IntegerField()
     ```

9. **Konfigurasi URLs**
   * Di dalam folder proyek, konfigurasi `urls.py` untuk melakukan routing dengan perintah: 
   
     ```python
     path('main/', include('main.urls'))
     ```

10. **Konfigurasi Views**
    * Di dalam aplikasi `main`, konfigurasi views di `views.py` dan isi dengan data yang diperlukan untuk dirender ke file `main.html`.
      ``` python
      from django.shortcuts import render
        # Create your views here.
        def show_main(request):
            products = [
                {
                    'name': 'T-Shirt Garis Lengan Pendek',
                    'image_url': 'https://image.uniqlo.com/UQ/ST3/AsianCommon/imagesgoods/437241/item/goods_69_437241.jpg?width=750', 
                    'price': 'Rp.199.000',
                    'description': 'T-Shirt dengan motif garis-garis dari bahan kualitas terbaik di Indonesia',
                    'amount': 25,
                },
                {
                    'name': 'Jaket Casual',
                    'image_url': 'https://image.uniqlo.com/UQ/ST3/AsianCommon/imagesgoods/459591/sub/goods_459591_sub14.jpg?width=750',
                    'price': 'Rp.249.000',
                    'description': 'Jaket casual dengan desain trendy dari bahan kualitas terbaik di Indonesia',
                    'amount': 10,
                },
                {
                    'name': 'Celana Jeans Slim Fit',
                    'image_url': 'https://image.uniqlo.com/UQ/ST3/AsianCommon/imagesgoods/459688/sub/goods_459688_sub14.jpg?width=750',
                    'price': 'Rp.299.000',
                    'description': 'Celana jeans dengan potongan slim fit dari bahan kualitas terbaik di Indonesia',
                    'amount': 15,
                },
            ]
        
            context = {
                'products': products
            }
        
            return render(request, "main.html", context)
      ```
     

11. **Routing Aplikasi Main**
    * Di dalam aplikasi `main`, konfigurasi file `urls.py` untuk menangani permintaan ke URL `main`.
      ``` python
        from django.urls import path
        from main.views import show_main
        
        app_name = 'main'
        
        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
      ```

12. **Testing Local**
    * Jalankan proyek secara local dengan perintah: 
     ``` shell
     python manage.py runserver
     ``` 

13. **Push ke GitHub**
    * Push perubahan ke Git dengan perintah: 
      ```shell
      git add .
      git commit -m 
      git push origin master
      ```

14. **Deployment ke Adaptable**
    * Lakukan deployment ke Adaptable dengan memilih repo yang digunakan. Pastikan database dan server HTTP WSGI sudah terkonfigurasi.

15. **Selesaikan Deployment**
    * Lanjutkan langkah-langkah deployment yang diperlukan untuk menyelesaikan proses deployment ke Adaptablle.


## Bagan Penjelasan
Berikut adalah bagan penjelasan yang berisikan request client dan kaitan antara urls.py, views.py, models.py, dan berkas html.
![BAGAN_PENJELASAN](Bagan.png)

## Mengapa Menggunakan Virtual Environment?
Kita menggunakan virtual environment dalam pengembangan Django supaya workspace kita lebih terorganisir untuk masing masing proyek. Virtual Environment berperan juga supaya tidak terjadi masalah seperti tabrakan versi dan juga berguna untuk menjaga dependensi jadi lebih teratur . Sebenarnya kita bisa saja kita membuat Aplikasi tanpa virtual environment, tetapi disarankan untuk menggunakannya agar proyek-proyek kita lebih terorganisir.

## Penjelasan Mengenai MVC, MVT, dan MVVM
Berikut adalah penjelasan tentang MVC, MVT, dan MVVM:
* MVC (Model-View-Controller): MVC adalah konsep arsitektur aplikasi yang umum digunakan untuk mengimplementasikan UI, data, dan controller. konsep ini menekankan pemisahan antara logika bisnis aplikasi dan tampilan. Pemisahan ini memberikan pembagian kerja yang lebih baik dan pemeliharaan yang lebih baik.

* MVT (Model View Template): MVT adalah konsep arsitektur  aplikasi yang terdiri dari tiga komponen: Model, View, dan Template. Model menangani informasi , View menampilkan data, dan Template mendefinisikan tata letak halaman web. Meskipun mirip dengan MVC, MVT memiliki perbedaan dalam cara kerjanya.

* MVVM (Model-View-ViewModel): MVVM adalah konsep arsitektur  dalam aplikasi komputer yang memfasilitasi pemisahan pengembangan GUI dari pengembangan logika bisnis atau logika back-end (model) sehingga tampilan tidak bergantung pada platform model tertentu. ViewModel bertindak sebagai konverter nilai, yang bertanggung jawab untuk mengonversi objek data dari model sedemikian rupa sehingga dapat dengan mudah dikelola dan disajikan.

Perbedaan utama antara ketiganya adalah komponen yang digunakan dalam arsitektur tersebut. MVC memisahkan aplikasi menjadi Model, View, dan Controller, dengan komunikasi antara mereka melalui pengamatan dan pengontrolan. Di sisi lain, MVT, yang umumnya digunakan dalam kerangka kerja web Django, memiliki komponen Template tambahan yang mengatur tampilan halaman web. Sementara itu, MVVM memisahkan aplikasi menjadi Model, View, dan ViewModel, dengan ViewModel berperan sebagai perantara antara Model dan View, memungkinkan pemisahan yang lebih jelas antara tampilan dan logika aplikasi. Setiap konsep ini memiliki karakteristiknya sendiri dan digunakan sesuai kebutuhan proyek dan teknologi yang digunakan.

## Referensi Tugas 2:
* https://code.visualstudio.com/docs/python/tutorial-django
* https://stackoverflow.com/questions/62181396/django-does-the-virtual-environment-have-to-be-on-every-time-i-develop-my-djang
* https://developer.mozilla.org/en-US/docs/Glossary/MVC
* https://www.javatpoint.com/django-mvt
* https://learn.microsoft.com/en-us/dotnet/architecture/maui/mvvm
</details>

<details>
<summary>TUGAS 3</summary>

## Apa perbedaan antara form POST dan form GET dalam Django?
Dalam Django, form POST dan form GET mengacu pada dua metode HTTP yang berbeda yang digunakan dalam pengiriman data dari form.

Metode GET digunakan untuk meminta data dari server. Data yang dihasilkan dari form akan ditambahkan ke URL dalam bentuk query string. Namun, karena data tersebut ditampilkan di URL, metode GET sebaiknya tidak digunakan untuk mengirim data sensitif seperti password. Selain itu, karena keterbatasan panjang URL, metode GET mungkin tidak cocok untuk mengirim data yang besar 

Sebaliknya, metode POST digunakan untuk mengirim data ke server. Data yang dihasilkan dari form dikirim sebagai bagian dari body request, bukan sebagai bagian dari URL. Oleh karena itu, metode POST lebih aman dan dapat digunakan untuk mengirim data sensitif serta data yang besar. Dalam Django, data yang dikirim melalui metode POST biasanya diakses melalui atribut request.POST 

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML, JSON, dan HTML adalah tiga format data yang berbeda yang sering digunakan dalam pengiriman data di web.
* HTML (HyperText Markup Language) adalah bahasa markup yang digunakan untuk membuat struktur dan tampilan halaman web. HTML bukan format yang ideal untuk pengiriman data antara aplikasi karena strukturnya yang kompleks dan berorientasi tampilan 
* XML (eXtensible Markup Language) adalah bahasa markup yang digunakan untuk menyimpan dan mengangkut data. XML mendukung struktur data yang kompleks dan dapat mendefinisikan skema sendiri. Namun, XML cenderung lebih rumit dibandingkan dengan JSON 
* JSON (JavaScript Object Notation) adalah format yang digunakan untuk menyimpan dan mengangkut data. JSON lebih ringan dan lebih mudah dibaca dan ditulis oleh manusia dibandingkan dengan XML. JSON juga mudah untuk di-parse dan di-generate oleh mesin. Oleh karena itu, JSON sering menjadi pilihan yang disukai untuk pertukaran data antara aplikasi web.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena beberapa alasan:

* JSON memiliki sintaks yang lebih sederhana dan lebih ringan dibandingkan dengan format lain seperti XML. Hal ini membuatnya lebih efisien.
* JSON lebih mudah dibaca sehingga sangat membantu saat debugging
* Hampir semua bahasa pemrograman modern memiliki dukungan bawaan untuk parsing dan menghasilkan JSON.
* SON dapat di-parse dengan mudah oleh JavaScript, bahasa yang digunakan di mayoritas webapp.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Cara Saya Mengimplementasikan Checklist
## Langkah-langkah untuk Menambahkan Fitur ke Proyek Django

1. **Membuat Forms**
* Buat file `forms.py` di dalam aplikasi `main`.
* Tambahkan fields dari `forms` yang berasal dari class `Product` yang telah dideklarasikan di `models.py`.

     ``` python
     from django.forms import ModelForm
     from main.models import Produc
     class ProductForm(ModelForm):
     class Meta:
         model = Product
         fields = ["name", "price", "description", "amount"]
     ```

2. **Membuat Fungsi `create_product` di `views.py`**
* Buat fungsi baru di `views.py` dengan nama `create_product`.
     ``` python
     def create_product(request):
        form = ProductForm(request.POST or None)
        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        context = {'form': form}
        return render(request, "create_product.html", context)
     ```
    Fungsi ini akan merender tampilan dari form pada sebuah template HTML.

3. **Buat Template HTML untuk create_product**
* Buat file HTML sebagai template untuk form yang akan dirender oleh fungsi `create_product`.
     ``` html
     {% extends 'base.html' %} 
        {% block content %}
        <div class="card">
          <h1>Add New Product</h1>
          <form method="POST" enctype="multipart/form-data">
              {% csrf_token %}
              <div class="form-field">
                <label for="{{ form.name.id_for_label }}">Product Name:</label>
                {{ form.name }}
              </div>
              <div class="form-field">
                <label for="{{ form.price.id_for_label }}">Price:</label>
                {{ form.price }}
              </div>
              <div class="form-field">
                <label for="{{ form.description.id_for_label }}">Description:</label>
                {{ form.description }}
              </div>
              <div class="form-field">
                <label for="{{ form.amount.id_for_label }}">Stock Amount:</label>
                {{ form.amount }}
              </div>
              <div class="form-field">
                <input type="submit" value="Add Product" />
              </div>
          </form>
        </div>
     {% endblock %}
    ```

4. **Menambahkan Button pada `main.html`**
* Tambahkan tombol pada halaman `main.html` yang akan mengarahkan pengguna ke halaman yang berisi form untuk menambahkan produk.
     ```
     <a href="{% url 'main:create_product' %}">
          <button class="add-product-button">Add Item</button>
     </a>
     ```

5. **Menambahkan Fungsi Tampilan dalam Format XML dan JSON**
* Buat 4 fungsi baru: `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id`.
     ```
     def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        
     def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        
    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        
    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
     ```
    Fungsi ini akan mengambil data dari database menggunakan serializer dan mengubahnya menjadi format XML atau JSON.

8. **Routing**
* Tambahkan URL untuk masing-masing fungsi yang ingin Anda terapkan pada file `urls.py`.
     ```
     path('create-product', create_product, name='create_product'),
     path('xml/', show_xml, name='show_xml'), 
     path('json/', show_json, name='show_json'), 
     path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
     path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
     ```

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
* https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction
</details>

<details>
<summary>TUGAS 4</summary>

## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
**Django UserCreationForm** adalah formulir yang disediakan oleh Django untuk membuat pengguna baru. Formulir ini memiliki tiga field: `username`, `password1`, dan `password2` (yang digunakan untuk konfirmasi password). Anda juga dapat menyesuaikan UserCreationForm untuk model pengguna khusus.
Kelebihan menggunakan UserCreationForm adalah:
- Django menyediakan formulir ini secara default, jadi Anda tidak perlu membuatnya dari awal.
- Formulir ini sudah mencakup validasi dasar, seperti memeriksa apakah password cocok.
Namun, ada juga beberapa kekurangan:
- Formulir ini mungkin tidak mencakup semua bidang yang Anda butuhkan untuk aplikasi Anda, jadi Anda mungkin perlu menyesuaikannya.
- Jika Anda memiliki model pengguna khusus dengan bidang tambahan, Anda harus membuat formulir khusus yang mewarisi dari UserCreationForm dan menambahkan bidang tambahan tersebut.

##  Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi dan otorisasi adalah dua konsep penting dalam Django dan pengembangan web pada umumnya. **Autentikasi** adalah proses verifikasi identitas pengguna. Dalam konteks Django, ini biasanya melibatkan memeriksa apakah kombinasi nama pengguna dan password yang diberikan oleh pengguna cocok dengan yang ada di database². 
Di sisi lain, **otorisasi** adalah proses penentuan apa yang dapat diakses dan dimodifikasi oleh pengguna yang telah terautentikasi. Dalam Django, ini bisa melibatkan memeriksa apakah pengguna memiliki izin tertentu atau apakah mereka adalah bagian dari grup tertentu².
Kedua konsep ini penting karena mereka membantu menjaga keamanan aplikasi web. Autentikasi memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi, sementara otorisasi memastikan bahwa pengguna hanya dapat mengakses sumber daya atau melakukan tindakan yang mereka izinkan.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
**Cookies** adalah file teks kecil yang disimpan di browser web pengguna oleh situs web. Cookies digunakan untuk menyimpan informasi tentang sesi pengguna, seperti ID sesi atau preferensi lainnya. Dalam konteks Django, cookies dapat digunakan untuk mengelola data sesi pengguna.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan **Cookies**  pada dasarnya aman, tetapi ada beberapa risiko potensial yang harus diwaspadai. Cookies dapat menyimpan data dan ID pengguna, yang berarti bahwa jika seorang penyerang dapat mengakses cookies tersebut, mereka mungkin dapat mencuri identitas pengguna atau melakukan tindakan lain atas nama mereka Selain itu, karena cookies disimpan dalam bentuk teks, mereka mungkin rentan terhadap serangan seperti Cross-Site Scripting (XSS) atau Cross-Site Request Forgery (CSRF). Oleh karena itu, penting untuk selalu mengimplementasikan praktik keamanan terbaik saat bekerja dengan cookies.

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step 
1. **Membuat Fungsi Register**
* Buat fungsi baru di `views.py` dengan nama `register`.
     ``` python
     def register(request):
        form = UserCreationForm()
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)
     ```
     
* Render Fungsi tersebut pada sebuah file template html 
     ```html
     <div class="card">
        <h1>Register</h1>

     <form method="POST">
        {% csrf_token %}
         <div class="form-field">
           <label for="{{ form.username.id_for_label }}">Username:</label>
           {{ form.username }}
         </div>

         <div class="form-field">
           <label for="{{ form.password1.id_for_label }}">Password:</label>
           {{ form.password1 }}
         </div>

         <div class="form-field">
           <label for="{{ form.password2.id_for_label }}">Confirm Password:</label>
           {{ form.password2 }}
         </div>

         <div class="form-field">
           <input type="submit" name="submit" value="Register" class="btn login_btn">
         </div>
     </form>

     {% if messages %}
     <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
     </ul>
     {% endif %}

     Already have an account? <a href="{% url 'main:login' %}">Login Now</a>
     </div>
     </div>

     {% endblock content %}
     ```
     
2. **Membuat Fungsi Login**
* Buat fungsi baru di `views.py` dengan nama `login_user`.
     ``` python
     def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
     ```
     
* Render Fungsi tersebut pada sebuah file template html 
     ```html
     <div class="card">
        <h1>Login</h1>

      <form method="POST">
        {% csrf_token %}
        <div class="form-field">
          <label for="username">Username:</label>
          <input type="text" name="username" id="username"  class="form-control">
        </div>

        <div class="form-field">
          <label for="password">Password:</label>
          <input type="password" name="password" id="password" class="form-control">
        </div>

        <div class="form-field">
          <input type="submit" name="submit" value="Login" class="btn login_btn">
        </div>
      </form>

      {% if messages %}
      <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
      </ul>
      {% endif %}
  
     Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
     </div>

     {% endblock content %}
     ```

3. **Membuat Fungsi Logout**
* Buat fungsi baru di `views.py` dengan nama `logou_user`.
     ``` python
     def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
     ```
     
* Render Fungsi tersebut pada sebuah file template html 
     ```html
     <a href="{% url 'main:logout' %}">
      <button class="logout-button">Logout</button>
     </a>
     ```
     
4. **Menghubungkan product dengan user**
* Untuk menghubungkan model dengan user kita harus menambahkan model baru bernama user menggunakan foreign key

     ``` python
        user = models.ForeignKey(User, on_delete=models.CASCADE)
     ```
* Kemudian lakukan filter terhadap products pada `views.py` untuk memfilter product yang muncul pada aplikasi sesuai dengan user yang melakukan login
     ``` python
        products = Product.objects.filter(user=request.user)
     ```

5.  **Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di local.**
* Buat dua akun pengguna di page `register` yang telah dibuat.
* Buat tiga dummy data untuk masing-masing akun pengguna, Data akan tersimpan di database local.

6. **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti `last_login` pada halaman utama aplikasi.**
* Tambahkan sebuah fungsi untuk menambah cookie pada `login_user` ketika kondisi tidak none
     ```python
     response.set_cookie('last_login', str(datetime.datetime.now()))
     ```
* Tambahkan context baru di fungsi show main untuk melihat data `last_login` pada template `main.html`

     ```python
      'last_login': request.COOKIES['last_login'],
     ```

## Referensi Tugas 4
* https://www.javatpoint.com/django-usercreationform.
* https://docs.djangoproject.com/en/4.2/topics/auth/customizing/.
* https://diginews.id/apa-perbedaan-antara-otentikasi-dan-otorisasi/.
* https://docs.djangoproject.com/en/4.2/topics/auth/default/.
* https://www.pythontutorial.net/django-tutorial/django-cookies/.
* https://www.dewaweb.com/blog/cookies-panduan-lengkap/.
</details>