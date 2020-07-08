# def safe_pawns(pawns: set) -> int:
#     result = 0
#     lines = [x for x in range(0, 10)]
#     chars = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '']
#     dictionary = dict.fromkeys(lines, [])
#     for i in pawns:
#         dictionary[int(i[1])] = dictionary[int(i[1])] + [(i[0])]
#     print(dictionary)
#     for i in pawns:
#         # print(i)
#         # print(1, chars.index(i[0])-1)
#         # print(2, dictionary[int(i[1])-1])
#         # print(3, chars.index(i[0])+1)
#         # print(4, dictionary[int(i[1])-1])
#         if chars[chars.index(i[0])-1] in dictionary[int(i[1])-1] or chars[chars.index(i[0])+1] in dictionary[int(i[1])-1]:
#             result += 1
#     # print(result)
#     return(result)
#
# -----------------------------------------
def getdiags(pawn):
    c, r = map(ord, pawn)
    return chr(c - 1) + chr(r - 1), chr(c + 1) + chr(r - 1)

def safe_pawns(pawns):
    return len([p for p in pawns if any(d in pawns for d in getdiags(p))])


def safe_pawns(pawns):
    answer = 0
    for pawn in pawns :
        if chr(ord(pawn[0])-1)+str(int(pawn[1])-1) in pawns or chr(ord(pawn[0])+1)+str(int(pawn[1])-1) in pawns : answer +=1
    return answer


def safe_pawns(pawns):
    def is_safe(p):
        file, rank = ord(p[0]), int(p[1])
        return (chr(file - 1) + str(rank - 1) in pawns or
                chr(file + 1) + str(rank - 1) in pawns)

    return sum(is_safe(p) for p in pawns)




if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})  #== 6
    safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})  #== 1
    safe_pawns(["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"])
    safe_pawns(["a8", "b7", "c6", "d5", "e4", "f3", "g2", "h1"])
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
