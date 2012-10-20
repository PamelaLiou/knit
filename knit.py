knit_main = ('''    /\   /\   \n___|__\ /__|__\n    \_____/   ''')
    
    
knit_top = ('''     _____    \n    /     \   \n    |     |   \n    \_____/   ''')

knit_bottom = ('''    /\   /\   \n___|__\ /__|__\n    \     /   \n_____\   /____''')
				
print knit_main
print "Let's knit in ASC-II!"

x = raw_input("How many stitches do you want to cast on your needle?")
y = raw_input("How many rows would you like to knit?")

print "So, your swatch will be %r stitches wide and %r rows tall." % ( x, y )

(x , y) = (int(x), int(y))

knit_toparray = knit_top.splitlines()
knit_mainarray = knit_main.splitlines()
knit_bottomarray = knit_bottom.splitlines()


def knit_body():
	for main_z in range (0,3):
		print knit_mainarray[main_z] * x
		main_z = main_z + 1;
		
def knit_rows():
	for rows in range (0, y - 2):
		knit_body()

for top_z in range (0, 3):
	print knit_toparray[top_z] * x
	top_z = top_z + 1;

knit_rows()

for bottom_z in range (0, 4):
	print knit_bottomarray[bottom_z] * x
	bottom_z = bottom_z + 1;
