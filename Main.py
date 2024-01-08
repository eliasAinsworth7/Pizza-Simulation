#coding:utf8
import csv
import datetime 


class pizza():
    def __init__(self,cost,description):
     self.cost = cost
     self.description = description

    def get_cost(cost):
      return cost
    
    def get_description(description):
      return description
class TürkPizza(pizza):
    cost = 2
    description = 'Turko misali pizza, hamurun icinde özel kahribar sosuyla'
class Klasik(pizza):
    cost = 2
    description = 'Klasik taban,peynir,salca..'
     
class AgizKokutan(pizza):
    cost = 3
    description = 'Bol soganli ve ekstra sarmisak:)'
     
class Zengin(pizza):
    cost = 5
    description = 'Etli, tavuklu ve sosisli zengin pizzasi'
     
class GoatPizza(pizza):
    cost = 4
    description = 'CR7 onayli GOAT pizza, peri peri sosuyla'
class Distractor():
  def get_cost(cost):
      return cost
    
  def get_description(description):
      return description
class Zeytin(Distractor):
  cost = 1
  description= "simsiyah"
class Mantarlar(Distractor):
  cost = 1
  description="Mantar dogada kolay bulunur tati hojdur"
class KeciPeyniri(Distractor):
  cost = 2
  description="Taze el yapimi"
class Et(Distractor):
  cost = 3
  description="Azot bakimindan iyidir, protein koçum"
class Sogan(Distractor):
  cost = 1 
  description="Nefiss, doğal agri kesici"
class Misir(Distractor):
  cost = 1
  description="Sut misirdir.."


def validate_credit_card(card_number: str) -> bool:
    card_number = [int(num) for num in card_number]

    checkDigit = card_number.pop(-1)

    card_number.reverse()

    card_number = [num * 2 if idx % 2 == 0
                   else num for idx, num in enumerate(card_number)]


    card_number = [num - 9 if idx % 2 == 0 and num > 9
                   else num for idx, num in enumerate(card_number)]

    card_number.append(checkDigit)

    checkSum = sum(card_number)

    return checkSum % 10 == 0

class main():
 #f = open("Menu.txt", "a")
 #try:
    #f.write("* Lutfen Bir Pizza Tabani Seciniz: 1: Klasik, 2: AgizKokutan 3: TurkPizza 4: Margarita 5:GoatPizza * ve sececeginiz sos: 11: Zeytin 12: Mantarlar 13: Keci Peyniri 14: Et 15: Sogan 16: Misir * Tesekku3r ederiz! ")
 #finally:
    #f.close()

 f = open("Menu.txt", "r")
    
 print(f.read())  
 
   
 cost1 =0

 print("Lütfen pizza tabanı seçin")
 taban = input()
 i = 1
 while i ==1:
  if taban=="AgizKokutan":
    cost1+=AgizKokutan.cost
    i=0
  elif taban=="Klasik":
    cost1+=Klasik.cost
    i=0
  elif taban=="TurkPizza":
    cost1+=TürkPizza.cost
    i=0
  elif taban=="GoatPizza":
    cost1+=GoatPizza.cost
    i=0
  elif taban=="Zengin":
    cost1+=Zengin.cost
    i=0
    
 else: 
    "Doğru yaz kardşm"

 print("Sos Seçiniz")
 sos=input()
 while i ==0:
   if sos=="Zeytin":
    cost1+=Zeytin.cost
    i=1
   elif sos=="Mantarlar":
    cost1+=Mantarlar.cost
    i=1
   elif sos=="KeçiPeyniri":
    cost1+=KeciPeyniri.cost
    i=1
   elif sos=="Et":
    cost1+=Et.cost
    i=1
   elif sos=="Soğan":
    cost1+=Sogan.cost
    i=1
   elif sos=="Mısır":
    cost1+=Misir.cost
   else: 
    "Doğru yaz kardşm"   

 print("TC nizi giriniz")
 tcNumber = input()
 while i==1:
    print("Kredi Kartınızı giriniz")
    cart = input()
    if validate_credit_card(cart):
     i==0

 print("İsminizi giriniz")
 name= input()

 print("Isim: "+name+", TC numarasi: "+tcNumber+" Kredi Karti: "+cart+"Ucretiniz: "+cost1)
 

  