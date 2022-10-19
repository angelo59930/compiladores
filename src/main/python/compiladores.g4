grammar compiladores;

fragment LETRA: [A-Za-z];
fragment DIGITO: [0-9];

PA: '(';
PC: ')';
LLA: '{';
LLC: '}';
PYC: ';';
COMA: ',';
ASSIG: '=';
SUMA: '+';
MULT: '*';
REST: '-';
DIV: '/';

MENOR: '<';
MAYOR: '>';
IGUALDAD: '==';
DISTINTO: '!=';

INT: 'int';

IF: 'if';
WHILE: 'while';
FOR: 'for';

NUMERO: DIGITO+;

ID: (LETRA | '_') (LETRA | DIGITO | '_')*;

WS: [ \t\n\r] -> skip;

programa: instrucciones EOF;

instrucciones: instruccion instrucciones |;

instruccion:
	bloque
	| declaracion PYC
	| asignacion PYC
	| bloqueif
	| bloquewhile
	| bloquefor;

bloque: LLA instrucciones LLC;

bloquefor:
	FOR PA (declaracion | asignacion) PYC cmp PYC asignacion PC bloque;

bloquewhile: WHILE control bloque;

bloqueif: IF control bloque;

declaracion:
	tdato ID
	| tdato asignacion
	| declaracion COMA asignacion
	|;

asignacion: ID ASSIG NUMERO | ID ASSIG itop;

tdato: INT;

itop: oparit itop |;
// c = a + b + d + f / r * q
oparit: exp;

exp: term t;

term: factor f;

t: SUMA term t | REST term t |;

factor: ID | NUMERO | PA exp PC;

f: MULT factor f | DIV factor f |;

control: PA cmp PC;

cmp:
	ID MAYOR NUMERO
	| ID MENOR NUMERO
	| ID IGUALDAD NUMERO
	| ID DISTINTO NUMERO
	| ID MAYOR ID
	| ID MENOR ID
	| ID IGUALDAD ID
	| ID DISTINTO ID
	| NUMERO MAYOR ID
	| NUMERO MENOR ID
	| NUMERO IGUALDAD ID
	| NUMERO DISTINTO ID;