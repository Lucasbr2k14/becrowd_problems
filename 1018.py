dinheiros:int = int(input())

cedulas:list[int] = [100, 50, 20, 10, 5, 2, 1]

print(dinheiros)

for i in range(len(cedulas)):
  q_cedula:int = dinheiros//cedulas[i]
  dinheiros -= (q_cedula * cedulas[i])
  print(f"{q_cedula} nota(s) de R$ {cedulas[i]},00")
