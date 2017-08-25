import shutil
import glob
from pathlib import Path
import argparse
import jinja2
import os
from jinja2 import Template

parser = argparse.ArgumentParser(description= "latex opties")
group = parser.add_mutually_exclusive_group()
group.add_argument("-t","--taknaam", help= " de taknaam voor het sjabloon")
group.add_argument("-a","--all",action="store_true")
parser.add_argument("--onderwerp", "-o", default= "mastworp", help= " het onderwerp van het sjabloon, default is Mastworp")
parser.add_argument("-s","--source",action="store_true")
parser.add_argument("-j","--jinlogo",action="store_true")

args = parser.parse_args()




latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

def readLogoList():
	return sorted(glob.glob("logos/logo_0*.png"))

takdict = {
	"kapoenen" : "logos/logo_01kapoenen.png",
	"kapoenen1" : "logos/logo_01kapoenen.png",
	"kapoenen2" : "logos/logo_01kapoenen.png",
	"welpen" : "logos/logo_02kawelpen.png",
	"kabouters" : "logos/logo_02kawelpen.png",
	"kawelpen" : "logos/logo_02kawelpen.png",
	"jonggidsen" : "logos/logo_03jonggivers.png",
	"jongverkenners":"logos/logo_03jonggivers.png",
	"jonggivers" : "logos/logo_03jonggivers.png",
	"givers" : "logos/logo_04givers.png",
	"leiding" : "logos/logo_06leiding.png",
	"groeps": "logos/logo_07groepsleiding.png",
	"groepsleiding": "logos/logo_07groepsleiding.png",
	"jin" : "logos/logo_05jin.png"}
colordict = {
"logos/logo_01kapoenen.png": "ffce5d",
"logos/logo_02kawelpen.png": "4fbeb7",
"logos/logo_03jonggivers.png": "f7a961",
"logos/logo_04givers.png": "668bc0",
"logos/logo_05jin.png": "b8627f",
"logos/logo_06leiding.png": "a376a1",
"logos/logo_07groepsleiding.png": "725543"
}
titel = args.onderwerp
titellogo = "logos/logo_mastworp.png"
my_file = Path("logos/logo_%s.png" % (titel))
if my_file.is_file():
	titellogo = "logos/logo_%s.png" % (titel)
if args.all:
	for key in takdict:
		com = "python gensjabloon.py -t %s -o %s %s %s" %(key,titel,args.source*"-s", args.jinlogo*"-j")
		os.system(com)
	exit()


template = latex_jinja_env.get_template('.sjabloon.tex')
Logolist = readLogoList()
taknaam = args.taknaam.lower()
if not taknaam in takdict.keys() :
	raise ValueError(' taknaam niet herkent: %s , gebruik een van deze: %s' % (taknaam, takdict.keys()))
if not taknaam == 'jin' and not args.jinlogo:
	Logolist.remove("logos/logo_05jin.png")
taklogo = takdict.get(taknaam)

takkleur = colordict.get(taklogo).upper()
fileStr = template.render( logolist = Logolist,
						takkleur = takkleur,
						tak = taknaam.title(),
						logo = taklogo,
						title = titel,
						titellogo = titellogo,
						)

f = open("temp.tex",'w')
f.write(fileStr)
f.close()
output = taknaam.title() + '_' + titel.title()
os.system("xelatex temp.tex")
os.system("xelatex temp.tex")
newpath = 'sjablonen/Sjabloon_%s.pdf'% (output)
shutil.move("temp.pdf" , newpath)
if args.source:
	shutil.move("temp.tex", "tex/Sjabloon_%s.tex"% (output))
os.remove("temp.aux")
os.remove("temp.log")


