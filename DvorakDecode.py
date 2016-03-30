#!/usr/bin/env python

userinput = raw_input()

output = ''

for i in userinput:
	if i == 'q':
		output += '\''
	elif i == 'w':
		output += ','
	elif i == 'e':
		output += '.'
	elif i == 'r':
		output += 'p'
	elif i == 't':
		output += 'y'
	elif i == 'y':
		output += 'f'
	elif i == 'u':
		output += 'g'
	elif i == 'i':
		output += 'c'
	elif i == 'o':
		output += 'r'
	elif i == 'p':
		output += 'l'
	elif i == '[':
		output += '/'
	elif i == ']':
		output += '='
	elif i == '\\':
		output += '\\'
	elif i == 'a':
		output += 'a'
	elif i == 's':
		output += 'o'
	elif i == 'd':
		output += 'e'
	elif i == 'f':
		output += 'u'
	elif i == 'g':
		output += 'i'
	elif i == 'h':
		output += 'd'
	elif i == 'j':
		output += 'h'
	elif i == 'k':
		output += 't'
	elif i == 'l':
		output += 'n'
	elif i == ';':
		output += 's'
	elif i == '\'':
		output += '-'
	elif i == 'z':
		output += ';'
	elif i == 'x':
		output += 'q'
	elif i == 'c':
		output += 'j'
	elif i == 'v':
		output += 'k'
	elif i == 'b':
		output += 'x'
	elif i == 'n':
		output += 'b'
	elif i == 'm':
		output += 'm'
	elif i == ',':
		output += 'w'
	elif i == '.':
		output += 'v'
	elif i == '/':
		output += 'z'
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
	elif i == '-':
		output += '['
	elif i == '=':
		output += ']'
#SHIFT
	elif i == 'Q':
		output += '"'
	elif i == 'W':
		output += '<'
	elif i == 'E':
		output += '>'
	elif i == 'R':
		output += 'P'
	elif i == 'T':
		output += 'Y'
	elif i == 'Y':
		output += 'F'
	elif i == 'U':
		output += 'G'
	elif i == 'I':
		output += 'C'
	elif i == 'O':
		output += 'R'
	elif i == 'P':
		output += 'L'
	elif i == '{':
		output += '?'
	elif i == '}':
		output += '+'
	elif i == '|':
		output += '|'
	elif i == 'A':
		output += 'A'
	elif i == 'S':
		output += 'O'
	elif i == 'D':
		output += 'E'
	elif i == 'F':
		output += 'U'
	elif i == 'G':
		output += 'I'
	elif i == 'H':
		output += 'D'
	elif i == 'J':
		output += 'H'
	elif i == 'K':
		output += 'T'
	elif i == 'L':
		output += 'N'
	elif i == ':':
		output += 'S'
	elif i == '"':
		output += '_'
	elif i == 'Z':
		output += ':'
	elif i == 'X':
		output += 'Q'
	elif i == 'C':
		output += 'J'
	elif i == 'V':
		output += 'K'
	elif i == 'B':
		output += 'X'
	elif i == 'N':
		output += 'B'
	elif i == 'M':
		output += 'M'
	elif i == '<':
		output += 'W'
	elif i == '>':
		output += 'V'
	elif i == '?':
		output += 'Z'
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
	elif i == '_':
		output += '{'
	elif i == '+':
		output += '}'

print output
