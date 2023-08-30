# Detta program ska fungera som ett exempel 
# på det som gås igenom på dagens lektion!
# Kör programmet och kolla utskriften
SPACING = 65
print(SPACING*"-")
print("Operatorer".center(SPACING, "-"))
print(SPACING*"-")
print("|"+8*"\t|")
print(f"{5+5=}\t\t\t\t\t{type(5+5)=}") 
print(f"{5-5=}\t\t\t\t\t{type(5-5)=}")
print(f"{5-4.6=}\t\t{type(5-4.6)=}")
print(f"{5-4.6=:.1f}\t\t\t\t{type(5-4.6)=}")
print(f"{5/5=}\t\t\t\t\t{type(5/5)=}")
print(f"{5*5=}\t\t\t\t\t{type(5*5)=}")
print(f"{5**5=}\t\t\t\t{type(5**5)=}")
print(f"{10//3=}\t\t\t\t\t{type(13//3)=}") # 10 = 4*3 + 1 
print(f"{10%3=}\t\t\t\t\t{type(13%3)=}") # 10 = 4*3 + 1
print(f"{5*4.5=}\t\t\t\t{type(5*4.5)=}")
print(f"{5*'T'=}\t\t\t\t{type(5*'T')=}")
print(f"{3*True=}\t\t\t\t{type(3*True)=}")
print(f"{3*False=}\t\t\t\t{type(3*False)=}")
print(f"{False=}\t\t\t\t{type(False)=}")
print(f"{5>4=}\t\t\t\t{type(5>4)=}")
print(f"{5<4=}\t\t\t\t{type(5<4)=}")
print(f"{'str'=='str'=}\t\t\t{type('str'=='str')=}")


print(SPACING*"-")
print("Variabler".center(SPACING, "-"))
print(SPACING*"-")
print("|"+8*"\t|")
v1 = 5
print(f"{v1=}\t\t{id(v1)=}\t{type(v1)=}")
v1 = 6
print(f"{v1=}\t\t{id(v1)=}\t{type(v1)=}")
v1 = "7"
print(f"{v1=}\t\t{id(v1)=}\t{type(v1)=}")
v1 = True
print(f"{v1=}\t\t{id(v1)=}\t{type(v1)=}")
v2 = v1
print(f"v2=v1\t\t{id(v2)=}\t{type(v2)=}")
print(f"{v2 is v1 =}\t\t\t\t{v2 == v1=}")
v1 = 3.14
print(f"{v1=}\t\t{id(v1)=}\t{type(v1)=}")
v2 = 3.14
print(f"{v2=}\t\t{id(v2)=}\t{type(v2)=}")
v1 = [2,3]
print(f"{v1=}\t{id(v1)=}\t{type(v1)=}")
v2 = [2,3]
print(f"{v2=}\t{id(v2)=}\t{type(v2)=}")
print(f"{v2 is v1 =}\t\t\t\t{v2 == v1=}")


