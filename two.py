while True:
  try:
    num = int(input("Masukkan jumlah anak ayam yang turun: ")) # form input num
    if num >= 1 and num <= 100:
      break
    else:
      print("Maaf, kamu hanya bisa input angka diantara 1-100") # validation user input
      continue
  except ValueError as err:
    print(err) # print if got some error

print("---------------------------\n") # give some space
print("Tek kotek kotek kotek, anak ayam turun berkotek")
for iter in range (num, 0, -1): # looping num with params (start, stop, step) which is if 'step' is negative and 'start' is bigger than 'stop', then you move through a series of decreasing numbers
  sequence = iter
  sequence_left = sequence - 1 if sequence > 1 else "induknya"
  print("anak ayam turunlah "+str(sequence)+" mati satu tinggallah "+str(sequence_left), end="\n")