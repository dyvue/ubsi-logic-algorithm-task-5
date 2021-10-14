while True:
  try:
    num = int(input("Masukkan jumlah baris yang ingin ditampilkan: ")) # form input num
    if num >= 1 and num <= 100:
      char = input("Masukkan sebuah karakter untuk pola: ") # form input what characters what you want 
      limit = num # declaration var limit
      break
    else:
      print("Maaf, kamu hanya bisa input angka diantara 1-100") # validation user input
      continue
  except ValueError as err:
    print(err) # print if got some error

print("---------------------------\n") # give some space
for iter in range (0, num): # looping the number of num
  for space in range (0, limit+1): # looping space / make shape of isoceles triangle perfectly
    print(" ", end="")
  
  for shape in range (0, iter+1): # looping an iter number per row of shape
    print(char+" ", end="")

  limit-=1 # decreases the limit every iteration
  print("")