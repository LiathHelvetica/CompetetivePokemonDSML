from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from db.meta_utilities import BASE

# TODO: Smooth relationships
# TODO: Strongest moves of type
# TODO: most popular moves
# TODO: can_do_this

POKEMON_NAME_MAX_LENGTH = 11
TYPE_NAME_MAX_LENGTH = 8


class Pokemon(BASE):
	__tablename__ = "pokemon"

	id = Column(Integer, primary_key=True, autoincrement=True)
	pokedex_id = Column(Integer)
	name = Column(String(POKEMON_NAME_MAX_LENGTH))
	type_1 = Column(Integer, ForeignKey("type.id"))
	type_2 = Column(Integer, ForeignKey("type.id"))
	hp = Column(Integer)
	attack = Column(Integer)
	defense = Column(Integer)
	special_attack = Column(Integer)
	special_defense = Column(Integer)
	speed = Column(Integer)
	ability_1 = Column(Integer, ForeignKey("ability.id"))
	ability_2 = Column(Integer, ForeignKey("ability.id"))
	hidden_ability = Column(Integer, ForeignKey("ability.id"))
	weight = Column(Float)


class Type(BASE):
	__tablename__ = "type"

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(TYPE_NAME_MAX_LENGTH))


class Ability(BASE):
	__tablename__ = "ability"

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String)
	description = Column(String)


class Move(BASE):
	__tablename__ = "move"

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String)
	type = Column(String(TYPE_NAME_MAX_LENGTH), ForeignKey("type.id"))
	category = Column(String)  # TODO: Enum ?
	max_pp = Column(Integer)
	power = Column(Integer)
	accuracy = Column(Integer)  # null if always hits
	description = Column(String)
	is_1_KO = Column(Boolean)
	# TODO: is bind used
	chance_to_burn = Column(Integer)
	chance_to_freeze = Column(Integer)
	chance_to_paralyze = Column(Integer)
	chance_to_poison = Column(Integer)
	chance_to_sleep = Column(Integer)
	chance_to_confuse = Column(Integer)
	chance_to_flinch = Column(Integer)
	boon_to_attack = Column(Integer)
	boon_to_defense = Column(Integer)
	boon_to_special_attack = Column(Integer)
	boon_to_special_defense = Column(Integer)
	boon_to_speed = Column(Integer)
	must_recharge = Column(Boolean)
	must_set_up = Column(Boolean)


class Item(BASE):
	__tablename__ = "item"

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String)
	consumable = Column(Boolean)
	is_berry = Column(Boolean)
	description = Column(String)


class MoveSet(BASE):
	__tablename__ = "move_set"

	pokemon_id = Column(Integer, ForeignKey("pokemon.id"))
	move_id = Column(Integer, ForeignKey("move.id"))
