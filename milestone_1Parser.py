# Generated from milestone_1.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3}")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7M\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class milestone_1Parser ( Parser ):

    grammarFileName = "milestone_1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'var'", "'and'", 
                     "'addr'", "'as'", "'asm'", "'end'", "'from'", "'bind'", 
                     "'block'", "'break'", "'case'", "'cast'", "'concept'", 
                     "'const'", "'continue'", "'converter'", "'defer'", 
                     "'discard'", "'distinct'", "'div'", "'do'", "'elif'", 
                     "'else'", "'enum'", "'except'", "'export'", "'finally'", 
                     "'for'", "'func'", "'if'", "'import'", "'in'", "'include'", 
                     "'interface'", "'is'", "'isnot'", "'iterator'", "'let'", 
                     "'macro'", "'method'", "'mixin'", "'mod'", "'nil'", 
                     "'not'", "'notin'", "'object'", "'of'", "'or'", "'out'", 
                     "'proc'", "'ptr'", "'raise'", "'ref'", "'return'", 
                     "'shl'", "'shr'", "'static'", "'template'", "'try'", 
                     "'tuple'", "'type'", "'using'", "'when'", "'while'", 
                     "'xor'", "'yield'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'*'", "'-'", "'/'", "'~'", "'&'", 
                     "'|'", "'<'", "'>'", "'@'", "'%'", "'!'", "'^'", "'.'", 
                     "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "COMMENT3", "COMMENT2", "COMMENT", "EMPTYSTR", 
                      "INDENT", "EMPTYSTR2", "VARIABLE", "ANDD", "ADDR", 
                      "ASS", "ASM", "END", "FROM", "BIND", "BLOCK", "BREAKK", 
                      "CASE", "CAST", "CONCEPT", "CONST", "CONTINUEE", "CONVERTER", 
                      "DEFER", "DISCARD", "DISTINCT", "DIV", "DO", "ELIFF", 
                      "ELSEE", "ENUM", "EXCEPTT", "EEXPORT", "FINALLYY", 
                      "FORR", "FUNC", "IFF", "IIMPORT", "INN", "INCLUDE", 
                      "INTERFACE", "ISS", "ISNOT", "ITERATOR", "LET", "MACRO", 
                      "METHOD", "MIXIN", "MOD", "NIL", "NOTT", "NOTIN", 
                      "OBJECTT", "OF", "ORR", "OUT", "PROC", "PTR", "RAISEE", 
                      "REF", "RETURNN", "SHL", "SHR", "STATIC", "TEMPLATE", 
                      "TRYY", "TUPLEE", "TYPEE", "USING", "WHEN", "WHILEE", 
                      "XOR", "YIELDD", "IDENTIFIER", "LETTER", "DIGIT", 
                      "INT8_LIT", "INT16_LIT", "INT32_LIT", "INT64_LIT", 
                      "UINT_LIT", "UINT8_LIT", "UINT16_LIT", "UINT32_LIT", 
                      "UINT64_LIT", "EXP", "FLOAT32_SUFFIX", "FLOAT32_LIT", 
                      "FLOAT64_LIT", "FLOAT_LIT", "FLOAT64_SUFFIX", "INT_LIT", 
                      "HEX_LIT", "DEC_LIT", "OCT_LIT", "BIN_LIT", "EQUALS_OPERATOR", 
                      "ADD_OPERATOR", "MUL_OPERATOR", "MINUS_OPERATOR", 
                      "DIV_OPERATOR", "BITWISE_NOT_OPERATOR", "AND_OPERATOR", 
                      "OR_OPERATOR", "LESS_THAN", "GREATER_THAN", "AT", 
                      "MODULUS", "NOT_OPERATOR", "XOR_OPERATOR", "DOT", 
                      "COLON", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACE", 
                      "CLOSE_BRACE", "OPEN_BRACK", "CLOSE_BRACK", "COMMA", 
                      "SEMI_COLON", "STR_LIT", "CHAR_LIT", "TRIPLESTR_LIT", 
                      "RSTR_LIT" ]

    RULE_start = 0

    ruleNames =  [ "start" ]

    EOF = Token.EOF
    COMMENT3=1
    COMMENT2=2
    COMMENT=3
    EMPTYSTR=4
    INDENT=5
    EMPTYSTR2=6
    VARIABLE=7
    ANDD=8
    ADDR=9
    ASS=10
    ASM=11
    END=12
    FROM=13
    BIND=14
    BLOCK=15
    BREAKK=16
    CASE=17
    CAST=18
    CONCEPT=19
    CONST=20
    CONTINUEE=21
    CONVERTER=22
    DEFER=23
    DISCARD=24
    DISTINCT=25
    DIV=26
    DO=27
    ELIFF=28
    ELSEE=29
    ENUM=30
    EXCEPTT=31
    EEXPORT=32
    FINALLYY=33
    FORR=34
    FUNC=35
    IFF=36
    IIMPORT=37
    INN=38
    INCLUDE=39
    INTERFACE=40
    ISS=41
    ISNOT=42
    ITERATOR=43
    LET=44
    MACRO=45
    METHOD=46
    MIXIN=47
    MOD=48
    NIL=49
    NOTT=50
    NOTIN=51
    OBJECTT=52
    OF=53
    ORR=54
    OUT=55
    PROC=56
    PTR=57
    RAISEE=58
    REF=59
    RETURNN=60
    SHL=61
    SHR=62
    STATIC=63
    TEMPLATE=64
    TRYY=65
    TUPLEE=66
    TYPEE=67
    USING=68
    WHEN=69
    WHILEE=70
    XOR=71
    YIELDD=72
    IDENTIFIER=73
    LETTER=74
    DIGIT=75
    INT8_LIT=76
    INT16_LIT=77
    INT32_LIT=78
    INT64_LIT=79
    UINT_LIT=80
    UINT8_LIT=81
    UINT16_LIT=82
    UINT32_LIT=83
    UINT64_LIT=84
    EXP=85
    FLOAT32_SUFFIX=86
    FLOAT32_LIT=87
    FLOAT64_LIT=88
    FLOAT_LIT=89
    FLOAT64_SUFFIX=90
    INT_LIT=91
    HEX_LIT=92
    DEC_LIT=93
    OCT_LIT=94
    BIN_LIT=95
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
    STR_LIT=120
    CHAR_LIT=121
    TRIPLESTR_LIT=122
    RSTR_LIT=123

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(milestone_1Parser.DIGIT, 0)

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
            self.match(milestone_1Parser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





