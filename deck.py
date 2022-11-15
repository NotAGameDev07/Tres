import random


class Card:
	#default card class
	def __init__(self, color, ID, iswild=False):
		#has basic attrs such as color, ID, and iswild
		self.color = color
		self.id = ID
		self.iswild = iswild
	#to make comparisons easier and not have to compare all attributes in every if statement
	def __eq__(self, other):
		return self.color == other.color or self.id == other.id or self.iswild
	def __str__(self):
		return f"({self.color}, {self.id})"
	__repr__ = __str__

class SCard(Card):
	#custom card class
	def __init__(self, color, ID, power, draw=0, skamt=0, iswild=False):
		#inits default attributes
		super().__init__(color, ID, iswild)
		#inits and sets draw amount and isskip
		self.draw = int(draw)
		self.skamt = int(skamt)
		self.isskip = int(skamt) > 0
	def __str__(self):
		return f'({self.color}, {self.id}, {self.draw}, {self.skamt})'
	__repr__ = __str__

class CCard(Card):
	#custom card class
	def __init__(self, color, ID, code='', iswild=False):
		#inits default attributes
		super().__init__(color, ID, iswild)
		#inits code attr
		#code gets executed when card is played
		self.code = code

class Hand:
	def __init__(self, deck, cards = 7):
		self.deck = deck
		self.cards = cards
	def gen(self):
		return [random.choice(self.deck) for i in range(self.cards)]
	def __iter__(self):
		for i in self.gen():
			yield i

class UNO:
	def __init__(self, users, deck):
		#inits game
		self.users = users
		self.deck = deck
		self.douac = {i: Hand(deck).gen() for i in users}
		self.ccard = Hand(deck, 1).gen()[0]
		self.discard = []
		self.skamt = 0
		self.cpl = list(self.douac)
	def __iter__(self):
		#returns info of current game except deck
		yield self.users
		yield self.douac
		yield self.ccard
	#plays round, there is player id and index of card
	def round(self, player, ind, color=''):
		self.nextplayer = self.cpl[(self.cpl.index(player) + 1) % len(self.cpl)]
		print(self.nextplayer, player)
		print("SKAMT:", self.skamt)
		if self.skamt > 0:
			self.skamt -= 1
			return None
		pcard = self.douac[player][ind]
		if pcard.iswild and type(pcard) == CCard:
			#Executes code and discards card when card matches
			self.discard += [pcard]
			del self.douac[player][ind]
			self.ccard = pcard
			exec(pcard.code)
		elif pcard == self.ccard and type(pcard) == CCard:
			#Executes code and discards card when card matches
			self.discard += [pcard]
			del self.douac[player][ind]
			self.ccard = pcard
			exec(pcard.code)
		if pcard == self.ccard and type(pcard) == Card:
			#Puts card and discards card when card matches
			self.discard += [pcard]
			self.ccard = pcard
			del self.douac[player][ind]
		if pcard.iswild and type(pcard) == SCard:
			#Puts card and discards card when card matches
			if pcard.isskip:
				self.skamt += pcard.skamt
			if pcard.draw > 0:
				self.douac[self.nextplayer] += Hand(self.deck).gen(pcard.draw)
				print("HUH")
			pcard.iswild = False
			pcard.color = color
			self.discard += [pcard]
			self.ccard = pcard
			del self.douac[player][ind]
		elif pcard == self.ccard and type(pcard) == SCard:
			#Puts card and discards card when card matches
			self.ccard = pcard
			if pcard.isskip:
				self.skamt += pcard.skamt
			if pcard.draw > 0:
				self.douac[self.nextplayer] += Hand(self.deck, pcard.draw).gen()
				print("OKAY")
			self.discard += [pcard]
			del self.douac[player][ind]