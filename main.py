class Bankomat:
     def __init__(self, parol):
         self.parol = parol
         self.k_parol = 1111
         if self.parol == self.k_parol:
             a = 100000
             print(f"Balansda {a} so'm bor")
             qwe = input("Pul yechishni istaysizmi: (ha/yoq) ")
             if qwe == 'ha':
                 qwer = int(input("Yechish kerak bo'lgan summani kiriting: "))
                 if qwer > a:
                     print("Balansda pul yetarli emas")
                 else:
                     a-=qwer
                     print(f"Balansda {a} so'm qoldi")
             else:
                 print("Xizmat ko'rsatish tugadi")
         else:
             print("Parol noto'g'ri")         
    
     def sms_qabul(self):
         tekshir = int(input("Telefon raqamni ulash uchun parolni kiriting: "))
         if tekshir == self.k_parol:
             qwe = input("Sms qabul qiluvchi telefon raqamingini kiriting: +998")
             if len(qwe) == 9:
                 print("Raqam muvaffaqiyatli qo'shildi")
             else:
                 print("Raqam kiritishda xatolik")
         else:
             print("Parolni xato kiritdiz")
     
     
     
     def parolni_almashtir(self):
         paroll = int(input("Eski parolni kiriting: "))
         if paroll == self.k_parol:
             son = int(input("Yangi parolni kiriting: "))
             son1 = int(input("Yangi parolni yana bir bor kiriting: "))
             if son == son1:
                 print("Parol muvaffaqiyatli o'rnatildi")
             else:
                 print("Yangi parollar bir xil emas")
         else:
             print("Parol noto'gri") 
s = Bankomat(parol =  1111)
s.sms_qabul()
s.parolni_almashtir()