# TRES, because UNO and DOS was taken

## How to currently run the application

### NOTE: This is currently CLI only, multiplayer is not yet supported

#### This is if the `python3` binary is ran when the `python` command is ran in the terminal

`python uno.py`

#### Else if you have python 3 and the `python3` binary is not ran when the `python` command is ran

`python3 uno.py`

# How to make custom cards

Make a new XML file with deck as root tag

```xml
<?xml version="1.0" encoding="UTF-8"?>
<deck>
</deck>
```

Then add any of the following tags, they are described as follows

> `<color id="X" name="Y"/>` defines a color in which you can put the following XML tags inside, X is the id of the color and Y is the name of the color, but the name of the color isn't used to compare if a card is playable or not while the id of the color is

---

> `<card id="X"/>` defines a card with no actions/custom actions with X being the id of the card

---

> `<scard id="X" type="Y"/>` defines a card with special actions but no custom actions, such as skip, draw, reverse, wild draw, and wild with X being the id of the card, and with Y being the type of action the card performs

---

> `<ccard id="X" ssc="Y" csc="Z">OPTIONAL</ccard>` defines a card with custom actions, the code to define custom actions is written in python with X being the id of the card, Y being the code ran on the server side, and Z being the code run on the client side, all attributes are required, inner text is optional as it is the card's description

---

> The entity tags are used for default cards, it is recommended that you add custom cards under another entity so you can shorten the XML file if each color has the same cards, the following is a short example of using vs not using XML entities

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE deck [
	<!ENTITY defcards '
		<card id="1"/>
		<card id="2"/>
		<card id="3"/>
		<card id="4"/>
		<card id="5"/>
		<card id="6"/>
		<card id="7"/>
		<card id="8"/>
		<card id="9"/>
		<card id="0"/>
		<scard id="SK" type="reverse"/>
		<scard id="RV" type="skip"/>
		<scard id="D2" type="draw" amount="2"/>
	'>
]>
<deck>
	<color id="R" name="Red">
		&defcards;
	</color>
	<color id="G" name="Red">
		&defcards;
	</color>
	<color id="B" name="Red">
		&defcards;
	</color>
	<color id="Y" name="Red">
		&defcards;
	</color>
</deck>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<deck>
	<color id="R" name="Red">
		<card id="1"/>
		<card id="2"/>
		<card id="3"/>
		<card id="4"/>
		<card id="5"/>
		<card id="6"/>
		<card id="7"/>
		<card id="8"/>
		<card id="9"/>
		<card id="0"/>
		<scard id="SK" type="reverse"/>
		<scard id="RV" type="skip"/>
		<scard id="D2" type="draw" amount="2"/>
	</color>
	<color id="G" name="Red">
		<card id="1"/>
		<card id="2"/>
		<card id="3"/>
		<card id="4"/>
		<card id="5"/>
		<card id="6"/>
		<card id="7"/>
		<card id="8"/>
		<card id="9"/>
		<card id="0"/>
		<scard id="SK" type="reverse"/>
		<scard id="RV" type="skip"/>
		<scard id="D2" type="draw" amount="2"/>
	</color>
	<color id="B" name="Red">
		<card id="1"/>
		<card id="2"/>
		<card id="3"/>
		<card id="4"/>
		<card id="5"/>
		<card id="6"/>
		<card id="7"/>
		<card id="8"/>
		<card id="9"/>
		<card id="0"/>
		<scard id="SK" type="reverse"/>
		<scard id="RV" type="skip"/>
		<scard id="D2" type="draw" amount="2"/>
	</color>
	<color id="Y" name="Red">
		<card id="1"/>
		<card id="2"/>
		<card id="3"/>
		<card id="4"/>
		<card id="5"/>
		<card id="6"/>
		<card id="7"/>
		<card id="8"/>
		<card id="9"/>
		<card id="0"/>
		<scard id="SK" type="reverse"/>
		<scard id="RV" type="skip"/>
		<scard id="D2" type="draw" amount="2"/>
	</color>
</deck>
```

---

### Here is an example, this may be the default deck in XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE deck [
	<!ENTITY sscode "your code here">
	<!ENTITY cscode "your code here">
	<!ENTITY defcards '
		<card id="1"/>
		<card id="2"/>
		<card id="3"/>
		<card id="4"/>
		<card id="5"/>
		<card id="6"/>
		<card id="7"/>
		<card id="8"/>
		<card id="9"/>
		<card id="0"/>
		<scard id="SK" type="reverse" skamt="6"/>
		<scard id="RV" type="skip"/>
		<scard id="D2" type="draw" amount="2"/>
		<ccard id="CC" ssc="&sscode;" csc="&cscode;">OPTIONAL TEXT</ccard>
	'>
]>
<deck>
	<color id="R" name="Red">
		&defcards;
	</color>
	<color id="G" name="Red">
		&defcards;
	</color>
	<color id="B" name="Red">
		&defcards;
	</color>
	<color id="Y" name="Yellow">
		&defcards;
	</color>
</deck>
```

# Variable Documentation

## self

> `self.douac` is a dictionary where the keys are the usernames of the player and the values are the decks of the players, the reason it's douac and not decks is because `douac` is an acronym for `dictionary of users and cards`

> `self.deck` is a list of cards that is being used by the current UNO game

> `self.players` is a list of all current players

> `self.ccard` is the current card

> `self.discard` is the list of cards that have been played from first to last, aka a discord pile

> `self.skamt` is the amount of consecutive skips to be done, this is normally `1` for vanilla UNO skips, but can be higher, for example `2` will skip the turn for the next player and the turn for the player after that, so the person that plays a custom skip card can be skipped by said card if `self.skamt` is large enough

> `self.reverse()` is the function to call that will reverse the order of the players

## Other variables

> `player` is the current player that is playing a card

> `ind` is the index of the array of cards that is the player's hand
