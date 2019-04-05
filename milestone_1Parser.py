# Generated from milestone_1.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3|")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\b\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class milestone_1Parser ( Parser ):

    grammarFileName = "milestone_1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'var'", "'and'", "'addr'", 
                     "'as'", "'asm'", "'end'", "'from'", "'bind'", "'block'", 
                     "'break'", "'case'", "'cast'", "'concept'", "'const'", 
                     "'continue'", "'converter'", "'defer'", "'discard'", 
                     "'distinct'", "'div'", "'do'", "'elif'", "'else'", 
                     "'enum'", "'except'", "'export'", "'finally'", "'for'", 
                     "'func'", "'if'", "'import'", "'in'", "'include'", 
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
                     "'='", "'+'", "'*'", "'-'", "'/'", "'~'", "'&'", "'|'", 
                     "'<'", "'>'", "'@'", "'%'", "'!'", "'^'", "'.'", "':'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "COMMENT2", "COMMENT", "EMPTYSTR", "INDENT", 
                      "EMPTYSTR2", "VARIABLE", "ANDD", "ADDR", "ASS", "ASM", 
                      "END", "FROM", "BIND", "BLOCK", "BREAKK", "CASE", 
                      "CAST", "CONCEPT", "CONST", "CONTINUEE", "CONVERTER", 
                      "DEFER", "DISCARD", "DISTINCT", "DIV", "DO", "ELIFF", 
                      "ELSEE", "ENUM", "EXCEPTT", "EEXPORT", "FINALLYY", 
                      "FORR", "FUNC", "IFF", "IIMPORT", "INN", "INCLUDE", 
                      "INTERFACE", "ISS", "ISNOT", "ITERATOR", "LET", "MACRO", 
                      "METHOD", "MIXIN", "MOD", "NIL", "NOTT", "NOTIN", 
                      "OBJECTT", "OF", "ORR", "OUT", "PROC", "PTR", "RAISEE", 
                      "REF", "RETURNN", "SHL", "SHR", "STATIC", "TEMPLATE", 
                      "TRYY", "TUPLEE", "TYPEE", "USING", "WHEN", "WHILEE", 
                      "XOR", "YIELDD", "IDENTIFIER", "LETTER", "DIGIT", 
                      "INT_LIT", "INT8_LIT", "INT16_LIT", "INT32_LIT", "INT64_LIT", 
                      "UINT_LIT", "UINT8_LIT", "UINT16_LIT", "UINT32_LIT", 
                      "UINT64_LIT", "EXP", "FLOAT_LIT", "FLOAT32_SUFFIX", 
                      "FLOAT32_LIT", "FLOAT64_SUFFIX", "FLOAT64_LIT", "HEX_LIT", 
                      "DEC_LIT", "OCT_LIT", "BIN_LIT", "EQUALS_OPERATOR", 
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
    COMMENT2=1
    COMMENT=2
    EMPTYSTR=3
    INDENT=4
    EMPTYSTR2=5
    VARIABLE=6
    ANDD=7
    ADDR=8
    ASS=9
    ASM=10
    END=11
    FROM=12
    BIND=13
    BLOCK=14
    BREAKK=15
    CASE=16
    CAST=17
    CONCEPT=18
    CONST=19
    CONTINUEE=20
    CONVERTER=21
    DEFER=22
    DISCARD=23
    DISTINCT=24
    DIV=25
    DO=26
    ELIFF=27
    ELSEE=28
    ENUM=29
    EXCEPTT=30
    EEXPORT=31
    FINALLYY=32
    FORR=33
    FUNC=34
    IFF=35
    IIMPORT=36
    INN=37
    INCLUDE=38
    INTERFACE=39
    ISS=40
    ISNOT=41
    ITERATOR=42
    LET=43
    MACRO=44
    METHOD=45
    MIXIN=46
    MOD=47
    NIL=48
    NOTT=49
    NOTIN=50
    OBJECTT=51
    OF=52
    ORR=53
    OUT=54
    PROC=55
    PTR=56
    RAISEE=57
    REF=58
    RETURNN=59
    SHL=60
    SHR=61
    STATIC=62
    TEMPLATE=63
    TRYY=64
    TUPLEE=65
    TYPEE=66
    USING=67
    WHEN=68
    WHILEE=69
    XOR=70
    YIELDD=71
    IDENTIFIER=72
    LETTER=73
    DIGIT=74
    INT_LIT=75
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
    FLOAT_LIT=86
    FLOAT32_SUFFIX=87
    FLOAT32_LIT=88
    FLOAT64_SUFFIX=89
    FLOAT64_LIT=90
    HEX_LIT=91
    DEC_LIT=92
    OCT_LIT=93
    BIN_LIT=94
    EQUALS_OPERATOR=95
    ADD_OPERATOR=96
    MUL_OPERATOR=97
    MINUS_OPERATOR=98
    DIV_OPERATOR=99
    BITWISE_NOT_OPERATOR=100
    AND_OPERATOR=101
    OR_OPERATOR=102
    LESS_THAN=103
    GREATER_THAN=104
    AT=105
    MODULUS=106
    NOT_OPERATOR=107
    XOR_OPERATOR=108
    DOT=109
    COLON=110
    OPEN_PAREN=111
    CLOSE_PAREN=112
    OPEN_BRACE=113
    CLOSE_BRACE=114
    OPEN_BRACK=115
    CLOSE_BRACK=116
    COMMA=117
    SEMI_COLON=118
    STR_LIT=119
    CHAR_LIT=120
    TRIPLESTR_LIT=121
    RSTR_LIT=122

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





