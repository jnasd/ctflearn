
#src = 'ctf~|'
#src = 'lemon>>^|&'
src = 'binaryrefinery|&&>>|^^^&&||~'
operands = list()
operators = list()

j = 0
for i in range(len(src)):
    if (j != i):
        continue;
    letter = src[i]
    j += 1
    if (letter.isalpha()):
        exponent = ord(letter)**3
        operands.append(exponent)
    else:
        if (letter == '~'):
            operators.append("neg")
        elif (letter == '&'):
            operators.append("and")
        elif (letter == '|'):
            operators.append("or")
        elif (letter == '^'):
            operators.append("xor")
        elif (letter == '>'):
            operators.append("shr")
            j += 1                                  # skip another > for operator '>>'
        else:
            print("Not supported operator!")
            exit(-1)
            
print("src statement: " + str(src))
print("operands : " + str(operands))
print("operators : " + str(operators))

rank_total = len(operators)

rank = 0
v0 = operands[0]
second_start = 1                        # every rank, second operand's start position increment
while (rank < rank_total):
    current_second = second_start       # position of the second operand
    for operator in operators:
        if (operator in ["and", "or", "xor", "shr"]):
            #print("operator: " + operator + " " + str(v0) + "and" + str(second))
            operand1 = v0
            operand2 = operands[current_second]
            if (operator == "shr"):
                v0 = operand1 >> operand2
            elif (operator == "or"):
                v0 = operand1 | operand2
            elif (operator == "xor"):
                v0 = operand1 ^ operand2
            elif (operator == "and"):
                v0 = operand1 & operand2
            else:
                print("something wrong!")
                exit(-1)
            current_second += 1
        elif (operator == "neg"):
            v0 = ~v0
            current_second += 1
        else:
            print("Not supported operator!")
            exit(-1)
        
    second_start += 1                       # every rank, second operand's start position increment
    operators.pop(0)
    print("rank: " + str(rank) + ",v0: " + str(v0))
    rank += 1
