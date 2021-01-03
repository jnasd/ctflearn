

# 1. use HUAWEI honor phone , download apk and run it;
# 2. use online apk decompiler to get the source code,  http://www.javadecompilers.com/
# 3. the most important logic is in the file Parser.java;
# 4. in function parseExpression(), watch line 57-60, the second if (v > 100.0d) never execute, that's the secret.

flags = bytearray()
nums = [1407, 1397, 1400, 1406, 1346, 1400, 1385, 1394, 1382, 1293, 1367, 1368, 1365, 1344, 1354, 1288, 1354, 1382, 1288, 1354, 1382, 1355, 1293, 1357, 1361, 1290, 1355, 1382, 1290, 1368, 1354, 1344, 1382, 1288, 1354, 1367, 1357, 1382, 1288, 1357, 1348]

for i in nums:
    flags.append(chr(i ^ 1337))

print flags
