n = int(input())

for i in range(n):
  number_input = input().split(" ")

  print(f"Case {i+1}:")

  if number_input[1] == "bin":
    dec = int(number_input[0], 2)
    print(f"{dec} dec")
    print(f"{dec:x} hex")

  if number_input[1] == "dec":
    dec = int(number_input[0])
    print(f"{dec:x} hex")
    print(f"{dec:b} bin")

  if number_input[1] == "hex":
    dec = int(number_input[0], 16)
    print(f"{dec} dec")
    print(f"{dec:b} bin")

  print("\n", end='')
