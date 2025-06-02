#include <stdio.h>
#define SEPARATOR "-----------------------------"

int main () {
  
  printf("%s\n", SEPARATOR);
  printf("| Pattern painter \n");
  printf("%s\n", SEPARATOR);

  int column;
  int rows;
  char symbole;
  
  printf("\nHow many column: ");
  scanf("%d", &column);

  printf("\nHow many rows: ");
  scanf("%d", &rows);

  printf("\nWhich symbole: ");
  scanf(" %c", &symbole);
  
  printf("\nResult:\n%s\n", SEPARATOR);
  for(int i = 0; column > i; i++){
    for(int j = 0; rows > j; j++){
      printf("%c", symbole);
    }
    printf("\n");
  }
  printf("%s\n", SEPARATOR);
}
