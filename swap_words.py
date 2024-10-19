def reverse_words_order_and_swap_cases(sentence):
    a = sentence.split(" ")
    b = []
    for i in reversed(range(len(a))):
        b.append(a[i])
    c = ""
    for j in b:
        c += j + " "
    print(c.swapcase())

if __name__ == '__main__':
   reverse_words_order_and_swap_cases("aWESOME is cODING")
