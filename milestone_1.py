import argparse
from antlr4 import *
from milestone_1Lexer import milestone_1Lexer
from milestone_1Listener import milestone_1Listener
from milestone_1Parser import milestone_1Parser
from antlr4.tree.Trees import Trees

def get_token_type(token):
    switcher = {
        milestone_1Lexer.VARIABLE: "VARIABLE",
        milestone_1Lexer.DIGIT: "DIGIT",
        milestone_1Lexer.ANDD: "AND",
        milestone_1Lexer.ADDR: "ADDR",
        milestone_1Lexer.ASS: "AS",
        milestone_1Lexer.ASM: "ASM",
        milestone_1Lexer.BIND: "BIND",
        milestone_1Lexer.BLOCK: "BLOCK",
        milestone_1Lexer.BREAKK: "BREAK",
        milestone_1Lexer.CASE: "CASE",
        milestone_1Lexer.CAST: "CAST",
        milestone_1Lexer.CONCEPT: "CONCEPT",
        milestone_1Lexer.CONST: "CONST",
        milestone_1Lexer.CONTINUEE: "CONTINUE",
        milestone_1Lexer.CONVERTER: "CONVERTER",
        milestone_1Lexer.DEFER: "DEFER",
        milestone_1Lexer.DISCARD: "DISCARD",
        milestone_1Lexer.DISTINCT: "DISTINCT",
        milestone_1Lexer.DIV: "DIV",
        milestone_1Lexer.DO: "DO",
        milestone_1Lexer.ELIFF: "ELIF",
        milestone_1Lexer.ELSEE: "ELSE",
        milestone_1Lexer.END: "END",
        milestone_1Lexer.ENUM: "ENUM",
        milestone_1Lexer.EXCEPTT: "EXCEPT",
        milestone_1Lexer.EEXPORT: "EXPORT",
        milestone_1Lexer.FINALLYY: "FINALLY",
        milestone_1Lexer.FORR: "FOR",
        milestone_1Lexer.FROM: "FROM",
        milestone_1Lexer.FUNC: "FUNC",
        milestone_1Lexer.IFF: "IF",
        milestone_1Lexer.IIMPORT: "IMPORT",
        milestone_1Lexer.INN: "IN",
        milestone_1Lexer.INCLUDE: "INCLUDE",
        milestone_1Lexer.INTERFACE: "INTERFACE",
        milestone_1Lexer.ISS: "IS",
        milestone_1Lexer.ISNOT: "ISNOT",
        milestone_1Lexer.ITERATOR: "ITERATOR",
        milestone_1Lexer.LET: "LET",
        milestone_1Lexer.MACRO: "MACRO",
        milestone_1Lexer.METHOD: "METHOD",
        milestone_1Lexer.MIXIN: "MIXIN",
        milestone_1Lexer.MOD: "MOD",
        milestone_1Lexer.NIL: "NIL",
        milestone_1Lexer.NOTT: "NOT",
        milestone_1Lexer.NOTIN: "NOTIN",
        milestone_1Lexer.OBJECTT: "OBJECT",
        milestone_1Lexer.OF: "OF",
        milestone_1Lexer.ORR: "OR",
        milestone_1Lexer.OUT: "OUT",
        milestone_1Lexer.PROC: "PROC",
        milestone_1Lexer.PTR: "PTR",
        milestone_1Lexer.RAISEE: "RAISE",
        milestone_1Lexer.REF: "REF",
        milestone_1Lexer.RETURNN: "RETURN",
        milestone_1Lexer.SHL: "SHL",
        milestone_1Lexer.SHR: "SHR",
        milestone_1Lexer.STATIC: "STATIC",
        milestone_1Lexer.TEMPLATE: "TEMPLATE",
        milestone_1Lexer.TRYY: "TRY",
        milestone_1Lexer.TUPLEE: "TUPLE",
        milestone_1Lexer.TYPEE: "TYPE",
        milestone_1Lexer.USING: "USING",
        milestone_1Lexer.WHEN: "WHEN",
        milestone_1Lexer.WHILEE: "WHILE",
        milestone_1Lexer.XOR: "XOR",
        milestone_1Lexer.MINUS_OPERATOR: "MINUS_OPERATOR",
        milestone_1Lexer.DIV_OPERATOR: "DIV_OPERATOR",
        milestone_1Lexer.BITWISE_NOT_OPERATOR: "BITWISE_NOT_OPERATOR",
        milestone_1Lexer.AND_OPERATOR: "AND_OPERATOR",
        milestone_1Lexer.OR_OPERATOR: "OR_OPERATOR",
        milestone_1Lexer.LESS_THAN: "LESS_THAN",
        milestone_1Lexer.GREATER_THAN: "GREATER_THAN",
        milestone_1Lexer.AT: "AT",
        milestone_1Lexer.MODULUS: "MODULUS",
        milestone_1Lexer.NOT_OPERATOR: "NOT_OPERATOR",
        milestone_1Lexer.XOR_OPERATOR: "XOR_OPERATOR",
        milestone_1Lexer.DOT: "DOT",
        milestone_1Lexer.COLON: "COLON",
        milestone_1Lexer.OPEN_PAREN: "OPEN_PAREN",
        milestone_1Lexer.CLOSE_PAREN: "CLOSE_PAREN",
        milestone_1Lexer.OPEN_BRACE: "OPEN_BRACE",
        milestone_1Lexer.CLOSE_BRACE: "CLOSE_BRACE",
        milestone_1Lexer.OPEN_BRACK: "OPEN_BRACK",
        milestone_1Lexer.CLOSE_BRACK: "CLOSE_BRACK",
        milestone_1Lexer.COMMA: "COMMA",
        milestone_1Lexer.SEMI_COLON: "SEMI_COLON",
        milestone_1Lexer.YIELDD: "YIELD",
        milestone_1Lexer.IDENTIFIER: "IDENTIFIER",
        milestone_1Lexer.LETTER: "LETTER",
        milestone_1Lexer.DIGIT: "DIGIT",
        milestone_1Lexer.INT8_LIT: "INT8_LIT",
        milestone_1Lexer.INT16_LIT: "INT16_LIT",
        milestone_1Lexer.INT64_LIT: "INT64_LIT",
        milestone_1Lexer.INT32_LIT: "INT32_LIT",
        milestone_1Lexer.UINT_LIT: "UINT_LIT",
        milestone_1Lexer.UINT8_LIT: "UINT8_LIT",
        milestone_1Lexer.UINT16_LIT: "UINT16_LIT",
        milestone_1Lexer.UINT32_LIT: "UINT32_LIT",
        milestone_1Lexer.UINT64_LIT: "UINT64_LIT",
        milestone_1Lexer.FLOAT32_LIT: "FLOAT32_LIT",
        milestone_1Lexer.FLOAT32_SUFFIX: "FLOAT32_SUFFIX",
        milestone_1Lexer.FLOAT64_LIT: "FLOAT64_LIT",
        milestone_1Lexer.FLOAT64_SUFFIX: "FLOAT64_SUFFIX",
        milestone_1Lexer.FLOAT_LIT: "FLOAT_LIT",
        milestone_1Lexer.EXP: "EXP",
        milestone_1Lexer.INT_LIT: "INT_LIT",
        milestone_1Lexer.HEX_LIT: "HEX_LIT",
        milestone_1Lexer.DEC_LIT: "DEC_LIT",
        milestone_1Lexer.OCT_LIT: "OCT_LIT",
        milestone_1Lexer.BIN_LIT: "BIN_LIT",
        milestone_1Lexer.HEXDIGIT: "HEXDIGIT",
        milestone_1Lexer.OCTDIGIT: "OCTDIGIT",
        milestone_1Lexer.BINDIGIT: "BINDIGIT",
        milestone_1Lexer.EQUALS_OPERATOR: "EQUALS_OPERATOR",
        milestone_1Lexer.ADD_OPERATOR: "ADD_OPERATOR",
        milestone_1Lexer.MUL_OPERATOR: "MUL_OPERATOR",
        milestone_1Lexer.INDENT: "INDENT"
    }
    return switcher.get(token, "ERROR UNKNOWN TOKEN")

def main():

    with open(args.file, "r") as file:
        lines = file.read()
    input_stream = InputStream(lines)
    lexer = milestone_1Lexer(input_stream)
    # token_stream = CommonTokenStream(lexer)
    # parser = milestone_1Parser(token_stream)

 #   tree = parser.start()
 #   print(Trees.toStringTree(tree,None, parser))

    token = lexer.nextToken()
    output_file = open("milestone_1_result.txt", "w+", encoding="utf-8")
    while not token.type == Token.EOF:
        if get_token_type(token):
            output_file.write(get_token_type(token.type) + "  "+token.text + "\n")
        token = lexer.nextToken()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?", metavar="file")

    args = parser.parse_args()

    print(args.file)
	
    main()	