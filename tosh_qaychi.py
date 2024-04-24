import random

tosh =  """
    _____
---' ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

qaychi =  """
    _____
---' ____)____
          ______)
       __________)
      (____)
---.__(___)
""" 

qogoz =  """
     _____
---' _____)____
           _______)
          ________)
         ________)
---.___________)
""" 



lst = [tosh, qaychi, qogoz]
print("1.Tosh\n2.Qaychi\n3.Qog'oz")


odam = int(input("Marhamat tanlang: "))
if odam > 3 or 0 > odam:
    print("Iltomos 1 dan 3 gacha son kiritng")
    exit()
pc = random.choice(lst)
if odam == 1:
    odam = tosh
elif odam == 2:
    odam = qaychi
elif odam == 3:
    odam = qogoz


print(f"PC {pc}")
print(f"Siz {odam}")
if odam == tosh and pc == qaychi:
    print("Siz yutdingiz")
elif odam == tosh and pc == qogoz:
    print("Siz yutdingiz")
elif odam == tosh and pc == tosh:
    print("Durrang")
elif odam == qaychi and pc == tosh:
    print("Siz yutqazdingiz")
elif odam == qaychi and pc == qogoz:
    print("Siz yutdingiz")
elif odam == qaychi and pc == qaychi:
    print("Durrang")
elif odam == qogoz and pc == qaychi:
    print("Siz yutqazdingiz")
elif odam == qogoz and pc == tosh:
    print("Siz yutqazdingiz")
elif odam == qogoz and pc == qogoz:
    print("Durrang")


