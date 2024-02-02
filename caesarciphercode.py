letterslow="abcdefghijklmnopqrstuvwxyz"
lettersup="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while True: 
  output=""
  print("""1: Encryption
2: Decryption
Enter Q to exit\n""")

  z = input("Enter your choice: ")
  if (z=="q"or z=="Q"):
    break
  elif (z=="1"):
    msg=str(input("Enter your message: "))
    shift = int(input("Enter shift value: "))%26
    for s in range(len(msg)):
      char=msg[s]
      if (char.isupper()):
        for i in range(len(lettersup)):
          if (char==lettersup[i]):
            output=output+lettersup[(i+shift)%26]
      elif (char.islower()):
        for i in range(len(letterslow)):
          if (char==letterslow[i]):
            output=output+letterslow[(i+shift)%26]
      else:
        output=output + char
    
  elif (z=="2"):
    msg=str(input("Enter your message: "))
    shift = int(input("Enter shift value: "))%26
    for s in range(len(msg)):
      char=msg[s]
      if (char.isupper()):
        for i in range(len(lettersup)):
          if (char==lettersup[i]):
            output=output+lettersup[(i-shift)%26]
      elif (char.islower()):
        for i in range(len(letterslow)):
          if (char==letterslow[i]):
            output=output+letterslow[(i-shift)%26]
      else:
        output=output + char
      
  else:
    print("Input Invalid")
    continue
    
  print("The message is \"" + output + "\"\n")
