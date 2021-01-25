#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <malloc.h>

// created by python(create_str.py)
char str[84];
void init_str()
{
str[0] = 8;
str[1] = 0;
str[2] = 0;
str[3] = 0;
str[4] = 6;
str[5] = 0;
str[6] = 0;
str[7] = 0;
str[8] = 44;
str[9] = 0;
str[10] = 0;
str[11] = 0;
str[12] = 58;
str[13] = 0;
str[14] = 0;
str[15] = 0;
str[16] = 50;
str[17] = 0;
str[18] = 0;
str[19] = 0;
str[20] = 48;
str[21] = 0;
str[22] = 0;
str[23] = 0;
str[24] = 28;
str[25] = 0;
str[26] = 0;
str[27] = 0;
str[28] = 92;
str[29] = 0;
str[30] = 0;
str[31] = 0;
str[32] = 1;
str[33] = 0;
str[34] = 0;
str[35] = 0;
str[36] = 50;
str[37] = 0;
str[38] = 0;
str[39] = 0;
str[40] = 26;
str[41] = 0;
str[42] = 0;
str[43] = 0;
str[44] = 18;
str[45] = 0;
str[46] = 0;
str[47] = 0;
str[48] = 69;
str[49] = 0;
str[50] = 0;
str[51] = 0;
str[52] = 29;
str[53] = 0;
str[54] = 0;
str[55] = 0;
str[56] = 32;
str[57] = 0;
str[58] = 0;
str[59] = 0;
str[60] = 48;
str[61] = 0;
str[62] = 0;
str[63] = 0;
str[64] = 13;
str[65] = 0;
str[66] = 0;
str[67] = 0;
str[68] = 27;
str[69] = 0;
str[70] = 0;
str[71] = 0;
str[72] = 3;
str[73] = 0;
str[74] = 0;
str[75] = 0;
str[76] = 124;
str[77] = 0;
str[78] = 0;
str[79] = 0;
str[80] = 19;
str[81] = 0;
str[82] = 0;
str[83] = 0;
}

void main()
{
	char *key2 = (char *)malloc(84);
	char msg[21];
	char * key = (char *)malloc(0x16);
	
	memset(key, 0, sizeof(key));
	strcpy(key, "IdontKnowWhatsGoingOn");

	init_str();

	int local_10 = 0;
	while (local_10 < 0x16)
	{
		*(int *)(key2 + (long)local_10 * 4) = (int)key[local_10];
		msg[local_10] =
			*(char *)(key2 + (long)local_10 * 4) ^
			*(char *)(str + (long)local_10 * 4);
		local_10 = local_10 + 1;
	}

	printf("%s\n", msg);
}
