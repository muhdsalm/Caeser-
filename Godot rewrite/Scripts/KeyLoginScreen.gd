extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_LoadKeyButton_button_down():
	$OpenKeyFileDialog.popup()


func _on_OpenKeyFileDialog_file_selected(path):
	var f = File.new()
	f.open(path, 1)
	Eod.key(int(f.get_as_text()))
	get_tree().change_scene("res://Scenes/main.tscn")
	Eod.keyed = true


func _on_CreateKey_button_down():
	$CreateKeyFileDialog.popup()



func _on_CreateKeyFileDialog_file_selected(path):
	var f = File.new()
	var r = RandomNumberGenerator.new()
	r.randomize()
	var key = r.randi_range(1000000000000, 1000000000000000000)
	key *= r.randi_range(10000000000, 1000000000000000000)
	#key *= -1
	f.open(path, 2)
	f.store_string(String(key))
	Eod.key(key)
	get_tree().change_scene("res://Scenes/main.tscn")
	Eod.keyed = true


func _on_Button_button_down():
	get_tree().change_scene("res://Scenes/help.tscn")
