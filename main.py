#Still Alive - Portal

import time
import os

clear = lambda: os.system('cls')



def pr(text,right = ""):
	print("---------------")
	print(text,"      ",right)
	print("---------------")


pr("truc")

pr("I AM BIG","droite\nlol")

def print_l(text,liste,image):
	taille2 = 18
	pos_text = 9
	separateur1 = "---------------------------------------------------------------------------"
	separateur2 = "------------------------------------------"
	leng_s1 = len(separateur1) - 4
	leng = leng_s1 - len(text)

	img = 0
	maximg = len(image) 

	clear()
	print(separateur1,separateur2)
	print("|"," "*(len(separateur1)-4),"|","|"," "*(len(separateur2)-4),"|")


	for i in range(len(liste)) :
		if taille2 == 10 :
		 	print(f"|{liste[i]}"," "*(leng_s1 - len(liste[i])),"|","|","                EPITA                 ","|")
		 	taille2 -= 1
		elif taille2 == 9 :
			print(f"|{liste[i]}"," "*(leng_s1 - len(liste[i])),"|","|","           Enrichment Center          ","|")
			taille2 -= 1
		elif taille2 >= 1 :
			print(f"|{liste[i]}"," "*(leng_s1 - len(liste[i])),"|","|"," "*(len(separateur2)-4),"|")
			#print("|"," "*(len(separateur1)-4),"|","|"," "*(len(separateur2)-4),"|")
			taille2 -= 1
		# elif taille2 == 1 :
		# 	print(f"|{liste[i]}"," "*(leng_s1 - len(liste[i])),"|","|"," "*(len(separateur2)-4),"|")
		# 	print("|"," "*(len(separateur1)-4),"|",separateur2)
		# 	taille2 -= 2
		elif taille2 == 0 :
			print(f"|{liste[i]}"," "*(leng_s1 - len(liste[i])),"|",separateur2)
			#print("|"," "*(len(separateur1)-4),"|", image[img])
			taille2 -= 1
			#img += 1 
		else :
			if img < maximg :
				print(f"|{liste[i]}"," "*(leng_s1 - len(liste[i])),"|",image[img])
				#print("|"," "*(len(separateur1)-4),"|",image[img + 1])
				img += 1
			else :
				print(f"|{liste[i]}"," "*(leng_s1 - len(liste[i])),"|")
				print("|"," "*(len(separateur1)-4),"|")

	if taille2 == 10 :
		print(f"|{text}"," "*leng,"|","|",           "                EPITA                 ","|")
		taille2 -= 1
	elif taille2 == 9 :
		print(f"|{text}"," "*leng,"|","|",           "           Enrichment Center          ","|")
		taille2 -= 1
	elif taille2 > 0 :
		print(f"|{text}"," "*leng,"|","|"," "*(len(separateur2)-4),"|")
		taille2 -= 1
	elif taille2 == 0 :
		print(f"|{text}"," "*leng,"|",separateur2)
		taille2 -= 1
	else :
		if img < maximg :
			print(f"|{text}"," "*leng,"|",image[img])
			img +=1
		else :
			print(f"|{text}"," "*leng,"|")

	k = 38 - len(liste)

	while (k > 0):
		if taille2 == 10 :
			print("|"," "*(len(separateur1)-4),"|","|","                EPITA                 ","|")
			taille2 -= 1
			k -= 1
		elif taille2 == 9 :
			print("|"," "*(len(separateur1)-4),"|","|","           Enrichment Center          ","|")
			taille2 -= 1
			k -= 1 
		elif taille2 > 0 :
			print("|"," "*(len(separateur1)-4),"|","|"," "*(len(separateur2)-4),"|")
			taille2 -= 1
			k -= 1
		elif taille2 == 0 : 
			print("|"," "*(len(separateur1)-4),"|",separateur2)
			taille2 -= 1
			k -= 1
		else :
			if img < maximg :
				print("|"," "*(len(separateur1)-4),"|",image[img])
				img += 1
			else :
				print("|"," "*(len(separateur1)-4),"|")
			k -= 1


	print(separateur1)

def pr_char(text,liste,image):
	tot = ""
	for i in text :
		tot += i
		print_l(tot,liste,image)
		#time.sleep(0.01)


