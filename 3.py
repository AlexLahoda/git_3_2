# Option selection
 op=int(input("Ваш вибір (1-8):"))

  if op == 1:
      num1 = float(input("Введіть число: "))
      num2 = float(input("Введіть друге число: "))
      print(add(num1, num2))
      print("\n")

  elif op == 2:
      num1 = float(input("Введіть число: "))
      num2 = float(input("Введіть друге число: "))
      print(subtract(num1, num2))
      print("\n")

  elif op == 3:
      num1 = float(input("Введіть число: "))
      num2 = float(input("Введіть друге число: "))
      print(multiply(num1, num2))
      print("\n")

  elif op == 4:
      num1 = float(input("Введіть число: "))
      num2 = float(input("Введіть друге число: "))
      print(divide(num1, num2))
      print("\n")

  elif op == 5:
      num1 = float(input("Введіть число: "))
      num2 = float(input("Введіть друге число: "))
      print(exponentiation(num1, num2))
      print("\n")

  elif op == 6:
      num1 = float(input("Введіть число: "))
      print(square_root(num1))
      print("\n")

  elif op == 7:
      num1 = float(input("Введіть число: "))
      print(cube_root(num1))
      print("\n")

  elif op == 8:
      break

  else:
      print("Немає такої опції.")
      print("\n")
