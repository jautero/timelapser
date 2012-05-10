duration=False
delay=4
imgdir="/tmp/netf"
waitkey=False
playsound=False
brightnessfilter=False

# Print config variable given as parameter for reading config file in shell scripts
if __name__ == '__main__':
	import sys
	print globals()[sys.argv[1]]