text = [
"Forms FORM-29827281-12:",
"Test Assessment Report",
" ",
"This was a triumph.",
"I'm making a note here:",
"HUGE SUCCESS.",
"It's hard to overstate",
"My satisfaction.",
"Aperture Science.",
"We do what we must",
"Because we can.",
"For the good of all of us.",
"Except the ones who are dead.",
" ",
"But there's no sense crying",
"Over every mistake.",
"You just keep on trying",
"Till you run out of cake.",
"And the Science gets done.",
"And you make a neat gun.",
"For the people who are",
"Still alive.",
-1,
"Forms FORM-55551-5:",
"Personnel File Addendum:",
" ",
"Dear <<Subject Name Here>>,",
" ",
"I'm not even angry.",
"I'm being so sincere right now.",
"Even though you broke my heart.",
"And killed me.",
"And tore me to pieces.",
"And threw every piece into a fire.",
"As they burned it hurt because",
"I was so happy for you!",
"Now these points of data",
"Make a beautiful line.",
"And we're out of beta.",
"We're releasing on time.",
"So I'm glad. I got burned.",
"Think of all the things we learned",
"For the people who are",
"Still alive.",
-1,
"Forms FORM-55551-6:",
"Personnel File Addendum Addendum:",
" ",
"One last thing:",
" ",
"Go ahead and leave me.",
"I think I prefer to stay inside.",
"Maybe you'll find someone else",
"To help you.",
"Maybe Black Mesa...",
"THAT WAS A JOKE, HA HA, FAT CHANCE.",
"Anyway this cake is great",
"It's so delicious and moist",
"Look at me still talking when there's science to do",
"When I look out there",
"It makes me GLaD I'm not you",
"I've experiments to run",
"There is research to be done",
"On the people who are",
"Still alive.",
-1,
"Ps: And believe me I am",
"still alive",
"PPS: I'm doing science and I'm",
"still alive",
"PPPS: I feel FANTASTIC and I'm", 
"still alive",
" ",
"FINAL THOUGHT:",
" ",
"While you're dying I'll be", 
"still alive",
" ",
"FINAL THOUGHT PS:",
" ",
"And when you're dead I will be", 
"still alive",
" ",
" ",
"Still alive",
" ",
"Still alive."]



aperture = ["              .,-:;//;:=,               ",
			"          . :H@@@MM@M#H/.,+%;,          ",
			"       ,/X+ +M@@M@MM%=,-%HMMM@X/,       ",
			"     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-     ",
			"    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.   ",
			"  ,%MM@@MH ,@%=            .---=-=:=,.  ",
			"  =@#@@@MX .,              -%HX$$%%%+;  ",
			" =-./@M@M$                  .;@MMMM@MM: ",
			" X@/ -$MM/                    .+MM@@@M$ ",
			",@M@H: :@:                    . =X#@@@@-",
			",@@@MMX, .                    /H- ;@M@M=",
			".H@@@@M@+,                    %MM+..%#$.",
			" /MMMM@MMH/.                  XM@MH; =; ",
			"  /%+%$XHH@$=              , .H@@@@MX,  ",
			"   .=--------.           -%H.,@@@@@MX,  ",
			"  .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.   ",
			"     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=     ",
			"      =%@M@M#@$-.=$@MM@@@M; %M%=       ",
			"         ,:+$+-,/H#MMMMMMM@= =,         ",
			"               =++%%%%+/:-.             "]


cake = ["            ,:/+/-                      ",
		"            /M/              .,-=;//;-  ",
		"       .:/= ;MH/,    ,=/+%$XH@MM#@:     ",
		"      -$##@+$###@H@MMM#######H:.    -/H#",
		" .,H@H@ X######@ -H#####@+-     -+H###@X",
		"  .,@##H;      +XM##M/,     =%@###@X;-  ",
		"X%-  :M##########$.    .:%M###@%:       ",
		"M##H,   +H@@@$/-.  ,;$M###@%,          -",
		"M####M=,,---,.-%%H####M$:          ,+@##",
		"@##################@/.         :%H##@$- ",
		"M###############H,         ;HM##M$=     ",
		"#################.    .=$M##M$=         ",
		"################H..;XM##M$=          .:+",
		"M###################@%=           =+@MH%",
		"@################M/.          =+H#X%=   ",
		"=+M##############M,       -/X#X+;.      ",
		"  .;XM##########H=    ,/X#H+:,          ",
		"     .=+HM######M+/+HM@+=.              ",
		"         ,:/%XM####H/.                  ",
		"              ,.:=-.                    "]

