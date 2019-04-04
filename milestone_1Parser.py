# Generated from milestone_1.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3y")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\6\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class milestone_1Parser ( Parser ):

    grammarFileName = "milestone_1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "' '", "'    '", "'var'", 
                     "'and'", "'addr'", "'as'", "'asm'", "'end'", "'from'", 
                     "'bind'", "'block'", "'break'", "'case'", "'cast'", 
                     "'concept'", "'const'", "'continue'", "'converter'", 
                     "'defer'", "'discard'", "'distinct'", "'div'", "'do'", 
                     "'elif'", "'else'", "'enum'", "'except'", "'export'", 
                     "'finally'", "'for'", "'func'", "'if'", "'import'", 
                     "'in'", "'include'", "'interface'", "'is'", "'isnot'", 
                     "'iterator'", "'let'", "'macro'", "'method'", "'mixin'", 
                     "'mod'", "'nil'", "'not'", "'notin'", "'object'", "'of'", 
                     "'or'", "'out'", "'proc'", "'ptr'", "'raise'", "'ref'", 
                     "'return'", "'shl'", "'shr'", "'static'", "'template'", 
                     "'try'", "'tuple'", "'type'", "'using'", "'when'", 
                     "'while'", "'xor'", "'yield'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'='", "'+'", "'*'", "'-'", "'/'", "'~'", "'&'", "'|'", 
                     "'<'", "'>'", "'@'", "'%'", "'!'", "'^'", "'.'", "':'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "EMPTYSTR", "EMPTYSTR2", "INDENT", "VARIABLE", 
                      "ANDD", "ADDR", "ASS", "ASM", "END", "FROM", "BIND", 
                      "BLOCK", "BREAKK", "CASE", "CAST", "CONCEPT", "CONST", 
                      "CONTINUEE", "CONVERTER", "DEFER", "DISCARD", "DISTINCT", 
                      "DIV", "DO", "ELIFF", "ELSEE", "ENUM", "EXCEPTT", 
                      "EEXPORT", "FINALLYY", "FORR", "FUNC", "IFF", "IIMPORT", 
                      "INN", "INCLUDE", "INTERFACE", "ISS", "ISNOT", "ITERATOR", 
                      "LET", "MACRO", "METHOD", "MIXIN", "MOD", "NIL", "NOTT", 
                      "NOTIN", "OBJECTT", "OF", "ORR", "OUT", "PROC", "PTR", 
                      "RAISEE", "REF", "RETURNN", "SHL", "SHR", "STATIC", 
                      "TEMPLATE", "TRYY", "TUPLEE", "TYPEE", "USING", "WHEN", 
                      "WHILEE", "XOR", "YIELDD", "IDENTIFIER", "LETTER", 
                      "DIGIT", "HEXDIGIT", "OCTDIGIT", "BINDIGIT", "HEX_LIT", 
                      "DEC_LIT", "OCT_LIT", "BIN_LIT", "INT_LIT", "INT8_LIT", 
                      "INT16_LIT", "INT32_LIT", "INT64_LIT", "UINT_LIT", 
                      "UINT8_LIT", "UINT16_LIT", "UINT32_LIT", "UINT64_LIT", 
                      "EXP", "FLOAT_LIT", "FLOAT32_SUFFIX", "FLOAT32_LIT", 
                      "FLOAT64_SUFFIX", "FLOAT64_LIT", "EQUALS_OPERATOR", 
                      "ADD_OPERATOR", "MUL_OPERATOR", "MINUS_OPERATOR", 
                      "DIV_OPERATOR", "BITWISE_NOT_OPERATOR", "AND_OPERATOR", 
                      "OR_OPERATOR", "LESS_THAN", "GREATER_THAN", "AT", 
                      "MODULUS", "NOT_OPERATOR", "XOR_OPERATOR", "DOT", 
                      "COLON", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACE", 
                      "CLOSE_BRACE", "OPEN_BRACK", "CLOSE_BRACK", "COMMA", 
                      "SEMI_COLON" ]

    RULE_start = 0

    ruleNames =  [ "start" ]

    EOF = Token.EOF
    EMPTYSTR=1
    EMPTYSTR2=2
    INDENT=3
    VARIABLE=4
    ANDD=5
    ADDR=6
    ASS=7
    ASM=8
    END=9
    FROM=10
    BIND=11
    BLOCK=12
    BREAKK=13
    CASE=14
    CAST=15
    CONCEPT=16
    CONST=17
    CONTINUEE=18
    CONVERTER=19
    DEFER=20
    DISCARD=21
    DISTINCT=22
    DIV=23
    DO=24
    ELIFF=25
    ELSEE=26
    ENUM=27
    EXCEPTT=28
    EEXPORT=29
    FINALLYY=30
    FORR=31
    FUNC=32
    IFF=33
    IIMPORT=34
    INN=35
    INCLUDE=36
    INTERFACE=37
    ISS=38
    ISNOT=39
    ITERATOR=40
    LET=41
    MACRO=42
    METHOD=43
    MIXIN=44
    MOD=45
    NIL=46
    NOTT=47
    NOTIN=48
    OBJECTT=49
    OF=50
    ORR=51
    OUT=52
    PROC=53
    PTR=54
    RAISEE=55
    REF=56
    RETURNN=57
    SHL=58
    SHR=59
    STATIC=60
    TEMPLATE=61
    TRYY=62
    TUPLEE=63
    TYPEE=64
    USING=65
    WHEN=66
    WHILEE=67
    XOR=68
    YIELDD=69
    IDENTIFIER=70
    LETTER=71
    DIGIT=72
    HEXDIGIT=73
    OCTDIGIT=74
    BINDIGIT=75
    HEX_LIT=76
    DEC_LIT=77
    OCT_LIT=78
    BIN_LIT=79
    INT_LIT=80
    INT8_LIT=81
    INT16_LIT=82
    INT32_LIT=83
    INT64_LIT=84
    UINT_LIT=85
    UINT8_LIT=86
    UINT16_LIT=87
    UINT32_LIT=88
    UINT64_LIT=89
    EXP=90
    FLOAT_LIT=91
    FLOAT32_SUFFIX=92
    FLOAT32_LIT=93
    FLOAT64_SUFFIX=94
    FLOAT64_LIT=95
    EQUALS_OPERATOR=96
    ADD_OPERATOR=97
    MUL_OPERATOR=98
    MINUS_OPERATOR=99
    DIV_OPERATOR=100
    BITWISE_NOT_OPERATOR=101
    AND_OPERATOR=102
    OR_OPERATOR=103
    LESS_THAN=104
    GREATER_THAN=105
    AT=106
    MODULUS=107
    NOT_OPERATOR=108
    XOR_OPERATOR=109
    DOT=110
    COLON=111
    OPEN_PAREN=112
    CLOSE_PAREN=113
    OPEN_BRACE=114
    CLOSE_BRACE=115
    OPEN_BRACK=116
    CLOSE_BRACK=117
    COMMA=118
    SEMI_COLON=119

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(milestone_1Parser.VARIABLE, 0)

        def getRuleIndex(self):
            return milestone_1Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = milestone_1Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(milestone_1Parser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





