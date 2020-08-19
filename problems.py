# conditions, effects
problems = [

{
	"name": "Clickediclick",

	"difficulty": "easy",

	"steps": 15,

	"start": {
		"money": 0,
	},

	"oneof" : [
		["manual click", "", "money += 1"],
	],

	"always" : [
	],

	"score": "money"
},

{
	"name": "Symmetric Ships and Factories",

	"difficulty": "medium",

	"background": "snf.png",

	"steps": 25,

	"start": {
		"money": 0,
		"ship": 0,
		"factory": 0,
	},

	"oneof" : [
		#["do nothing", "",""],
		["manual click", "", "money += 1"],
		["buy ship", "money >= 10", "money -= 10;ship += 1"],
		["sell ship", "ship >= 1", "money += 10;ship -= 1"],
		["buy factory", "money >= 20", "money -= 20;factory += 1"],
		["sell factory", "factory >= 1", "money += 20;factory -= 1"],
	],

	"always" : [
		["ship income", "", "money += ship * 3"],
		["factory income", "", "money += factory * 5"],
	],

	"score": "money"
},

{
	"name": "Asymmetric Ships and Factories",

	"difficulty": "medium",

	"background": "snf.png",

	"steps": 25,

	"start": {
		"money": 0,
		"ship": 0,
		"factory": 0,
	},

	"oneof" : [
		["manual click", "", "money += 1"],
		["buy ship", "money >= 10", "money -= 10;ship += 1"],
		["sell ship", "ship >= 1", "money += 5;ship -= 1"],
		["buy factory", "money >= 20", "money -= 20;factory += 1"],
		["sell factory", "factory >= 1", "money += 10;factory -= 1"],
	],

	"always" : [
		["ship income", "", "money += ship * 3"],
		["factory income", "", "money += factory * 5"],
	],

	"score": "money"
},

{
	"name": "Asymmetric Complex",

	"difficulty": "hard",

	"steps": 50,

	"start": {
		"money": 5,
		"ship": 0,
		"factory": 0,
		"workshop": 0,
		"bank": 0
	},

	"oneof" : [
		["manual click", "", "money += 1"],
		["buy ship", "money >= 10", "money -= 10;ship += 1"],
		["sell ship", "ship >= 1", "money += 5;ship -= 1"],
		["buy factory", "money >= 20", "money -= 20;factory += 1"],
		["sell factory", "factory >= 1", "money += 10;factory -= 1"],
		["buy workshop", "money >= 35", "money -= 35;workshop += 1"],
		["sell workshop", "workshop >= 1", "money += 15;workshop -= 1"],
		["buy bank", "money >= 60", "money -= 60;bank += 1"],
		["sell bank", "bank >= 1", "money += 30;bank -= 1"],
	],

	"always" : [
		["ship income", "", "money += ship * 3"],
		["factory income", "", "money += factory * 5"],
		["workshop income", "", "money += workshop * 9"],
		["bank income", "", "money += bank * 15"],
	],

	"score": "money"
},

{
	"name": "Expendable Boosters",

	"difficulty": "hard",

	"steps": 40,

	"start": {
		"money": 5,
		"ship": 0,
		"factory": 0,
		"workshop": 0,
		"booster": 0,
		"boostertimer": 0
	},

	"oneof" : [
		["manual click", "", "money += 1"],
		["buy ship", "money >= 10", "money -= 10;ship += 1"],
		["sell ship", "ship >= 1", "money += 5;ship -= 1"],
		["buy factory", "money >= 20", "money -= 20;factory += 1"],
		["sell factory", "factory >= 1", "money += 10;factory -= 1"],
		["buy workshop", "money >= 35", "money -= 35;workshop += 1"],
		["sell workshop", "workshop >= 1", "money += 15;workshop -= 1"],
		["buy booster", "booster == 0 and money >= 60", "money -= 60;booster += 1;boostertimer = 3"],
	],

	"always" : [
		["income zero", "", "income = 0"],
		["ship income", "", "income += ship * 3"],
		["factory income", "", "income += factory * 5"],
		["workshop income", "", "income += workshop * 9"],
		["unboosted income", "booster == 0", "money += income"],
		["income booster", "booster >= 1", "money += income * 2"],
		["boostertimer decrease", "boostertimer > 1", "boostertimer -= 1"],
		["booster kill", "boostertimer == 0", "booster = 0"],
	],

	"score": "money"
},

{
	"name": "Linear Increasing Costs (No sell)",

	"difficulty": "medium",

	"steps": 35,

	"start": {
		"money": 50,
		"ship": 0,
		"factory": 0,
		"workshop": 0,
		"shipcost": 10,
		"factorycost": 30,
		"workshopcost": 50,
	},

	"oneof" : [
		["manual click", "", "money += 1"],
		["buy ship", "money >= shipcost", "money -= shipcost;ship += 1"],
		["buy factory", "money >= factorycost", "money -= factorycost;factory += 1"],
		["buy workshop", "money >= workshopcost", "money -= workshopcost;workshop += 1"],
	],

	"always" : [
		["ship cost increase", "", "shipcost += 1"],
		["factory cost increase", "", "factorycost += 1"],
		["workshop cost increase", "", "workshopcost += 1"],
		["ship income", "", "money += ship * 3"],
		["factory income", "", "money += factory * 5"],
		["workshop income", "", "money += workshop * 9"],
	],

	"score": "money"
},

{
	"name": "Exponentially Increasing Costs (No sell)",

	"difficulty": "medium",

	"steps": 35,

	"start": {
		"money": 50,
		"ship": 0,
		"factory": 0,
		"workshop": 0,
		"shipcost": 10,
		"factorycost": 30,
		"workshopcost": 50,
	},

	"oneof" : [
		["manual click", "", "money += 1"],
		["buy ship", "money >= shipcost", "money -= shipcost;ship += 1"],
		["buy factory", "money >= factorycost", "money -= factorycost;factory += 1"],
		["buy workshop", "money >= workshopcost", "money -= workshopcost;workshop += 1"],
	],

	"always" : [
		["ship cost increase", "", "shipcost *= 1.05"],
		["factory cost increase", "", "factorycost *= 1.05"],
		["workshop cost increase", "", "workshopcost *= 1.05"],
		["ship income", "", "money += ship * 3"],
		["factory income", "", "money += factory * 5"],
		["workshop income", "", "money += workshop * 9"],
	],

	"score": "money"
},

{
	"name": "Mouseclick Boosters",

	"difficulty": "easy",

	"steps": 25,

	"start": {
		"money": 5,
		"clickincome": 1,
		"l1cost": 5,
		"l2cost": 7,
		"l3cost": 11
	},

	"oneof" : [
		["manual click", "","money += clickincome"],
		["buy level 1 boost", "money >= l1cost", "money -= l1cost;clickincome += 1"],
		["buy level 2 boost", "money >= l2cost", "money -= l2cost;clickincome += 3"],
		["buy level 3 boost", "money >= l3cost", "money -= l3cost;clickincome += 5"],
	],

	"always" : [
	],

	"score": "money"
},

{
	"name": "The A's and the B's",

	"difficulty": "medium",

	"steps": 25,

	"start": {
		"A": 0,
		"B": 0,
		"clickincome": 1,
		"l1cost": 5,
		"l2cost": 7,
		"l3cost": 11
	},

	"oneof" : [
		["click A", "", "A += clickincome"],
		["click B", "", "B += clickincome"],
		["buy level 1 boost", "A >= l1cost", "A -= l1cost;clickincome += 1"],
		["buy level 2 boost", "B >= l2cost", "B -= l2cost;clickincome += 3"],
		["buy level 3 boost", "A >= l3cost and B >= l3cost", "A -= l3cost;B -= l3cost;clickincome += 5"],
	],

	"always" : [
	],

	"score": "A*B"
},

{
	"name": "ABC-0",

	"difficulty": "easy",

	"steps": 35,

	"start": {
		"A": 4,
		"B": 5,
		"C": 6,
	},

	"oneof" : [
		["click A", "", "A *= 2"],
		["click B", "", "B *= 2"],
		["click C", "", "C *= 2"],
	],

	"always" : [
		["da", "A >= 1", "A -= 1"],
		["db", "B >= 1", "B -= 1"],
		["dc", "C >= 1", "C -= 1"],
	],

	"score": "A*B*C"
},


{
	"name": "ABC-1",

	"difficulty": "easy",

	"steps": 35,

	"start": {
		"A": 5,
		"B": 5,
		"C": 5,
	},

	"oneof" : [
		["click A", "", "A *= 2"],
		["click B", "", "B *= 2"],
		["click C", "", "C *= 2"],
	],

	"always" : [
		["da", "", "A -= 1"],
		["db", "", "B -= 1"],
		["dc", "", "C -= 1"],
	],

	"score": "A*B*C"
},

{
	"name": "Approximating Pi",

	"difficulty": "medium",

	"steps": 35,

	"start": {
		"value": 0,
		"A": 30,
		"B": 20,
		"C": 3,
	},

	"oneof" : [
		["A = A + 1", "", "A += 1"],
		["A = A * 2", "", "A *= 2"],
		["A = A / 3", "", "A /= 3"],
		["rotate A,B,C", "", "t=A;A=C;B=A;C=t"],
	],

	"always" : [
		["value = (A/B)^C", "B != 0", "value = (A/B)**C"],
	],

	"score": "abs(value-3.141592653589793)"
},

{
	"name": "Lunar Landing",

	"difficulty": "medium",

	"steps": 35,

	"start": {
		"height": 1000,
		"velocity": 0,
		"acceleration": 0,
		"thrust": 0,
		"gravity": -1.62,
	},

	"oneof" : [
		["do nothing", "",""],
		["increase thrust", "", "thrust += 1"],
		["decrease thrust", "", "thrust -= 1"],
	],

	"always" : [
		["gravity acceleration", "", "acceleration += gravity;acceleration += thrust;velocity += acceleration;height += velocity"],
		["crash", "height < 0", "height = -1000000"]
	],

	"score": "abs(height)"
},

{
	"name": "Crafting Table and Cooked Fish",

	"difficulty": "easy",

	"steps": 70,

	"start": {
		"logs": 0,
		"planks": 0,
		"sticks": 0,
		"pickaxe": 0,
		"cobblestone": 0,
		"oven": 0,
		"coal": 0,
		"sword": 0,
		"string": 0,
		"fishingrod": 0,
		"fish": 0,
		"cookedfish": 0,
	},

	"oneof" : [
		["collect logs", "","logs += 1"],
		["craft planks", "logs >= 1", "logs -= 1;planks += 4"],
		["craft sticks", "planks >= 2", "planks -= 2;sticks += 4"],
		["craft wooden pickaxe", "sticks >= 2 and planks >= 3", "sticks -= 2;planks -= 3;pickaxe += 5"],
		["mine cobblestone", "pickaxe >= 1", "pickaxe -= 1;cobblestone += 1"],
		["craft oven", "cobblestone >= 8", "cobblestone -= 8;oven += 1"],
		["craft stone pickaxe", "sticks >= 2 and cobblestone >= 3", "sticks -= 2;cobblestone -= 3;pickaxe += 10"],
		["mine coal", "pickaxe >= 2", "pickaxe -= 2;coal += 1"],
		["craft stone sword", "sticks >= 1 and cobblestone >= 2", "sticks -= 1;cobblestone -= 2;sword += 5"],
		["kill spider", "sword >= 1", "sword -= 1;string += 1"],
		["craft fishing rod", "sticks >= 3 and string >= 2", "sticks -= 3;string -= 2;fishingrod += 3"],
		["fish", "fishingrod >= 1", "fishingrod -= 1;fish += 1"],
		["cook fish", "oven >= 1 and fish >= 1 and coal >= 1", "fish -= 1;coal -= 1;cookedfish += 1"],
	],

	"always" : [
	],

	"score": "cookedfish"
},

]
