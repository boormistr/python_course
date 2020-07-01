text = input('Enter the text: ').split()
n = 0
for i in text:
    print(n, ': ', i[:10], sep='')
    n += 1