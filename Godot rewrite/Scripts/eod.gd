extends Node


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var clippy = ""
var old_clippy = ""
var keyed = false
var justeodd = false

var commonWords = [
	"sudo",
	"http",
]


var keylist = []
func key(key):
	key = String(key)
	for i in key:
		keylist.append(int(i))
				


# Called when the node enters the scene tree for the first time.
func _ready():
	$Timer.start()


var encryptDict = {
  1: "A",
  2: "B",
  3: "C",
  4: "D",
  5: "E",
  6: "F",
  7: "G",
  8: "H",
  9: "I",
  10: "J",
  11: "K",
  12: "L",
  13: "M",
  14: "N",
  15: "O",
  16: "P",
  17: "Q",
  18: "R",
  19: "S",
  20: "T",
  21: "U",
  22: "V",
  23: "W",
  24: "X",
  25: "Y",
  26: "Z",
  27: " ",
  28: "`",
  29: "~",
  30: "!",
  31: "@",
  32: "#",
  33: "$",
  34: "%",
  35: "^",
  36: "&",
  37: "*",
  38: "(",
  39: ")",
  40: "-",
  41: "_",
  42: "=",
  43: "+",
  44: "[",
  45: "]",
  46: "\\",
  47: "{",
  48: "}",
  49: "|",
  50: ";",
  51: "'",
  52: ":",
  53: "\"",
  54: ",",
  55: ".",
  56: "/",
  57: "<",
  58: ">",
  59: "?",
  60: "a",
  61: "b",
  62: "c",
  63: "d",
  64: "e",
  65: "f",
  66: "g",
  67: "h",
  68: "i",
  69: "j",
  70: "k",
  71: "l",
  72: "m",
  73: "n",
  74: "o",
  75: "p",
  76: "q",
  77: "r",
  78: "s",
  79: "t",
  80: "u",
  81: "v",
  82: "w",
  83: "x",
  84: "y",
  85: "z",
  86: "0",
  87: "1",
  88: "2",
  89: "3",
  90: "4",
  91: "5",
  92: "6",
  93: "7",
  94: "8",
  95: "9",
  96: "\n",
}

var dictlength = 96
# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

func get_key(val):
	var lolly = 0
	for value in encryptDict.values():
		lolly += 1
		if val == value:
			 return lolly
 
	return 100000000


func encrypt(plainText):
#	print(keylist)
	
	#plainText = plainText.upper()
	

	var cryptText = ""
	
	var keyIter = 0
	for character in plainText:
		while keyIter > len(keylist) - 1:
			keyIter -= len(keylist)
#            print(keyIter)
#		print(character)
#		print(get_key(character))
#		print(keylist[keyIter])
		 
		if get_key(character) == 100000000:
			$AcceptDialog.popup()
			return
		
		var thing = get_key(character) + keylist[keyIter]
		if thing > dictlength:
			thing -= dictlength
		#print(thing)
		cryptText += encryptDict[thing]
		#print(encryptDict[thing])
		keyIter += 1
	justeodd = true
	return cryptText

func decrypt(plainText):

	var decryptText = ""
	#plaintext = plainText.upper()

	var keyIter = 0
	for character in plainText:
		while keyIter > len(keylist) - 1:
			keyIter -= len(keylist)
#            print(keyIter)
#		print(character)
#		print(get_key(character))
#		print(keylist[keyIter])
		var thing = get_key(character) - keylist[keyIter]
		if thing < 1:
			thing += dictlength
#			print("OverStepped The Line with", thing, dictlength)
		#print(thing)
		decryptText += encryptDict[thing]
		#print(encryptDict[thing])
		keyIter += 1

	#decryptText = decryptText.lower()
	return decryptText
	
func _process(delta):
	pass


func _on_Timer_timeout():
	if !keyed:
		return
	
	clippy = OS.get_clipboard()
	if clippy == old_clippy:
		return
	if justeodd:
		justeodd = false
		return
	if clippy.count(" ") < 4 and clippy.length() > 20:
		$Decrypt_notification/Label2.text = "This is the text decrypted:\n" + decrypt(clippy)
		$Decrypt_notification.popup()
#		print("Data, sir!")
	old_clippy = OS.get_clipboard()
#	print("Clean")
