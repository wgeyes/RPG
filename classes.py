import moves
import itertools

def combo(cls):
	cls.moves |= set(itertools.chain.from_iterable(x.moves for x in cls.__bases__))
	return cls
def bcombo(cls=None, **kwargs):
	if cls is not None:
		cls.bases = dict(cls.bases)
		sup_bases = [x.bases for x in cls.__bases__]
		n_bases = {}
		for i in sup_bases[0]:
			all = [base[i] for base in sup_bases]
			cls.bases[i] = sum(all) / len(all) * 1.2
		return cls
	else:
		def _wrap(cls):
			cls = bcombo(cls)
			for k, v in kwargs.items():
				cls.bases[k] = cls.bases[k] * v // 1
			return cls
		return _wrap

class BaseClass:
	bases = {}
	moves = {moves.punch}
@combo
class Warrior(BaseClass):
	bases = dict(hp=19, mp=4, attack=23, defense=16, wisdom=7, speed=15)
	moves = {moves.kick}
@combo
class Mage(BaseClass):
	bases = dict(hp=12, mp=20, attack=6, defense=9, wisdom=22, speed=13)
	moves = {moves.flame}
@combo
class Priest(BaseClass):
	bases = dict(hp=11, mp=19, attack=8, defense=5, wisdom=23, speed=14)
	moves = {moves.heal}
@combo
class Bard(BaseClass):
	bases = dict(hp=18, mp=11, attack=14, defense=13, wisdom=13, speed=11)
	moves = {moves.chill}
@combo
class Ninja(BaseClass):
	bases = dict(hp=12, mp=5, attack=18, defense=14, wisdom=7, speed=24)
@combo
class Guard(BaseClass):
	bases = dict(hp=22, mp=6, attack=15, defense=23, wisdom=4, speed=10)
	#moves.defend]
# advanced classes
@combo
@bcombo
class Theurge(Mage, Priest):
	pass
@combo
@bcombo
class Gladiator(Warrior, Ninja):
	pass#dict(hp=22, mp=8, attack=30, defense=18, wisdom=8, speed=14)
@combo
@bcombo(mp=1.5, wisdom=1.2)
class Sage(Mage):
	pass#dict(hp=12, mp=32, attack=4, defense=8, wisdom=28, speed=16)
	
"""class Saint(BaseClass):
	bases = dict(hp=12, mp=24, attack=7, defense=7, wisdom=32, speed=18)
class Joker(BaseClass):
	bases = dict(hp=20, mp=16, attack=16, defense=16, wisdom=16, speed=16)
class Master(BaseClass):
	bases = dict(hp=15, mp=10, attack=23, defense=12, wisdom=10, speed=30)
class Paladin(BaseClass):
	bases = dict(hp=27, mp=14, attack=21, defense=24, wisdom=12, speed=2)"""

classes = dict(warrior=Warrior, mage=Mage, priest=Priest, bard=Bard, ninja=Ninja, guard=Guard, theurge=Theurge, gladiator=Gladiator, sage=Sage)#, saint=Saint, joker=Joker, master=Master, paladin=Paladin)