# -*- coding: utf-8 -*- 
import random
counter = 0
score = 0

# creation du dict des verbes au preterit
preterit = {
"abide":"abode",
"arise":"arose",
"awake":"awoke",
"be":"was: were",
"bear":"bore",
"beat":"beat",
"become":"became",
"beget":"begat / begot",
"begin":"began",
"bend":"bent",
"bereave":"bereft / bereaved",
"bet":"bet",
"bid":"bid / bade",
"bleed":"bled",
"blow":"blew",
"break":"broke",
"breed":"bred",
"bring":"brought",
"broadcast":"broadcast",
"build":"built",
"burn":"burnt / burned",
"burst":"burst",
"buy":"bought",
"can":"could",
"cast":"cast",
"catch":"caught",
"chide":"chid",
"choose":"chose",
"cling":"clung",
"clothe":"clad / clothed",
"come":"came",
"cost":"cost",
"creep":"crept",
"cut":"cut",
"deal":"dealt",
"dig":"dug",
"dive":"dived",
"do":"did",
"draw":"drew",
"dream":"dreamt / dreamed",
"drink":"drank",
"drive":"drove",
"dwell":"dwelt",
"eat":"ate",
"fall":"fell",
"feed":"fed",
"feel":"felt",
"fight":"fought",
"find":"found",
"flee":"fled",
"fling":"flung",
"fly":"flew",
"forbid":"forbade",
"forecast":"forecast",
"foresee":"foresaw",
"forget":"forgot",
"forgive":"forgave",
"forsake":"forsook",
"freeze":"froze",
"get":"got",
"give":"gave",
"go":"went",
"grind":"ground",
"grow":"grew",
"hang":"hung",
"have":"had",
"hear":"heard",
"hide":"hid",
"hit":"hit",
"hold":"held",
"hurt":"hurt",
"keep":"kept",
"kneel":"knelt / knelled",
"know":"knew",
"lay":"laid",
"lead":"led",
"lean":"leant / leaned",
"leap":"leapt / leaped",
"learn":"learnt",
"leave":"left",
"lend":"lent",
"let":"let",
"lie":"lay",
"light":"lit / lighted",
"lose":"lost",
"make":"made",
"mean":"meant",
"meet":"met",
"mow":"mowed",
"offset":"offset",
"overcome":"overcame",
"partake":"partook",
"pay":"paid",
"plead":"pled / pleaded",
"preset":"preset",
"prove":"proved",
"put":"put",
"quit":"quit",
"read":"read",
"relay":"relaid",
"rend":"rent",
"rid":"rid",
"ride":"rode",
"ring":"rang",
"rise":"rose",
"run":"ran",
"saw":"saw / sawed",
"say":"said",
"see":"saw",
"seek":"sought",
"sell":"sold",
"send":"sent",
"set":"set",
"shake":"shook",
"shed":"shed",
"shine":"shone",
"shoe":"shod",
"shoot":"shot",
"show":"showed",
"shut":"shut",
"sing":"sang",
"sink":"sank / sunk",
"sit":"sat",
"slay":"slew",
"sleep":"slept",
"slide":"slid",
"slink":"slunk / slinked",
"slit":"slit",
"smell":"smelt",
"sow":"sowed",
"speak":"spoke",
"speed":"sped",
"spell":"spelt",
"spend":"spent",
"spill":"spilt / spilled",
"spin":"spun",
"spit":"spat / spit",
"split":"split",
"spoil":"spoilt",
"spread":"spread",
"spring":"sprang",
"stand":"stood",
"steal":"stole",
"stick":"stuck",
"sting":"stung",
"stink":"stank",
"strew":"strewed",
"strike":"struck",
"strive":"strove",
"swear":"swore",
"sweat":"sweat / sweated",
"sweep":"swept",
"swell":"swelled",
"swim":"swam",
"swing":"swung",
"take":"took",
"teach":"taught",
"tear":"tore",
"tell":"told",
"think":"thought",
"thrive":"throve / thrived",
"throw":"threw",
"thrust":"thrust",
"tread":"trod",
"typeset":"typeset",
"undergo":"underwent",
"understand":"understood",
"wake":"woke",
"wear":"wore",
"weep":"wept",
"wet":"wet / wetted",
"win":"won",
"wind":"wound",
"withdraw":"withdrew",
"wring":"wrung",
"write":"wrote",
}

print preterit

for verb, conjug in preterit.items():
    print "Le verbe %s se conjugue au prétérit par %s" % (verb, conjug)
    
    
while counter < 10:
    verbe = random.choice(preterit.keys())
    print "Vous devenez conjuguer le verbe %s au preterit" % verbe
    devine = raw_input("Quelle est la conujgaison du verbe %s au prétérit? > " % verbe)
    print verbe
    if devine == preterit[verbe]:
        print "Bravo!"
        score = score +1
        
    else:
        print "Non ce n'est pas ça!"
        print "La réponse est %s" % (preterit[verbe])
    
    counter = counter + 1 

if score >= 8:
    print "TB vous avez %d réponses justes" % score
elif score >= 6 and score < 8:
    print "Bien vous avez %d réponses justes" % score
elif score < 6 and score >= 5:
    print "Vous avez la moyenne avec %d réponses justes" % score
else:
    print "Vous n'avez pas la moyenne avec %d réponses justes" % score
    
    
