

operations = bytearray("++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++.----------->@>>.<@<<<.@<@<@<++++<.<@<@<<@<-----.<<<<<.<@<@<+<.+>@.-------.-------->>>.<@<@<++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++>>>.<@<@<<.-----------<.>@>@<@><<.>@>@++++<.>@-----.>>>.<@<@<+<.>@+.-------.--------.+++++++++++++>>>>>>.<@<@<@<@<@<<.>@++.-------<.>@+++++++<<<.>@>@>@<<.>@>@<.>@-<.>@++++++++++++<<<.>@>@>@+++++++++++", 'utf8')

buf = bytearray(1)
buf[0] = 0

for i in range(len(operations)):
    if (operations[i] == ord('+')):
        count = len(buf)
        buf[count - 1] += 1
    elif (operations[i] == ord('-')):
        count = len(buf)
        buf[count - 1] -= 1
    elif (operations[i] == ord('.')):
        count = len(buf)
        last_value = buf[count - 1]
        buf.append(last_value)
    elif (operations[i] == ord('@')):
        count = len(buf)
        last1 = buf.pop(-1)
        last2 = buf.pop(-1)
        buf.append(last1)
        buf.append(last2)
    elif (operations[i] == ord('>')):
        first_value = buf.pop(0)
        buf.append(first_value)
    elif (operations[i] == ord('<')):
        last_value = buf.pop(-1)
        buf.insert(0, last_value)
    else:
        print("wrong operation!")
        print(chr(operations[i]))

print(buf)