rad = [
"             =+$HM####@H%;,",
"          /H###############M$,",
"          ,@################+",
"           .H##############+",
"             X############/",
"              $##########/",
"               %########/",
"                /X/;;+X/",
"  ",
"                 -XHHX-",
"                ,######,",
"#############X  .M####M.  X#############",
"##############-   -//-   -##############",
"X##############%,      ,+##############X",
"-##############X        X##############-",
" %############%          %############%",
"  %##########;            ;##########%",
"   ;#######M=              =M#######;",
"    .+M###@,                ,@###M+.",
"       :XH.                  .HX:]"
]

boom = [
"            .+",
"             /M;",
"              H#@:              ;,",
"              -###H-          -@/",
"               %####$.  -;  .%#X",
"                M#####+;#H :M#M.",
"..          .+/;%#########X###-",
" -/%H%+;-,    +##############/",
"    .:$M###MH$%+############X  ,--=;-",
"        -/H#####################H+=.",
"           .+#################X.",
"         =%M####################H;.",
"            /@###############+;;/%%;,",
"         -%###################$.",
"       ;H######################M=",
"    ,%#####MH$%;+#####M###-/@####%",
"  :$H%+;=-      -####X.,H#   -+M##@-",
" .              ,###;    ;      =$##+",
"                .#H,               :XH,",
"                +                   .;-"
]

radio = [
"                   ;=",
"                   /=",
"                   ;=",
"                   /=",
"                   ;=",
"                   /=",
"                   ;=",
"                   /=",
"            ,--==-:$;",
"        ,/$@#######@X+-",
"     ./@###############X=",
"    /M#####X+/;;;;+H#####$.",
"   %####M/;+H@XX@@%;;@####@,",
"  +####H=+##$,--,=M#X-%####@.",
" -####X,X@HHXH##MXHXXH-+####$",
" X###@.X/$M$:####$=@X/X,X####-",
".####:+$:##@:####$:##H/X=####%",
"-%%$%,+==%$+-$+:$;-$$%-+,/$%%+",
"-/+%%X$XX$$$$$$$%$$$%$X$X$%+/-"
]

atom = [
"                 =/;;/-",
"                +:    //",
"               /;      /;",
"              -X        H.",
".//;;;:;;-,   X=        :+   .-;:=;:;%;.",
"M-       ,=;;;#:,      ,:#;;:=,       ,@",
":%           :%.=/++++/=.$=           %=",
" ,%;         %/:+/;,,/++:+/         ;+.",
"   ,+/.    ,;@+,        ,%H;,    ,/+,",
"      ;+;;/= @.  .H##X   -X :///+;",
"      ;+=;;;.@,  .XM@$.  =X.//;=%/.",
"   ,;:      :@%=        =$H:     .+%-",
" ,%=         %;-///==///-//         =%,",
";+           :%-;;;:;;;;-X-           +:",
"@-      .-;;;;M-        =M/;;;-.      -X",
" :;;::;;-.    %-        :+    ,-;;-;:==",
"              ,X        H.",
"              ;/      %=",
"                //    +;",
"                 ,////,"
]

mesa = [
"           .-;+$XHHHHHHX$+;-.",
"        ,;X@@X%/;=----=:/%X@@X/,",
"      =$@@%=.              .=+H@X:",
"    -XMX:                      =XMX=",
"   /@@:                          =H@+",
"  %@X,                            .$@$",
" +@X.                               $@%",
"-@@,                                .@@=",
"%@%                                  +@$",
"H@:                                  :@H",
"H@:         :HHHHHHHHHHHHHHHHHHX,    =@H",
"%@%         ;@M@@@@@@@@@@@@@@@@@H-   +@$",
"=@@,        :@@@@@@@@@@@@@@@@@@@@@= .@@:",
" +@X        :@@@@@@@@@@@@@@@M@@@@@@:%@%",
"  $@$,      ;@@@@@@@@@@@@@@@@@M@@@@@@$.",
"   +@@HHHHHHH@@@@@@@@@@@@@@@@@@@@@@@+",
"    =X@@@@@@@@@@@@@@@@@@@@@@@@@@@@X=",
"      :$@@@@@@@@@@@@@@@@@@@M@@@@$:",
"        ,;$@@@@@@@@@@@@@@@@@@X/-",
"           .-;+$XXHHHHHX$+;-."
]

