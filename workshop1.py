Name = int(input("ชื่อ :"))
age = int(input(" อายุ :"))
CM = int(input("ส่วนสูง : "))
Power = int(input("พละกำลัง :"))
Money = int(input("ตัง : "))

print(Name)
if age < 25 :
 print("คุณไม่ผ่าน")
elif Power < 3000 :
 print("คุณไม่ผ่าน")

elif Money < 30000 :
 print("คุณไม่ผ่าน")
elif Money > 300000 :
 print("คุณผ่าน")

