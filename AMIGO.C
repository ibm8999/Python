/*
   calcula numero amigos
*/

#include <stdio.h>

int main()

{
 int k,g,h,j,limite,liminf;
 float cal;
printf("Límite inferior");
scanf("%d",&liminf);
printf("Límite superior");
scanf("%d",&limite);

for (k=liminf;k!=limite;k++)
    {
/*      printf("k vale %d",k); */
	g=0;
 	for (j=k/2;j!=0;j--)
	{
	  cal=(float)k/j;
          if (k/j==cal) 
             g=g+j;
	}
/*   printf("la suma de divisores de %d es %d \n",k,g); */
        h=0;
	for (j=g/2;j!=0;j--)
	{
          cal=(float)g/j;
	  if (g/j==cal) 
             h=h+j;
	}
/*
      printf("la suma de divisores de %d es %d \n",g,h);
        printf("voy por %d",k); */

        if (k==h)  printf("Los numeros %d y %d son amigos\n",k,g);
    }
}
		
	