heart = [
"                          .,---.",
"                        ,/XM#MMMX;,",
"                      -%##########M%,",
"                     -@######%  $###@=",
"      .,--,         -H#######$   $###M:",
"   ,;$M###MMX;     .;##########$;HM###X=",
" ,/@##########H=      ;################+",
"-+#############M/,      %##############+",
"%M###############=      /##############:",
"H################      .M#############;.",
"@###############M      ,@###########M:.",
"X################,      -$=X#######@:",
"/@##################%-     +######$-",
".;##################X     .X#####+,",
" .;H################/     -X####+.",
"   ,;X##############,       .MM/",
"      ,:+$H@M#######M#$-    .$$=",
"           .,-=;+$@###X:    ;/=.",
"                  .,/X$;   .::,",
"                      .,    .."
]

check = [
"                                     :X-",
"                                  :X###",
"                                ;@####@",
"                              ;M######X",
"                            -@########$",
"                          .$##########@",
"                         =M############-",
"                        +##############$",
"                      .H############$=.",
"         ,/:         ,M##########M;.",
"      -+@###;       =##########M;",
"   =%M#######;     :#########M/",
"-$M###########;   :#########/",
" ,;X###########; =########$.",
"     ;H#########+#######M=",
"       ,+##############+",
"          /M#########@-",
"            ;M######%",
"              +####:",
"               ,$M-"
]

cube = [
"+@##########M/             :@#########@/",
"##############$;H#######@;+#############",
"###############M########################",
"##############X,-/++/+%+/,%#############",
"############M$:           -X############",
"##########H;.      ,--.     =X##########",
":X######M;     -$H@M##MH%:    :H#######@",
"  =%#M+=,   ,+@#######M###H:    -=/M#%",
"  %M##@+   .X##$, ./+- ./###;    +M##%",
"  %####M.  /###=         @##M.   X###%",
"  %####M.  ;M##H:.     =$###X.   $###%",
"  %####@.   /####M$-./@#####:    %###%",
"  %H#M/,     /H###########@:     ./M#%",
" ;$H##@@H:    .;$HM#MMMH$;,   ./H@M##M$=",
"X#########%.      ..,,.     .;@#########",
"###########H+:.           ./@###########",
"##############/ ./%%%%+/.-M#############",
"##############H$@#######@@##############",
"##############X%########M$M#############",
"+M##########H:            .$##########X="
]

flame = [
"                     -$-",
"                    .H##H,",
"                   +######+",
"                .+#########H.",
"              -$############@.",
"            =H###############@  -X:",
"          .$##################:  @#@-",
"     ,;  .M###################;  H###;",
"   ;@#:  @###################@  ,#####:",
" -M###.  M#################@.  ;######H",
" M####-  +###############$   =@#######X",
" H####$   -M###########+   :#########M,",
"  /####X-   =########%   :M########@/.",
"    ,;%H@X;   .$###X   :##MM@%+;:-",
"                 ..",
"  -/;:-,.              ,,-==+M########H",
" -##################@HX%%+%%$%%%+:,,",
"    .-/H%%%+%%$H@###############M@+=:/+:",
"/XHX%:#####MH%=    ,---:;;;;/%%XHM,:###$"
]

thing = [
"       #+ @      # #              M#@",
" .    .X  X.%##@;# #   +@#######X. @#%",
"   ,==.   ,######M+  -#####%M####M-    #",
"  :H##M%:=##+ .M##M,;#####/+#######% ,M#",
" .M########=  =@#@.=#####M=M#######=  X#",
" :@@MMM##M.  -##M.,#######M#######. =  M",
"             @##..###:.    .H####. @@ X,",
"   ############: ###,/####;  /##= @#. M",
"           ,M## ;##,@#M;/M#M  @# X#% X#",
".%=   ######M## ##.M#:   ./#M ,M #M ,#$",
"##/         $## #+;#: #### ;#/ M M- @# :",
"#+ #M@MM###M-;M #:$#-##$H# .#X @ + $#. #",
"      ######/.: #%=# M#:MM./#.-#  @#: H#",
"+,.=   @###: /@ %#,@  ##@X #,-#@.##% .@#",
"#####+;/##/ @##  @#,+       /#M    . X,",
"   ;###M#@ M###H .#M-     ,##M  ;@@; ###",
"   .M#M##H ;####X ,@#######M/ -M###$  -H",
"    .M###%  X####H  .@@MM@;  ;@#M@",
"      H#M    /@####/      ,++.  / ==-,",
"               ,=/:, .+X@MMH@#H  #####$="
]

