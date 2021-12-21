islem = input("Yapmak istediginiz islemi yaziniz: [yukleme] [silme] [indirme] [gonderme] ")
if islem == "yukleme" :
	x = float(input("Yuklemek istediginiz dosyanin adini yaziniz: "))
	y = float(input("Yuklemek icin gereken 2. dosyanin adini yaziniz: "))
	print(x + y)
elif islem == "indirme" :
	x = float(input("Indirmek istediginiz dosyayin adini yaziniz: "))
	y = float(input("Indirmek icin gereken 2. dosyanin adini yaziniz: "))
	print(x - y)
elif islem == "silme" :
	x = float(input("Silmek istediginiz dosyanin adini yaziniz: "))
	y = float(input("Silmek icin gereken 2. dosyanin adini yaziniz: "))
	print(x / y)
elif islem == "gonderme" :
	x = float(input("Gondermek istediginiz dosyanin adini yaziniz: "))
	y = float(input("Gondermek icin gereken 2. dosyanin adini yaziniz: "))
	print(x * y)

else :
	print("Gecersiz islem girdiniz. Lütfen tekrar deneyiniz.")

