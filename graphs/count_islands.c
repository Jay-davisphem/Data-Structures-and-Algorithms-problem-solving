#include <stdio.h>

char count_islands(char * grid[2][3]){
  return grid[1][2];
}

int main(int argc, char ** argv){
  char * grid[2][3] = {
    {'w', 'l', 'w'},
    {'w', 'w', 'l'}
  };
  printf("%c", count_islands(grid));
}
