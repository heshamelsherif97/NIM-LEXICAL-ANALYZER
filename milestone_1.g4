grammar milestone_1;

COMMENT2 : ' '* '#'+ '[' .*? ']' '#'+ ' '* -> skip;
COMMENT : ' '* '#'+ .*? [\n\r] ' '* -> skip;
EMPTYSTR : [\n\r] -> skip;
INDENT : ('    ')+;
EMPTYSTR2 : ' '+ -> skip;
start : VARIABLE;
VARIABLE : 'var';
ANDD : 'and';
ADDR : 'addr';
ASS : 'as';
ASM : 'asm';
END : 'end';
FROM : 'from';
BIND : 'bind';
BLOCK : 'block';
BREAKK : 'break';
CASE : 'case';
CAST : 'cast';
CONCEPT : 'concept';
CONST : 'const';
CONTINUEE : 'continue';
CONVERTER : 'converter';
DEFER : 'defer';
DISCARD : 'discard';
DISTINCT : 'distinct';
DIV : 'div';
DO : 'do';
ELIFF :  'elif';
ELSEE : 'else';
ENUM : 'enum';
EXCEPTT : 'except';
EEXPORT : 'export';
FINALLYY : 'finally';
FORR : 'for';
FUNC : 'func';
IFF : 'if';
IIMPORT : 'import';
INN : 'in';
INCLUDE : 'include';
INTERFACE : 'interface';
ISS : 'is';
ISNOT : 'isnot';
ITERATOR : 'iterator';
LET : 'let';
MACRO : 'macro';
METHOD : 'method';
MIXIN : 'mixin';
MOD : 'mod';
NIL : 'nil';
NOTT : 'not';
NOTIN : 'notin';
OBJECTT : 'object';
OF : 'of';
ORR : 'or';
OUT : 'out';
PROC : 'proc';
PTR : 'ptr';
RAISEE : 'raise';
REF : 'ref';
RETURNN : 'return';
SHL : 'shl';
SHR : 'shr';
STATIC : 'static';
TEMPLATE : 'template';
TRYY : 'try';
TUPLEE : 'tuple';
TYPEE : 'type';
USING : 'using';
WHEN : 'when';
WHILEE : 'while';
XOR : 'xor';
YIELDD : 'yield';
IDENTIFIER : (LETTER)+ (('_') | (LETTER|DIGIT))*;
LETTER : [A-Za-z\u0080-\u00ff];
DIGIT : [0-9];

INT_LIT : HEX_LIT
        | DEC_LIT
        | OCT_LIT
        | BIN_LIT;

INT8_LIT : INT_LIT '\'' ('i' | 'I') '8';
INT16_LIT : INT_LIT '\'' ('i' | 'I') '16';
INT32_LIT : INT_LIT '\'' ('i' | 'I') '32';
INT64_LIT : INT_LIT '\'' ('i' | 'I') '64';

UINT_LIT : INT_LIT '\'' ('u' | 'U');
UINT8_LIT : INT_LIT '\'' ('u' | 'U') '8';
UINT16_LIT : INT_LIT '\'' ('u' | 'U') '16';
UINT32_LIT : INT_LIT '\'' ('u' | 'U') '32';
UINT64_LIT : INT_LIT '\'' ('u' | 'U') '64';

EXP : ('e' | 'E' ) ('+' | '-') DIGIT ( '_' DIGIT )*;
FLOAT_LIT : DIGIT ('_' DIGIT)* (('.' DIGIT ('_' DIGIT)* EXP) |EXP);
FLOAT32_SUFFIX : ('f' | 'F') '32';
FLOAT32_LIT : HEX_LIT '\'' FLOAT32_SUFFIX
            | (FLOAT_LIT | DEC_LIT | OCT_LIT | BIN_LIT) '\'' FLOAT32_LIT;
FLOAT64_SUFFIX : ( ('f' | 'F') '64' ) | 'd' | 'D';
FLOAT64_LIT : HEX_LIT '\'' FLOAT64_LIT
            | (FLOAT_LIT | DEC_LIT | OCT_LIT | BIN_LIT) '\'' FLOAT64_SUFFIX;


HEX_LIT : '0' ('x' | 'X' ) DIGIT | [A-Fa-f] ( '_' DIGIT | [A-Fa-f] )*;
DEC_LIT : DIGIT ( ('_') DIGIT )*;
OCT_LIT : '0' 'o' [0-7] ( '_' [0-7] )*;
BIN_LIT : '0' ('b' | 'B' ) [0-1] ( '_' [0-1] )*;

EQUALS_OPERATOR : '=';
ADD_OPERATOR : '+';
MUL_OPERATOR : '*';
MINUS_OPERATOR : '-';
DIV_OPERATOR : '/';
BITWISE_NOT_OPERATOR : '~';
AND_OPERATOR : '&';
OR_OPERATOR : '|';
LESS_THAN : '<';
GREATER_THAN : '>';
AT : '@';
MODULUS : '%';
NOT_OPERATOR : '!';
XOR_OPERATOR : '^';
DOT : '.';
COLON : ':';
OPEN_PAREN : '(';
CLOSE_PAREN : ')';
OPEN_BRACE : '{';
CLOSE_BRACE : '}';
OPEN_BRACK : '[';
CLOSE_BRACK : ']';
COMMA : ',';
SEMI_COLON : ';';
STR_LIT : '"' (.)*? '"';
CHAR_LIT : '\'' (.)*? '\'';
TRIPLESTR_LIT : '"""' (.)*? '"""';
RSTR_LIT : ('r'|'R') '"' (.)*? '"';