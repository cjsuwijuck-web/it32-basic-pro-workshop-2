quantity = int(input("จำนวนปืนที่รับมาขาย :"))
cost_price = int(input("ต้นทุนของปืนที่รับมา (บาท/กระบอก :"))
sell_price = int(input("ราคาที่จะนำไปขายต่อ (บาท/กระบอก : "))
team_members = int(input("จำนวนลูกน้องในทีมที่ไปทำงาน (คน) :"))

totalcost = cost_price * quantity
Money = quantity * sell_price
Profit = Money - totalcost
Bossmoney = 0.2 * Profit
member = Profit / team_members


print("ต้นทุนทั้งหมด",totalcost, "bath")
print("รายรับทั้งหมด",Money, "bath")
print("กำไร",Profit, "bath")
print(f"จำนวนเงินที่หักให้บอส {Bossmoney} bath")
print(f"จำนวนเงินที่ลูกน้องได้{member} bath")
