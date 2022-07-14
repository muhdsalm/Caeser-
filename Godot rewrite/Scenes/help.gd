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


func _on_BackButton_button_down():
	get_tree().change_scene("res://Scenes/KeyLoginScreen.tscn")


func _on_NextButton_button_down():
	get_tree().change_scene("res://Scenes/help2.tscn")


func _on_Help2BackButton_button_down():
	get_tree().change_scene("res://Scenes/help.tscn")
