

f = open('data.dat', 'r')

cnt = 0
while 1:
    line = f.readline()
    if not line:
        break;

    ones = 0
    zeros = 0
    for i in line:
        if (i == '1'):
            ones += 1
        else:
            zeros += 1
    zeros -= 1              # skip the EOS(end of string, which is 0)
    # print("ones: " + str(ones) + " zeros: " + str(zeros))
    if ((zeros % 3 == 0) or (ones % 2 == 0)):
        cnt += 1

print(cnt)

# The flag is: 6662
