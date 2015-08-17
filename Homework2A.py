#!/usr/bin/env python

import sys

nota1 = int(sys.argv[1])
nota2 = int(sys.argv[2])
nota3 = int(sys.argv[3])
nota4 = int(sys.argv[4])
print "The average score is:" , (nota1 + nota2 + nota3 + nota4)/4

avg = (nota1 + nota2 + nota3 + nota4)/4

if avg >= 90:
	print "Letter Grade: A"
elif avg >= 80:
	print "Letter Grade: B"
elif avg >= 70:
	print "Letter Grade: C"
elif avg >= 60:
	print "Letter Grade: D"
else:
	print "Letter Grade: F"

