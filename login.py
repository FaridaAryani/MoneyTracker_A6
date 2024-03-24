import re
import time

def is_password_strong(password):
    # Memeriksa apakah password memenuhi standar internasional
    # Standar internasional:
    # - Panjang minimal 8 karakter
    # - Setidaknya satu huruf kecil (a-z)
    # - Setidaknya satu huruf besar (A-Z)
    # - Setidaknya satu angka (0-9)
    # - Setidaknya satu karakter khusus (misalnya: !, @, #, $, %, ^, &, *)
    return (
        len(password) >= 8 and
        re.search("[a-z]", password) and
        re.search("[A-Z]", password) and
        re.search("[0-9]", password) and
        re.search("[!@#$%^&*]", password)
    )

def register(username, password):
    if is_password_strong(password):
        with open('users.txt', 'a') as file:
            file.write(f"{username},{password}\n")
        print("Registrasi berhasil!")
    else:
        print("Password tidak memenuhi standar keamanan. Password harus memiliki setidaknya 8 karakter, termasuk huruf besar, huruf kecil, angka, dan karakter khusus.")

def login(username, password):
    with open('users.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if stored_username == username and stored_password == password:
                print("Login berhasil!")
                return True
    print("Username atau password salah.")
    return False

def print_welcome_message():
    print("===============================================")
    print("  Selamat datang di Aplikasi Money Tracker ")
    print("===============================================")

def print_menu():
    print("\nPilih opsi:")
    print("1. Registrasi")
    print("2. Login")
    print("3. Keluar")

def print_goodbye_message():
    print("===============================================")
    print("        Terima kasih telah menggunakan")
    print("        Aplikasi Money Tracker kami!")
    print("===============================================")

def print_ascii_art():
    ascii_art = """
   _____                                           
  /     \   ____   ____   ____ ___.__.             
 /  \ /  \ /  _ \ /    \_/ __ <   |  |             
/    Y    (  <_> )   |  \  ___/\___  |             
\____|__  /\____/|___|  /\___  > ____|             
        \/            \/     \/\/                  
___________                     __                 
\__    ___/___________    ____ |  | __ ___________ 
  |    |  \_  __ \__  \ _/ ___\|  |/ // __ \_  __ \ 
  |    |   |  | \// __ \\  \___|    <\  ___/|  | \/
  |____|   |__|  (____  /\___  >__|_ \\___  >__|   
                      \/     \/     \/    \/       
   _____    ________                               
  /  _  \  /  _____/                               
 /  /_\  \/   __  \                                
/    |    \  |__\  \                               
\____|__  /\_____  /                               
        \/       \/                                
    """
    print(ascii_art)

def loginmain():
    print_ascii_art()
    print_welcome_message()

    while True:
        print_menu()

        choice = input("Masukkan nomor opsi: ")

        if choice == '1':
            print("\n[Registrasi]")
            username = input("Masukkan username baru: ")
            password = input("Masukkan password: ")
            register(username, password)
            time.sleep(3)  # Tunggu sebentar setelah registrasi sebelum kembali ke menu
            continue

        elif choice == '2':
            print("\n[Login]")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            if login(username, password):
                print("===============================================")
                print(f" Selamat datang, {username}!")
                print("===============================================")
                return username
            break

        elif choice == '3':
            print_goodbye_message()
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan nomor opsi yang benar.")
