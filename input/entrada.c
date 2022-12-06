int suma (int a, int b);

int resta (int a, int b);

int main(){

  int a, b;
  int c = 0, d = 8;
  int e = c + d;

  if(e == 8){
    a = 1;
  }else{
    a = 0;
  }

  while(a != 1){
    b = a * 5 + 2;
    a++;
  }

  d = suma(b, e);

  return 0;
}

int suma(int a, int b){
  return a + b;
}

int resta(int a, int b){
  return a - b;
}