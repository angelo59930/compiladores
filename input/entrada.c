int suma(int a, int b);

float resta(int a, int b);

int main(){

  float a, b = 15651.516;
  int c = 0, d = 8;
  int e = c + d;

  if (e == 8 && e == 2){
    a = 1;
  }
  else{
    a = 0;
  }

  while (a != 1){
    b = a * 5 + 2;
  }

  d = suma(b, e);

  return 0;
}

int suma(int a, int b){
  return a + b;
}

float resta(int a, int b){
  return a - b;
}