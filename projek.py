import time
print("--------------------------------------------------")
#Welcome the user
print(" #### KUIZ SEMPENA HARI KEMERDEKAAN MALAYSIA ####")
time.sleep(2)
print("--------------------------------------------------")

#Chances
chances=1
print("SILA PILIH SATU JAWAPAN YANG BETUL.\n")
time.sleep(2)

#SKOR
score=0

#SOALAN 1
print("==================================================")
question_1=print("1) SIAPAKAH BAPA KEMERDEKAAN NEGARA KITA?\n(A) Tunku Abdul Rahman\n(B) Tun Abdul Razak\n(C) Tun Dr Mahathir\n(D) Tun Hussain Onn\n\n")
answer_1= "A"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.upper() == answer_1):
        print("TAHNIAH! JAWAPAN ANDA BETUL!\n")
        score = score + 1
        break
    else:
        print("JAWAPAN ANDA SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL", answer_1, "\n\n")

time.sleep(2)

#SOALAN 2
print("==================================================")
question_2 = print("2)BILAKAH NEGARA KITA MERDEKA?\n(A) 1956\n(B) 1957\n(C) 1960\n(D) 1963\n\n")  
answer_2 = "B"

for i in range(chances):
    answer = input("answer: ")
    if (answer.upper() == answer_2):
        print("TAHNIAH! JAWAPAN ANDA BETUL!\n")
        score = score + 1
        break
    else:
        print("JAWAPAN ANDA SALAH!\n ")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL ADALAH ", answer_2, "\n\n")

time.sleep(2)

#SOALAN 3
print("==================================================")
question_3 =print("3)  REKABENTUK BENDERA MALAYSIA MEMPUNYAI JALUR BERWARNA APA?\n(A) Merah Putih \n(B) Merah Biru\n(C) Biru Kuning\n(D) Biru Merah\n\n")
answer_3= "B"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.upper() == answer_3):
        print("TAHNIAH! JAWAPAN ANDA BETUL!\n")
        score = score + 1
        break
    else:
        print("JAWAPAN ANDA SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL ADALAH ", answer_3, "\n\n")

time.sleep(2)

#SOALAN 4
print("==================================================")
question_4 =print("4)  APAKAH GELARAN YANG MERUJUK KEPADA NEGERI KEDAH?\n(A) Darul Naim\n(B) Darul Khusus\n(C) Darul Ehsan\n(D) Darul Aman\n\n")
answer_4= "D"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.upper() == answer_4):
        print("TAHNIAH! JAWAPAN ANDA BETUL!\n")
        score = score + 1
        break
    else:
        print("JAWAPAN ANDA SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL ADALAH ",answer_4, "\n\n")

time.sleep(2)

#SOALAN 5
print("==================================================")
question_5 =print("5)  SIAPAKAH NAMA PERDANA MENTERI MALAYSIA SEKARANG?\n(A) TUN ABDULLAH AHMAD BADAWI\n(B) TAN SRI MAHYUDDIN BIN YASSIN\n(C) DATUK SERI ANUAR IBRAHIM\n(D) TUN DR MATHIR MOHAMAD\n\n")
answer_5= "C"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.upper() == answer_5):
        print("TAHNIAH! JAWAPAN ANDA BETUL!\n")
        score = score + 1
        break
    else:
        print("JAWAPAN ANDA SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN YABNG BETUL ADALAH ", answer_5, "\n\n")

time.sleep(2)

#CETAK SKOR
print("==================================================")
while score >=2:
    print("TAHNIAH! SKOR ANDA ADALAH", score)
    break

while score <2:
    print("USAHA LAGI! SKOR ANDA ADALAH",score)
    break

#Goobye message
print("TERIMA KASIH!")