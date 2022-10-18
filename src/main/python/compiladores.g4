grammar compiladores;

fragment LETRA: [A-Za-z];
fragment DIGITO: [0-9];
// PUNTO Y COMA
PYC: ';';

COMA: ',';
PUNTO: '.';
ESPACIO: ' ';
// CONTROL DE BLOQUE
LA: '{';
LC: '}';
CA: '[';
CC: ']';
PA: ')';
PC: '(';
// OPERADORES ARITMETICOS
MAS: '+';
MENOS: '-';
PRODUCTO: '*';
DIVISION: '/';
// ASIGNACION
IGUAL: '=';
// COMPARACION
MENOR: '<';
MAYOR: '>';
IGUALDAD: '==';
DISTINTO: '!=';
IF: 'if';
FOR: 'for';
WHILE: 'while';
// TIPO DE DATO
INT: 'int';
FLOAT: 'float';

FLOTANTE: DIGITO PUNTO DIGITO | '-' DIGITO PUNTO DIGITO;
ENTERO: DIGITO+ | '-' DIGITO+;
PALABRA: LETRA+;

WS: [ \t\n\r] -> skip;
OTRO: .;

ID: (LETRA | '_') (LETRA | DIGITO | '_')+;

prog: (prototipado PYC instrucciones | instruccion) EOF;

instrucciones: instruccion instrucciones |;

instruccion:
	bloque
	| funcion // PREGUNTAR QUE HACER CON ESTO
	| declaracion PYC
	| asignacion PYC
	| bloqif
	| bloqfor
	| bloqwhile;

prototipado: tdato ID parametro PC;

funcion: prototipado bloque;

parametro: tdato ID | tdato ID PYC parametro;

bloque: LA instrucciones LC;

declaracion:
	tdato ID
	| tdato asignacion
	| tdato asignacion COMA declaracion
	| tdato ID COMA declaracion;

tdato: INT | FLOAT;

asignacion: ID IGUAL valor;

valor: ENTERO | FLOTANTE;

bloqif: IF comprobacion bloque;

bloqwhile: WHILE comprobacion bloque;

bloqfor:
	FOR PA declaracion PYC control PYC modificacion PC bloque
	| FOR PA PYC control PYC modificacion PC bloque
	| FOR PA PYC PYC modificacion PC bloque
	| FOR PA PYC PYC PC bloque
	| FOR PA declaracion PYC PYC modificacion PC bloque
	| FOR PA declaracion PYC PYC PC bloque;

modificacion: ID IGUAL ID MAS valor | ID IGUAL ID MAS ID;

comprobacion: PA control PC;

control:
	ID MAYOR valor
	| ID MENOR valor
	| ID IGUAL valor
	| ID DISTINTO valor
	| ID MAYOR ID
	| ID MENOR ID
	| ID IGUAL ID
	| ID DISTINTO ID;

