extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"

var eod = ""

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.
	
func eod():
	if eod == "encrypt":
		$OuputTextEdit.text = Eod.encrypt($InputTextEdit.text)
		if $InputTextEdit.text.count(" ") < 4 and $InputTextEdit.text.length() > 20:
			$Helper.text = "Did you mean to decrypt?"
		else:
			$Helper.text = ""
		
	if eod == "decrypt":
		$OuputTextEdit.text = Eod.decrypt($InputTextEdit.text)
		if $InputTextEdit.text.count(" ") > 4 and $InputTextEdit.text.length() > 20:
			$Helper.text = "Did you mean to encrypt?"
		else:
			$Helper.text = ""



# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_InputTextEdit_text_changed():
	eod()


func _on_EncyptBox_pressed():
	eod = "encrypt"
	$InputLabel.text = "Regular Text"
	$Output.text = "Encrypted Text"
	eod()


func _on_DecryptBox_pressed():
	eod = "decrypt"
	$InputLabel.text = "Encrypted Text"
	$Output.text = "Decrypted Text"
	eod()
	



func _on_CopyButton_button_down():
	OS.set_clipboard($OuputTextEdit.text)
	Eod.justeodd = true


func _on_CopyForDiscordButton_button_down():
	OS.set_clipboard("```" + $OuputTextEdit.text + "```")
	Eod.justeodd = true
