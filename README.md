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