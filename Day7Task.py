# FizzBuzz
# bikin 1 function dengan parameter => fizzbuzz(150)
# Jika bilangan kelipatan 3 print Fizz
# Jika bilangan kelipatan 5 print Buzz
# Jika bilangan kelipatan 3 & 5 print FizzBuzz

def fizzbuzz(x):
    for i in range (x):
        if i % 3 == 0 and i % 5 != 0:
            print('Fizz')
        elif i % 3 != 0 and i % 5 == 0 :
            print('Buzz')
        elif i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        else:
            print(i)

fizzbuzz(30)

# buat program yg bisa ngereverse tanpa menggunakan reverse method
x = [1, 2, 3, 4, 5, 6, 7]
y = []

for i in x:
    y.append(x[-i])

print(y)

# ubah huruf vokal jadi o
def vokal(x):
    y = []
    for i in x:
        if i in 'aiue':
            i = 'o'
            y.append(i)
        else:
            y.append(i)
    y = ''.join(y) 
    print(y)

vokal('Lintang')

# Palindrome
def palindrome(x):
    y = x[::-1]
    if x == y:
        print('True')
    else:
        print('False')

palindrome('malam malam')

# buat program yg bisa ngereverse per kata
def balik_kata(x):
    x_list= x.split()
    x_list2 = []
    for i in x_list:
        y = list(i)
        y.reverse()
        z = ''.join(y)
        x_list2.append(z)
    print(' '.join(x_list2))

balik_kata('Aku suka memasak mie goreng')

# bikin program yg ngeubah kata jadi morse
def sandi(x):
    morse = {
        'A' : '• –',
        'B' : '– • • •',
        'C' : '– • – •',
        'D' : '– • •',
        'E' : '•',
        'F' : '• • – •',
        'G' : '– – •',
        'H' : '• • • •',
        'I' : '• •',
        'J' : '• – – –',
        'K' : '– • –',
        'L' : '• – • •',
        'M' : '– –',
        'N' : '– •',
        'O' : '– – –',
        'P' : '• – – •',
        'Q' : '– – • –',
        'R' : '• – •',
        'S' : '• • •',
        'T' : '–',
        'U' : '• • –',
        'V' : '• • • –',
        'W' : '• – –',
        'X' : '– • • –',
        'Y' : '– • – –',
        'Z' : '– – • •',
        ' ' : '/'
        }
    key = list(morse)
    value = list(morse.values())
    y = []
    for i in x:
        if i.upper() in key:
            z = value[key.index(i.upper())]
        y.append(z)
    print(''.join(y))

sandi('Makan Ketoprak')


# Caesar Cipher
def caesar_cipher(kata, move):
    huruf = 'abcdefghijklmnopqrstuvwxyz'
    listnya = list(huruf)
    kata.lower()
    y = []

    for i in kata:
        if i in listnya:
            x = listnya.index(i)
            cipher = move % len(listnya)
            jadinya = listnya[(x + cipher) % len(listnya)]
        else:
            jadinya = i
        y.append(jadinya)
    print(''.join(y))

caesar_cipher('adyan', -3)

# bikin program yg ngeubah kata jadi morse atau morse jadi kata
def sanmor(x):
    morse = {
        'A' : '•–',
        'B' : '–•••',
        'C' : '–•–•',
        'D' : '–••',
        'E' : '•',
        'F' : '••–•',
        'G' : '––•',
        'H' : '••••',
        'I' : '••',
        'J' : '•–––',
        'K' : '–•–',
        'L' : '•–••',
        'M' : '––',
        'N' : '–•',
        'O' : '–––',
        'P' : '•––•',
        'Q' : '––•–',
        'R' : '•–•',
        'S' : '•••',
        'T' : '–',
        'U' : '••–',
        'V' : '•••–',
        'W' : '•––',
        'X' : '–••–',
        'Y' : '–•––',
        'Z' : '––••',
        ' ' : '/'
        }
    key = list(morse)
    value = list(morse.values())
    y = []
    if (x.split())[0] in value:
        x = x.split()
    for i in x:
        if i.upper() in key:
            z = value[key.index(i.upper())]
        else:
            z = key[value.index(i)]
        y.append(z)
    if y[0] in value:
        print(' '.join(y))
    else:
        print(''.join(y))

sanmor('–– •– –•– •– –• / –•– • – ––– •––• •–• •– –•–')