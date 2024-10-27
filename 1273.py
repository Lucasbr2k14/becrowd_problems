def get_major_strig(strings:list[str]) -> tuple[int]:
  major:int = len(strings[0])
  index:int = 0
  for i in range(len(strings)):
    if len(strings[i]) > major:
      major = len(strings[i])
      index = i
  return index, major

def insert_spaces(string:str, num) -> str:
  string_result:str = ""
  for i in range(num):
    string_result += ' '
  string_result += string
  return string_result

def justified(strings:list[str]) -> list[str]:
  major_string:tuple[int] = get_major_strig(strings)
  list_results: list[str] = []
  for i in range(len(strings)):
    spaces:int = major_string[1] - len(strings[i])
    list_results.append(insert_spaces(strings[i], spaces))
  return list_results

run:bool = True
i_i:int = 0

while run:
  i_i += 1
  n:int = int(input())

  if n > 0:
    if(i_i != 1):
      print()
    
    list_strings:list[str] = []

    for i in range(n):
      input_str:str = input() 
      list_strings.append(input_str)
    
    justi = justified(list_strings)
    
    for i in range(len(justi)):
      print(justi[i])    

  else:
    run = False
