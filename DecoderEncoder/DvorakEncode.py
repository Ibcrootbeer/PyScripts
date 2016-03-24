#!/usr/bin/env python

userinput = raw_input()

output = ''

for i in userinput:
	if i == '\'':
		output += 'q'
	elif i == ',':
		output += 'w'
	elif i == '.':
		output += 'e'
	elif i == 'p':
		output += 'r'
	elif i == 'y':
		output += 't'
	elif i == 'f':
		output += 'y'
	elif i == 'g':
		output += 'u'
	elif i == 'c':
		output += 'i'
	elif i == 'r':
		output += 'o'
	elif i == 'l':
		output += 'p'
	elif i == '/':
		output += '['
	elif i == '=':
		output += ']'
	elif i == '\\':
		output += '\\'
	elif i == 'a':
		output += 'a'
	elif i == 'o':
		output += 's'
	elif i == 'e':
		output += 'd'
	elif i == 'u':
		output += 'f'
	elif i == 'i':
		output += 'g'
	elif i == 'd':
		output += 'h'
	elif i == 'h':
		output += 'j'
	elif i == 't':
		output += 'k'
	elif i == 'n':
		output += 'l'
	elif i == 's':
		output += ';'
	elif i == '-':
		output += '\''
	elif i == ';':
		output += 'z'
	elif i == 'q':
		output += 'x'
	elif i == 'j':
		output += 'c'
	elif i == 'k':
		output += 'v'
	elif i == 'x':
		output += 'b'
	elif i == 'b':
		output += 'n'
	elif i == 'm':
		output += 'm'
	elif i == 'w':
		output += ','
	elif i == 'v':
		output += '.'
	elif i == 'z':
		output += '/'
	elif i == '1':
		output += '1'
	elif i == '2':
		output += '2'
	elif i == '3':
		output += '3'
	elif i == '4':
		output += '4'
	elif i == '5':
		output += '5'
	elif i == '6':
		output += '6'
	elif i == '7':
		output += '7'
	elif i == '8':
		output += '8'
	elif i == '9':
		output += '9'
	elif i == '0':
		output += '0'
	elif i == '[':
		output += '-'
	elif i == ']':
		output += '='
#SHIFT
	elif i == '"':
		output += 'Q'
	elif i == '<':
		output += 'W'
	elif i == '>':
		output += 'E'
	elif i == 'P':
		output += 'R'
	elif i == 'Y':
		output += 'T'
	elif i == 'F':
		output += 'Y'
	elif i == 'G':
		output += 'U'
	elif i == 'C':
		output += 'I'
	elif i == 'R':
		output += 'O'
	elif i == 'L':
		output += 'P'
	elif i == '?':
		output += '{'
	elif i == '+':
		output += '}'
	elif i == '|':
		output += '|'
	elif i == 'A':
		output += 'A'
	elif i == 'O':
		output += 'S'
	elif i == 'E':
		output += 'D'
	elif i == 'U':
		output += 'F'
	elif i == 'I':
		output += 'G'
	elif i == 'D':
		output += 'H'
	elif i == 'H':
		output += 'J'
	elif i == 'T':
		output += 'K'
	elif i == 'N':
		output += 'L'
	elif i == 'S':
		output += ':'
	elif i == '_':
		output += '"'
	elif i == ':':
		output += 'Z'
	elif i == 'Q':
		output += 'X'
	elif i == 'J':
		output += 'C'
	elif i == 'K':
		output += 'V'
	elif i == 'X':
		output += 'B'
	elif i == 'B':
		output += 'N'
	elif i == 'M':
		output += 'M'
	elif i == 'W':
		output += '<'
	elif i == 'V':
		output += '>'
	elif i == 'Z':
		output += '?'
	elif i == '!':
		output += '!'
	elif i == '@':
		output += '@'
	elif i == '#':
		output += '#'
	elif i == '$':
		output += '$'
	elif i == '%':
		output += '%'
	elif i == '^':
		output += '^'
	elif i == '&':
		output += '&'
	elif i == '*':
		output += '*'
	elif i == '(':
		output += '('
	elif i == ')':
		output += ')'
	elif i == '{':
		output += '_'
	elif i == '}':
		output += '+'

print output
