# This script is used for generating html pages from markdown
# Dependencies:
#	markdown2 - https://github.com/trentm/python-markdown2

from markdown2 import Markdown
import glob
import os
from config import *

print "Converter of markdown to html for knowledgebase"

converter = Markdown() 
files = glob.glob('sources/*.md')
for f in files:
	print "Converting file", f
	# read markdown input
	markdown = open(f, 'r')
	text = markdown.read()
	markdown.close()

	# convert markdown to html
	result = converter.convert(text)	
	
	# write result to the html ouput file
	outputFile = os.path.basename(f)[:-2] + 'html'
	outputPath = EXPORT_PATH + '/' + outputFile
	html = open(outputPath, 'w')
	html.write(result)
	html.close()