idea = [
"         ,=;%$%%$X%%%%;/%%%%;=,",
"     ,/$$+:-                -:+$$/,",
"   :X$=                          =$X:",
" ;M%.                              .%M;",
"+#/                                  /#+",
"##                                    M#",
"H#,                     =;+/;,       ,#X",
".HM-       :@X+%H:   .%M%- .M#.     -M@.",
"  /#%.     @#-  ,H@--MH, .;@$-    .%#+",
"   .$M;    .+@X;, MM#@:/$X;.     ;M$,",
"     =@H,     ,:+%H#M%;-       ,H@=",
"      .$#;        -#H         =#$",
"        %#;        #M        ;#%",
"         H#-       ##       -#H",
"         ;#+       ##       +#;",
"          ;H+;;;;;;HH;;;;;;+H/",
"           =H#@HHHHHHHHHH@#H=",
"           =@#H%%%%%%%$HH@#@=",
"           =@#X%%%%%%%$M###@=",
"               =+%XHHX%+="
]

grab = [
"      X MM X",
"      X MM X",
"      X MM X",
"      X MM X",
"      + HX +",
"    ,=$$XX%/-",
"  =X#########@%-",
" ;##############=",
"-###############M,",
";##@@@######M@###=",
".+:;+:=H##$=:/:;H.",
"- +###- ## :###,,;",
"+@:/%;-H##H==/::H;",
" /#@/-=+$$%::+H#$",
" $#%-,      ,.:##-",
"-@/            =X%.",
"%H=             -$;",
" =HH,         .%M;",
"  /MM/       :@M/.",
"   .:XX,   -$H:."
]

weat = [
"      .-+$H###MM@MMMMM##@$+-,. ....",
"-@$+%$+%HX+--..  .  . .,:X$/+/++$#:",
"-#MXH$=                      $HXH#:",
" .--,:#+   ,+$HMX =@@X%, . .X#:,,,",
"     =#@$H :####H =####;,M%$#X",
"     X###$ $####X =####H %###X",
"    ;###X /###@$: ,+HM##H.+###;",
"   :###;,X##%=;%H@H$;-;M#@-;###/",
"  ,M##;.@##;-H#######M=.M##-:###-",
"  ;##M ;##X @###H-=@###.;##X H##;",
"  ;##M./##X.@###H:/M###-=##X X##;",
"  -###;,M##:,@########+-H##; @##-",
"   %##M==@##%==%HMH%::/M##+.X##+",
"    %###/./###X+: -+$M##M=,X##+",
"     X###X X####H +#####% @##H",
"     :###H %####H +#####; X##;",
"     /#$.  -HM##H /###@+.  +#$. .",
"/HX%$X:      .,-, .-,.      =XX$H@-",
"/#H+/+%+/+;=.          .=/%;;/;;+#+",
" ..  .,-:XM#MM@@@@@@H@@M#@+=,.   ,,"
]

def pr_f(text):
	liste = []
	image = aperture
	for k in text :
		if k != -1 :
			if "crying" in k or "people" in k or "look out" in k or "when you're" in k :
				image = aperture
			elif "dead" in k or "Science to do" in k :
				image = rad
			elif "Science gets done" in k or "learned" in k or "experiments" in k :
				image = atom
			elif "heart" in k :
				image = heart
			elif "tore" in k or "burned" in k or "experiments" in k :
				image = boom
			elif "fire" in k :
				image = flame
			elif "happy" in k :
				image = check
			elif "Black Mesa" in k :
				image = mesa
			elif "cake" in k :
				image = cake
			elif "Look" in k :
				image = thing
			pr_char(k,liste,image)
			liste.append(k)
		else :
			time.sleep(2)
			clear()
			liste = []


pr_f(text)
