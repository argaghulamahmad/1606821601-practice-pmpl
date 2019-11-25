# Arga Ghulam Ahmad - 1606821601- Computer Science 2016 - PMPL B - Practice Repo
## Application Information
This application has deployed at [http://pmpl-arga.herokuapp.com/](http://pmpl-arga.herokuapp.com/)
## Exercises Stories
### Exercise 3 Story
#### How to Implement Test Isolation on Functional Test
Pada exercise 2, Functional test menguji aplikasi yang sudah dideploy di heroku.
Dengan demikian django akan meninggalkan item ToDo baru pada aplikasi heroku setiap functional test dijalankan.
Tentunya, hal itu mengganggu hasil test berikutnya. Oleh karena itu dibutuhkan suatu solusi agar antar aktivitas testing tidak saling mengganggu.

Salah satu solusi yang dapat diterapkan untuk mengatasi masalah tersebut adalah dengan Test Isolation.
Dengan Test Isolation, Django akan menjalankan proses testing dengan membuat database pengujian baru (terpisah dari yang asli).
Dengan demikian, proses testing dapat dijalankan dengan aman,

Lalu bagaimana cara menerapkan Test Isolation pada exercise 3?
- Karena Saya menggunakan selenium dalam melakukan functional test, Saya memanfaatkan LiveTestServerCase
    - LiveTestServerCase merupakan fitur yang disediakan django yang membantu melakukan functional test. Fitur ini secara otomatis meluncurkan server Django langsung di latar belakang, membuat database uji (seperti yang dilakukan oleh unit test), melakukan proses testing, dan mematikannya pada saat teardown.
    - LiveTestServerCase memungkinkan penggunaan klien uji otomatis (misalnya Selenium) untuk melakukan serangkaian uji fungsional di dalam browser dan mensimulasikan tindakan pengguna nyata.
    - Keuntungan yang diperoleh dengan menggunakan LiveTestServerCase adalah Saya tidak perlu menulis manual url aplikasi yang diuji.
        LiveTestServerCase akan memberikan url dari server django yang telah diluncurukan di latar belakang.
        URL tersebut dapat diakses melalu variabel self.live_server_url selama proses tes berlangsung.
        
#### Differences Between Old Design (Exercise 2) with New Design (Exercise 3) to Achieve Test Isolation
##### Use LiveServerTestCase instead of unittest.TestCase
Old Design (Exercise 2):
```python
import unittest

class NewVisitorTest(unittest.TestCase):
```
New Design (Exercise 3):
```python
# Change the class that use by NewVisitorTest for functional testing
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
```
##### Delete the code that take the HEROKU_APP_HOST from environment variables
Old Design (Exercise 2):
```python
import environ

root = environ.Path(__file__)
env = environ.Env(DEBUG=(bool, False), )
environ.Env.read_env('.env')

HEROKU_APP_HOST = env("HEROKU_APP_HOST")
print("HEROKU_APP_HOST is", HEROKU_APP_HOST)
```
New Design (Exercise 3):
```python
# Delete the old design code
```
##### Test the app with new database generated using LiveServerTestCase instead of deployed one
Old Design (Exercise 2):
```python
self.browser.get(HEROKU_APP_HOST)
```
New Design (Exercise 3):
```python
self.browser.get(self.live_server_url)
```

---

### Exercise 4 Story
#### Correlation between code changes in this exercise with chapter 7
##### Regression Test
Pada exercise 4, Saya belajar bagaimana bekerja secara incremental dan membuat tes regresi. 
Bekerja secara incremental mmerupakan cara bekerja yang dianjurkan oleh Test Driven Development.
Bekerja secara incremental adalah memecah pekerjaan menjadi pekerjaan-pekerjaan kecil yang dapat dikerjakan dengan mudah.
Selain bekerja secara incremental, Sata juga belajar bagaimana membuat tes regresi. 
Tes regresi merupakan salah satu jenis tes yang mengonfirmasi bahwa perubahan kode tidak mempengaruhi fitur yang sudah ada.
Tes regresi menjalankan semua atau sebagian kode yang sudah ada untuk memastikan fungsionalitas yang ada berfungsi dengan baik.
Pengujian ini dilakukan untuk memastikan bahwa perubahan kode baru seharusnya tidak menyebabkan efek samping pada fungsi yang sudah ada.
Pengujian ini memastikan bahwa kode yang lama masih bekerja dengan baik setelah ada penambahan kode/perubahan kode.

Pada exercise ini, Kali ini, Saya mengembangkan fitur TODO dengan desain arsitektur baru. 
Dimana, setiap pengunjung dapat membuat TODO yang berbeda dengan pengunjung yang lainnya. 
Untuk dapat menerapkan desain baru tersebut. 
Saya membagi pekerjaan tersebut menjadi pekerjaan-pekerjaan kecil yaitu menyesuaikan model sehingga item dikaitkan dengan daftar yang berbeda, menambahkan URL unik untuk setiap daftar, menambahkan URL untuk membuat daftar baru melalui POST, dan menambahkan URL untuk menambahkan item baru ke daftar yang ada melalui POST.
##### Prettification
Sebelum exercise 4, tampilan aplikasi TODO list ini masuh jelek. Pada exercise 4, Saya mulai menata kembali style aplikasi ini, mengintergasikan HTML dengan bootstrap,
mengonfigurasi static files, menggunakan CSS preprocessor, dan menguji style aplikasi menggunakan functional testing.

Dengan fungsional testing, Saya berhasil menguji tata letak dan gaya aplikasi. Namun, telebih dahulu Saya mempretifikasi aplikasi dengan menggunakan CSS.
Selain CSS saya juga mencoba SCSS. SCSS merupakan tools yang memungkinkan untuk memprogram CSS dan mengkompilenya menjadi CSS. Untuk mengkompile SCSS menjadi CSS,
Saya menggunakan file watcher yang disediakan oleh PyCharm. Untuk mempermudah mempretifikasi aplikasi ini, Saya mengunduh bootstrap dan menggunakannya sebagai static files.
Static files dapat digunakan dengan menjalankan perintah ```python manage.py collectstatic``` terlebih dahulu. Kemudian, menggunakannya di file html dengan keyword ```static```.
Selain mempretifikasi aplikasi, Saya juga merefactor templates yang sebelumnya tidak modular dan berada pada satu file saja. Sekarang, templates sudah bersifat modular dan reusable.
Terdapat tiga file html pada templates app list yaitu base, home, dan lists. Pada ketiga file html tersebut, Saya menintegrasikan bootstrap. Dengan bootstrap, Saya dapat menggunakan class ```row```
dan ```column```. Dengan demikian layout aplikasi ini lebih indah untuk dipandang. Selain ```row``` dan ```column```. Selain row dan column, Saya juga menggunakan 
jumbotron, table, dan input yang disediakan oleh bootstrap. Walaupun Saya menggunakan bootstrap, Saya juga menulis CSS sendiri, yaitu ```base.css```. Walaupun ```base.css``` Saya tulis ulang sebagai SCSS.
```base.scss``` Saya gunakan untuk mengubah warna belakang jumbotron menjadi hijau dan warna tulisan menjadi putih.

Kesimpulan yang Saya peroleh setelah mengerjakan exercise 4 adalah programmer tidak harus menulis tes untuk menguji desain dan tata letak.
Karena desain dan tata letak merupakan konstanta, dan tes ini sering mengalami perubahan. Setidaknya, programmer harus menulis tes minimal sehingga
desain dan tata letak yang programmer kembangkan berfungsi tanpa menguji apa itu sebenarnya. Usahakan agar programmer dapat dengan bebas membuat perubahan 
pada desain dan tata letak, tanpa harus kembali dan menyesuaikan tes setiap saat.

---

### Exercise 5 Story
#### Relevance between clean code and test driven development
Pada exercise 5 dan exercise-exercise sebelumnya, Saya sudah menerapkan Test Driven Development dan refactoring. 
Dalam praktik TDD, kita diwajibkan wajib menuliskan test terlebih dahulu kemudian menulis berkas sumber kode. 
Dengan demikian kita tidak bingung dalam mengimplementasikan fitur yang akan dikembangkan.
Tahap-tahap TDD adalah menulis tes yang gagal, menulis minimal working code sehingga test pass, kemudian refactor minimal working code (remove duplication).
Tujuan utama test driven development (TDD) dan refactoring adalah untuk mencegah (membayar, bila ada) technical debt. 
Technical debt dapat berupa tidak ada/kurangnya tes otomatis, tidak ada deployment otomatis, tidak ada nya dokumentasi, adanya code smell, software defects, desain yang buruk, dan lain lain. 
Dengan adanya TDD dan refactoring, jumlah technical debt dapat ditekan atau dihilangkan. Sehingga, kode dapat digolongkan menjadi clean code. 
Clean code memiliki beberapa karakteristik yaitu tidak mengandung code smell (bersih, jelas, dan tidak mengandung duplikasi) , high cohesion. lulus semua tes, dokumentasi berupa test, dan lebih mudah dan murah untuk dikembangkan.
#### Advantages applying test organizations
Kendala yang Saya hadapi pada exercise-exercise sebelumnya adalah semakin sulit untuk menulis test (functional atau unit tests) karena semua tes hanya ditulis dalam satu file saja.
Oleh karena itu, Saya perlu menerapkan test organizations. Test organizations (bisa disebut juga mengorganisir test) adalah suatu cara untuk membagi test menjadi file test-test yang lebih kecil.
Seperti yang dapat dilihat pada source code, Saya memecah functional test menjadi ```test_home_page.py,  test_layout_and_styling.py,  test_list_item_validation.py, dan test_simple_list_creation.py```.
Selain itu, Saya juga memecah unit test app lists menjadi ```test_home_page.py,  test_list_and_item_model.py,  test_list_view.py,  test_new_item.py, dan test_new_list.py```. 
Dengan demikian, Saya dapat dengan mudah menulis test karena setiap test sudah dibagi dan dibuat modular sesuai dengan fungsionalitas yang ingin diuji.

---

### Exercise 6 Story
#### Create two mutant from function in feedback todo feature views
Sebelum membuat mutant untuk fungsi pada views fitur feedback todo,
mari lihat bagaimana Saya mengimpelementasikan fungsionalitas fitur feedback todo.

Di bawah ini adalah source code views yang bertanggung jawab untuk memberikan data list todo ke frontend.
```python
lists/views.py

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})
```
Di bawah ini adalah source code template html yang menampilkan todo dan memberikan umpan balik berdasarkan jumlah todo.
```html
lists/templates/list.html

{% block todo_feedback %}
    <h5>Jumlah To-Do: {{ list.item_set.all|length }}</h5>
    <h6 id="todo-feedback">
        {% if list.item_set.all|length == 0 %}
            Yeahh, tidak ada tugas. Main game ahh.
        {% elif list.item_set.all|length < 5 %}
            Kerjain ahhh, biar cepat kelar.
        {% elif list.item_set.all|length >= 5 %}
            Oh tidakk, kerjaan ku banyak.
        {% endif %}
    </h6>
{% endblock %}
```
Dapat dilihat source code di atas,
yang bertanggung jawab untuk memutuskan umpan balik dari jumlah todo adalah
lists/templates/list.html. Oleh karena itu, Saya membuat dua mutant pada source code html tersebut.

Berikut source code template html di mana Saya membuat kedua mutant yaitu
```html
lists/templates/list.html

{% block todo_feedback %}
    <h5>Jumlah To-Do: {{ list.item_set.all|length }}</h5>
    <h6 id="todo-feedback">
        {% if list.item_set.all|length >= 0 %}
            Yeahh, tidak ada tugas. Main game ahh.
        {% elif list.item_set.all|length == 5 %}
            Kerjain ahhh, biar cepat kelar.
        {% elif list.item_set.all|length >= 5 %}
            Oh tidakk, kerjaan ku banyak.
        {% endif %}
    </h6>
{% endblock %}
```
Dua mutant yang Saya buat adalah
```html
    {% if list.item_set.all|length >= 0 %}
```
dan
```html
    {% elif list.item_set.all|length == 5 %}
```
Kedua mutant diperoleh dengan menerapkan relational operator replacement (ROR).
Mutant pertama diperoleh dengan mengganti operator `==` dengan `>=`.
Mutant kedua diperoleh dengan mengganti operator `<` dengan `==`.
#### Whether the tests have successfully strongly killed both mutants that have been made?
Sebelum memeriksa apakah kedua mutant yang sudah dibuat berhasil dibunuh secara kuat oleh
test case. Mari kita baca definisi dari membunuh secara kuat mutant yang diperoleh dari slide 
pendahuluan pengujian perangkat lunak oleh Ammmann.

```
Membunuh secara kuat adalah 

Diberikan sebuah mutant m dari sebuah program P dan test t, t dikatakan membunuh secara kuat m
jika dan hanya jika output dari t pada p berbeda dengan output t pada m.

```

Pada commit ```3a3ede8885cdc640de058a1094e665130f91045a``` dengan commit message 
```Create two mutant for the todo list feedback feature Using relational operator replacemen```,
 Saya sudah berhasil membuat dua mutant untuk fitur feedback todo dan Saya juga sudah berhasil 
membuat test case yang berhasil membunuh secara kuat dua mutant tersebut.

Berikut test case yang Saya buat untuk membunuh secara kuat kedua mutant tersebut yaitu

```python
functional_tests/test_list_item_validation.py
    
def test_multiple_users_can_start_lists_at_different_urls(self):
    # Arga starts a new to-do list
    self.browser.get(self.server_url)
    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Buy peacock feathers')
    inputbox.send_keys(Keys.ENTER)
    self.check_for_row_in_list_table('1: Buy peacock feathers')

    # He notices that Him list has a unique URL
    edith_list_url = self.browser.current_url
    self.assertRegex(edith_list_url, '/lists/.+')

    # He want to know what the system's feedback when there is a to-do
    todo_feedback = self.browser.find_element_by_id("todo-feedback")
    self.assertEqual("Kerjain ahhh, biar cepat kelar.", todo_feedback.text)

    # He is invited to enter some to-do items, to check what the system feedback after he input 5 to-do items in
    # total
    for i in range(4):
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Another todo' + str(i))
        inputbox.send_keys(Keys.ENTER)

    todo_feedback = self.browser.find_element_by_id("todo-feedback")
    self.assertEqual("Oh tidakk, kerjaan ku banyak.", todo_feedback.text)
```

Bagaimana Saya tahu bahwa test case yang dibuat sudah berhasil membunuh secara kuat mutant tersebut?
Dapat dilihat status pipeline commit ini di gitlab adalah failed, di mana functional test-nya gagal.
Dengan functional test fitur feedback todo yang gagal, 
dapat disimpulkan bahwa output test case (t) fitur feedback todo pada program (p) 
berbeda dengan output test case (t) pada kedua mutant (t).

Jadi, Saya sudah berhasil membuat dua mutant dan test case yang membunuh secara kuat kedua mutant tersebut.
#### Install the django_mutpy and check the result
Sebelum dapat menggunakan django mutpy terlebih dahulu Saya menginstall package tersebut menggunakan pip
dan menambahkan package tersebut sebagai installed apps.

```bash
# Add the django mutpy yo requirements.txt

pip install django-mutpy
pip freeze > requirements.txt
```


```python
# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mutpy',
    'lists'
]
```

Kemudian, Saya menjalankan mutation testing untuk pertama kali menggunakan
django mutpy. 
```bash
python manage.py muttest lists
```
Berikut merupakan hasil penggunaan django mutpy pada app lists untuk pertama kali.
```
[*] Mutation score [7.64198 s]: 49.2%
   - all: 63
   - killed: 31 (49.2%)
   - survived: 32 (50.8%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%) 
```
Dilihat dari hasil menjalankan mutation test menggunakan mutpy untuk pertama kali,
Saya berhasil membunuh 31 mutant dengan mutation score yang diperoleh adalah 49.2%.

Berdasarkan hasil penggunaan django mutpy pada app lists, untuk pertama kali,
dapat disimpulkan bahwa semua fungsi yang ada pada source code di ```lists/models.py```, ```lists/urls.py```, dan ```lists/views.py```
sudah berhasil dibunuh oleh test case yang ada pada ```lists/tests.py```.

Fungsi yang survived adalah fungsi yang berada pada source code di folder  ```lists/migrations```, 
di mana source code tersebut merupakan hasil ```manage.py makemigrations``` dari source code yang ada pada
````lists/models.py````. Selain itu juga ada source code lain yang survived yaitu ```lists/apps.py```.
Oleh karena itu, Saya membuat unit test untuk menguji ```lists/apps.py```.

Berikut unit test yang Saya tulis untuk menguji ```lists/apps.py``` yaitu
````python
lists/tests/test_apps.py

from django.apps import apps
from django.test import TestCase
from lists.apps import ListsConfig


class ListsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(ListsConfig.name, 'lists')
        self.assertEqual(apps.get_app_config('lists').name, 'lists')

````

Setelah Saya selesai mengimplementasikan unit test untuk menguji ```lists/apps.py```,
Saya pun menjalankan mutation test menggunakan mutpy untuk kedua kalinya. 
Berikut hasilnya yaitu

```
[*] Mutation score [8.09359 s]: 52.4%
   - all: 63
   - killed: 33 (52.4%)
   - survived: 30 (47.6%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
```

Dilihat dari hasil menjalankan mutation test menggunakan mutpy untuk kedua kalinya,
Saya berhasil membunuh 33 mutant dengan mutation score yang diperoleh adalah 52.4%.

Jadi Saya berhasil merefactor unit test untuk memperbaiki kualitas yang Saya miliki
berdasarkan hasil penggunaan mutation testing tool django mutpy.

---

### Exercise 7 Story
#### My Experience on applying spiking and de-spiking technique
Pada exercise 7 Saya mempelajari teknik bagaimana agar dapat belajar suatu application programming interface dengan bebas tetapi tetap menerapkan test driven development. Teknik tersebut dinamakan dengan spiking dan de-spiking. 

Teknik spiking merupakan suatu teknik untuk mengeksplorasi suatu API tanpa menerapkan test driven development (TDD) dan menulis unit test. Sebagai contoh, Saya belajar bagaimana menggunakan API untuk mengirim email smtp menggunakan library Django mail dan otentikasi menggunakan library Django auth tanpa menerapkan test driven development. Teknik spiking tersebut Saya lakukan dengan membuat branch baru (exercise-7-1) dari branch master, implementasi kode pada exercise-7-1 (tahap spiking), kemudian kembali ke branch master saat de-spiking. Sebelum de-spiking, saya membuat fungsional tes dari hasil implementasi teknik spiking agar dapat digunakan pada tahap de-spiking. Pada tahap de-spiking, Saya kembali ke branch master dan membuat branch baru (exercise-7-2), kemudian Saya membuang kode yang dibuat pada tahap spiking dan mengimplementasikan fitur dari awal lagi dengan menerapkan test driven development.

Keuntungan yang Saya peroleh dengan menggunakan teknik spiking dan de-spiking adalah Saya dapat membuat fungsional test pada teknik spiking yang mana fungsional test tersebut dapat dijadikan acuan pada teknik de-spiking. Dengan demikian, pada proses implementasi di tahap de-spiking Saya dapat fokus menulis unit test dan implementasi kode yang lebih baik, efektif dan efisien daripada kode yang ditulis pada tahap spiking.

---

### Exercise 8 Story
#### Differences between manual mocking with mocking using library
Mocking merupakan aktivitas mensimulasikan objek dengan meniru perilaku objek nyata dengan cara yang terkontrol. Salah satu penerapan mocking adalah untuk menguji dependencies eksternal. Pada tutorial ini, Saya menggunakan mocking untuk menguji fungsi layanan pengirim email. Mocking yang Saya praktikan ada dua macam yaitu mocking manual dan mocking menggunakan library. Mocking dapat dilakukan dengan dua cara yaitu mocking secara manual dan mocking menggunakan library.

Karena bahasa pemrograman python merupakan bahasa pemrograman dinamis. Kita dapat memanfaatkan sifat dinamisnya untuk melakukan mocking secara manual. Yang dimaksud dengan mocking manual adalah mereplace fungsi yang ingin di-mock menggunakan fungsi baru palsu. Fungsi baru palsu ini dibuat dengan membuat variabel mocking di dalam fungsi tersebut. Fungsi tersebut akan berperilaku seperti mutable objek yang berisi daftar variabel, dimana bila ada perubahan input variabel maka isi daftar variable juga berubah.

Namun, melakukan mocking manual membutuhkan upaya yang cukup banyak. Oleh karena itu, Kita dapat memanfaatkan library mocking python yaitu `unittest.mock`. Library ini dapat melakukan mocking pemanggilan fungsi atau atribut apapun. Dimana, nilainya dapat dikonfigurasikan secara spesifik. Untuk memocking suatu object kita tinggal menambahkan decorator function yaitu `patch`. Dimana kita dapat mengotomatisasikan mocking manual dengan menggunakan  decorator function ini.
#### Why mocking can make the implementation that we make tightly coupled
Walaupun, mocking membantu pengembang perangkat lunak untuk menguji dependencies, mocking dapat membuat implementasi yang kita buat tightly coupled. Terlebih apabila kita menguji detail implementasi dibandingkan perilaku. Sebagai contoh fungsi unit test `test_adds_success_message`:
```python
def test_adds_success_message(self):
    response = self.client.post('/accounts/send_login_email', data={
        'email': 'edith@example.com'
    }, follow=True)

    message = list(response.context['messages'])[0]
    self.assertEqual(
        message.message,
        "Check your email, we've sent you a link you can use to log in."
    )
    self.assertEqual(message.tags, "success")
```
Apa yang terjadi pada `accounts/views.py` apabila kita menguji fungsionalitas menambahkan pesan sukses dengan mocking? Kita dapat me-mock modul `messages` dan mengecek atribut success pada messages dengan parameter `request` asli, dan pesan yang kita inginkan. Kurang lebih seperti ini nantinya:
```python
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse

from accounts.models import Token

def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for Superlists',
        message_body,
        'noreply@superlists',
        [email]
    )
    messages.add_message(
        request,
        messages.SUCCESS,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')
```
Bila diperhatikan, ada sesuatu implementasi yang berbeda dari implementasi `accounts/views.py` (mocking) yang Saya terapkan yaitu
```python
messages.add_message(
    request,
    messages.SUCCESS,
    "Check your email, we've sent you a link you can use to log in."
)
```
Padahal implementasi tersebut dapat dicapai dengan source code (non mocking) berikut
```python
messages.success(
    request,
    "Check your email, we've sent you a link you can use to log in."
)
```
Apabila kita mengeksekusi unit test. Tes mock akan berhasil, tetapi tidak dengan tes non mock. Tes non mock akan gagal. Meskipun hasil akhirnya sama, implementasi benar, dan unit test non mock rusak.

Inilah akibat apabila kita tidak berhati-hati dalam memutuskan apakah suatu fungsionalitas harus diuji menggunakan mocking atau tidak. Apabila kita salah memutuskan apakah mocking diperlukan untuk menguji suatu fungsionalitas, implementasi yang kita buat tightly coupled dengan unit test yang dibuat. Masalah ini merupakan hal yang harus dihindari. Oleh karena itu, Kita harus bijak dalam memilih apakah suatu fungsionalitas harus diuji menggunakan mocking atau tidak.

---

### Exercise 9 Story
#### Differences between functional implementation between sub bab 20.1 with sub bab 18.3
Pada functional test subbab 20.1, Saya menulis sebuah fungsi di file test_my_lists.py yang digunakan untuk men-skip semua proses login pada saat melakukan pengujian fungsional. Fungsi tersebut bernama create_pre_authenticated_session. 

```python
class MyListsTest(FunctionalTest):

    def create_pre_authenticated_session(self, email):
        user = User.objects.create(email=email)
        session = SessionStore()
        session[SESSION_KEY] = user.pk
        session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        session.save()

        # to set a cookie we need to first visit the domain.
        # 404 pages load the quickest!

        self.browser.get(self.live_server_url + "/404_no_such_url/")
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session.session_key,
            path='/',
        ))
```

Cara kerja fungsi ini adalah membuat ulang session object pada database testing. Session object berisi session key yang merupakan primary key dari objek user. Kemudian, fungsi tersebut menambahkan cookie ke browser. Dengan cookie tersebut, browser akan menyimpan informasi bahwa proses functional test ini merupakan pengguna yang sudah login. Oleh karena itu, fungsi ini memungkinkan proses login functional test dilakukan hanya sekali saja untuk semua test. Berbeda dengan functional test subbab 18.3 yang melakukan proses login pada setiap test.
### Why sub bab 20.1 login functional test implementation is better than sub bab 18.3 login functional test implementation?
Dengan implementasi subbab 20.1 functional test untuk fitur login yaitu proses login functional test dilakukan hanya sekali saja untuk semua test, diperoleh keuntungan yaitu menghemat waktu yang diperlukan untuk menjalankan proses functional test. Berbanding terbalik dengan, subbab 18.3 yang menghabiskan banyak waktu untuk setiap test untuk proses login saja.

