extends Node2D

@onready var door: Area2D = $Door

func _ready() -> void:
	$Key.collected.connect(on_key_collected)
	$Door.player_success.connect(on_player_success)
	
func on_key_collected():
	$Player.has_key = true
	$Door.open()
	
func on_player_success():
	$SuccessLabel.visible = true
	print("Ganamo")
