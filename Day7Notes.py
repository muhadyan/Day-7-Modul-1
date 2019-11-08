'''
kota = ['Jakarta', 'Bandung', 'Surabaya']

i = 0
while i < len(kota):
    print(kota[i])
    i += 1

# for range
for i in range(len(kota)):
    print(kota[i])

# for in
for namaKota in kota:
    print(namaKota)

x = 'purwadhika'
for i in x:
    print(i)

for i in range(5):
    print(i)

for i in range(2,5):    # (start,stop)
    print(i)

for i in range(2,10,2):    # (start,stop, step)
    print(i)
else:
    print('OK')

for i in range(2,10):
    print(i)
    if i == 7:
        break

for i in range(2,10):
    if i == 7:
        continue
    print(i)            # print nya setelah 'continue'

# print 1-10 angka yg genap jadi 'Wow'
for i in range (11):
    if i % 2 == 0:
        print('Wow')
    else:
        print(i)
'''
