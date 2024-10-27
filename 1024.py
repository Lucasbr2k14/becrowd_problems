n = int(input())

def cript(string:str) -> str:
  list_string = [] 

  for i in range(len(string)):
    char = ord(string[i])

    if((char >= ord('a') and char <= ord('z')) or (char >= ord('A') and char <= ord('Z'))):
      list_string.append(chr(char+3))
    else:
      list_string.append(chr(char))

  list_string = list_string[::-1]
  
  center = len(list_string) // 2
  
  for i in range(center, len(list_string)):
    list_string[i] = chr(ord(list_string[i]) - 1)  

  return ''.join(list_string)

for i in range(n):
  inp = input() 
  print(cript(inp))
