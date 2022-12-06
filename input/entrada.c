int suma(int k, int j);

int resta(int x, int j);

int main(int arg, int argv){

  int a;
  int b;
  int c;

  a = 2;

  b = resta(a, c);

  c = a + b;


  if(a > 2){
    a = a + 1;
  }
  else {
    a = 2;
  }

  while( a == 2){
    a = a + 1;
  }


  return a + b;
}

int suma(int k, int j){
  return k + j;
}

int resta(int x, int j){
  return x - j; 
}
