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
PUNTO: '.';
INCREMENTO: '++';
DECREMENTO: '--';

MENOR: '<';
MAYOR: '>';
IGUALDAD: '==';
DISTINTO: '!=';
AND: '&&';
OR: '||';

INT: 'int';
FLOAT: 'float';

IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';

// NUMERO = 6.+981298+1+6
NUMERO:
	DIGITO+
	| '-' DIGITO+
	| DIGITO+ PUNTO DIGITO+
	| '-' DIGITO+ PUNTO DIGITO+;

RETORNO: 'return';

ID: (LETRA | '_') (LETRA | DIGITO | '_')*;

WS: [ \t\n\r] -> skip;

programa: instrucciones EOF;

instrucciones: instruccion instrucciones |;

instruccion:
	bloque
	| declaracion PYC
	| asignacion PYC
	| incrementoUnario PYC
	| decrementoUnario PYC
	| bloqueif
	| bloquewhile
	| bloquefor
	| prototipado PYC
	| funcion
	| llamadaFuncion PYC
	| asignarFuncion PYC;

bloque:
	LLA instrucciones LLC
	| LLA instrucciones retorno PYC LLC;

retorno: RETORNO | RETORNO ID | RETORNO NUMERO | RETORNO oparit;

prototipado: tdato ID PA (argumentos |) PC;

argumentos: argumento | argumento COMA argumentos |;

argumento: tdato ID;

funcion: prototipado bloque;

parametros:
	ID
	| ID COMA parametros
	| NUMERO COMA parametros
	| NUMERO
	|;

llamadaFuncion: ID PA (parametros |) PC | ID PA PC;

bloquefor:
	FOR PA (declaracion | asignacion) PYC cmp PYC asignacion PC bloque
	| FOR PA PYC PYC PYC PC
	| FOR PA (declaracion | asignacion) PYC PYC asignacion PC bloque
	| FOR PA (declaracion | asignacion) PYC cmp PYC PC bloque
	| FOR PA (declaracion | asignacion) PYC PYC PC bloque
	| FOR PA PYC cmp PYC asignacion PC bloque
	| FOR PA PYC PYC asignacion PC bloque;

bloquewhile: WHILE control bloque;

bloqueif: IF control bloque | IF control bloque bloqueElse;

bloqueElse: ELSE bloque;

declaracion:
	tdato ID
	| tdato init
	| tdato init conDeclaracion
	| tdato ID conDeclaracion;

conDeclaracion:
	COMA ID
	| COMA ID conDeclaracion
	| COMA init conDeclaracion
	|;

init: ID ASSIG NUMERO | ID ASSIG itop | ID ASSIG llamadaFuncion;

asignacion: ID ASSIG NUMERO | ID ASSIG itop;

asignarFuncion: ID ASSIG llamadaFuncion;

tdato: INT | FLOAT;

itop: oparit itop |;
// c = a + b + d + f / r * q
oparit: exp;

exp: term t;

term: factor f;

t: SUMA term t | REST term t |;

factor: ID | NUMERO | PA exp PC;

f: MULT factor f | DIV factor f |;

control: PA cmps PC;

cmps: cmp | cmp AND cmps | cmp OR cmps;

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

incrementoUnario: ID INCREMENTO;

decrementoUnario: ID DECREMENTO;