// Generated from /home/angelo/Facultad/Tercero/DHS/test/src/main/python/compiladores.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class compiladoresLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NUMERO=1, PALABRA=2, PUCO=3, ASIG=4, PA=5, PC=6, CA=7, CC=8, LA=9, LC=10, 
		SUM=11, RES=12, MUL=13, DIV=14, IGUAL=15, MAYOR=16, MENOR=17, DISTINTO=18, 
		IF=19, ELSE=20, WHILE=21, OTRO=22, ID=23;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LETRA", "DIGITO", "NUMERO", "PALABRA", "PUCO", "ASIG", "PA", "PC", "CA", 
			"CC", "LA", "LC", "SUM", "RES", "MUL", "DIV", "IGUAL", "MAYOR", "MENOR", 
			"DISTINTO", "IF", "ELSE", "WHILE", "OTRO", "ID"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "';'", "'='", "'('", "')'", "'['", "']'", "'{'", "'}'", 
			"'+'", "'-'", "'*'", "'/'", "'=='", "'>='", "'<='", "'!='", "'if'", "'else'", 
			"'while'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "NUMERO", "PALABRA", "PUCO", "ASIG", "PA", "PC", "CA", "CC", "LA", 
			"LC", "SUM", "RES", "MUL", "DIV", "IGUAL", "MAYOR", "MENOR", "DISTINTO", 
			"IF", "ELSE", "WHILE", "OTRO", "ID"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public compiladoresLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "compiladores.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31\u0082\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\3\2\3\2\3\3\3\3\3\4\6\4;\n\4\r\4\16\4<\3\5\6\5@\n\5\r"+
		"\5\16\5A\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r"+
		"\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23"+
		"\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27"+
		"\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\5\32z\n\32\3\32"+
		"\3\32\3\32\6\32\177\n\32\r\32\16\32\u0080\2\2\33\3\2\5\2\7\3\t\4\13\5"+
		"\r\6\17\7\21\b\23\t\25\n\27\13\31\f\33\r\35\16\37\17!\20#\21%\22\'\23"+
		")\24+\25-\26/\27\61\30\63\31\3\2\4\4\2C\\c|\3\2\62;\2\u0085\2\7\3\2\2"+
		"\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23"+
		"\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2"+
		"\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2"+
		"\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\3\65\3"+
		"\2\2\2\5\67\3\2\2\2\7:\3\2\2\2\t?\3\2\2\2\13C\3\2\2\2\rE\3\2\2\2\17G\3"+
		"\2\2\2\21I\3\2\2\2\23K\3\2\2\2\25M\3\2\2\2\27O\3\2\2\2\31Q\3\2\2\2\33"+
		"S\3\2\2\2\35U\3\2\2\2\37W\3\2\2\2!Y\3\2\2\2#[\3\2\2\2%^\3\2\2\2\'a\3\2"+
		"\2\2)d\3\2\2\2+g\3\2\2\2-j\3\2\2\2/o\3\2\2\2\61u\3\2\2\2\63y\3\2\2\2\65"+
		"\66\t\2\2\2\66\4\3\2\2\2\678\t\3\2\28\6\3\2\2\29;\5\5\3\2:9\3\2\2\2;<"+
		"\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\b\3\2\2\2>@\5\3\2\2?>\3\2\2\2@A\3\2\2\2"+
		"A?\3\2\2\2AB\3\2\2\2B\n\3\2\2\2CD\7=\2\2D\f\3\2\2\2EF\7?\2\2F\16\3\2\2"+
		"\2GH\7*\2\2H\20\3\2\2\2IJ\7+\2\2J\22\3\2\2\2KL\7]\2\2L\24\3\2\2\2MN\7"+
		"_\2\2N\26\3\2\2\2OP\7}\2\2P\30\3\2\2\2QR\7\177\2\2R\32\3\2\2\2ST\7-\2"+
		"\2T\34\3\2\2\2UV\7/\2\2V\36\3\2\2\2WX\7,\2\2X \3\2\2\2YZ\7\61\2\2Z\"\3"+
		"\2\2\2[\\\7?\2\2\\]\7?\2\2]$\3\2\2\2^_\7@\2\2_`\7?\2\2`&\3\2\2\2ab\7>"+
		"\2\2bc\7?\2\2c(\3\2\2\2de\7#\2\2ef\7?\2\2f*\3\2\2\2gh\7k\2\2hi\7h\2\2"+
		"i,\3\2\2\2jk\7g\2\2kl\7n\2\2lm\7u\2\2mn\7g\2\2n.\3\2\2\2op\7y\2\2pq\7"+
		"j\2\2qr\7k\2\2rs\7n\2\2st\7g\2\2t\60\3\2\2\2uv\13\2\2\2v\62\3\2\2\2wz"+
		"\5\3\2\2xz\7a\2\2yw\3\2\2\2yx\3\2\2\2z~\3\2\2\2{\177\5\3\2\2|\177\5\5"+
		"\3\2}\177\7a\2\2~{\3\2\2\2~|\3\2\2\2~}\3\2\2\2\177\u0080\3\2\2\2\u0080"+
		"~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\64\3\2\2\2\b\2<Ay~\u0080\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}