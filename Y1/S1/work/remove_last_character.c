#include <stdio.h>
#include <string.h>
int main() {
  char name[100];
  //printf("");
  scanf("%s", &name);
  while (name[strlen(name)-1 != '\0']) {
  name[strlen(name)-1] = '\0';
  printf("%s\n",name);
  }
}
