grammar compiladores;

fragment LETRA: [A-Za-z];
fragment DIGITO: [0-9];

PA: '(';
PC: ')';
LLA: '{';
LLC: '}';
PYC: ';';
ASSIG: '=';
SUMA: '+';
MULT: '*';
REST: '-';

INT: 'int';

NUMERO: DIGITO+;

ID: (LETRA | '_') (LETRA | DIGITO | '_')*;

WS: [ \t\n\r] -> skip;

programa: instrucciones EOF;

instrucciones: instruccion instrucciones |;

instruccion: bloque | declaracion PYC | asignacion PYC;
// | bloqueif | bloquefor | bloquewhile;

bloque: LLA instrucciones LLC;

asignacion: ID ASSIG NUMERO
					| ID ASSIG itop;

declaracion:
	tdato ID
	| tdato asignacion
	|; // | tdato ID ASSIG ... ?

tdato: INT;

itop: oparit itop |;
// c = a + b + d + f / r * q
oparit: exp;

exp: term t;

term: factor f;

t: SUMA term t | REST term t |;

factor: ID | NUMERO | PA exp PC;

f: MULT factor f |;
