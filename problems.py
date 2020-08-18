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
		#["do nothing", [],[]],
		["manual click", [],[["add", "money",1],]],
	],

	"always" : [
	],

	"score": ["get", "money"]
},

{
	"name": "Symmetric Ships and Factories",

	"difficulty": "medium",

	"background": "snf.png",

	"steps": 25,

	"start": {
		"money": 0,
	},

	"oneof" : [
		#["do nothing", [],[]],
		["manual click", [],[["add", "money",1],]],
		["buy ship", [["atleast", "money",10],], [["add", "money", -10], ["add", "ship", 1]]],
		["sell ship", [["atleast", "ship",1],],[["add", "money", 10], ["add", "ship", -1]]],
		["buy factory", [["atleast", "money",20],], [["add", "money", -20], ["add", "factory", 1]]],
		["sell factory", [["atleast", "factory",1],],[["add", "money", 20], ["add", "factory", -1]]],
	],

	"always" : [
		["ship income", [], [["addMultiply", "money", "ship", 3],]],
		["factory income", [], [["addMultiply", "money", "factory", 5],]],
	],

	"score": ["get", "money"]
},

{
	"name": "Asymmetric Ships and Factories",

	"difficulty": "medium",

	"background": "snf.png",

	"steps": 25,

	"start": {
		"money": 0,
	},

	"oneof" : [
		#["do nothing", [],[]],
		["manual click", [],[["add", "money",1],]],
		["buy ship", [["atleast", "money",10],], [["add", "money", -10], ["add", "ship", 1]]],
		["sell ship", [["atleast", "ship",1],],[["add", "money", 5], ["add", "ship", -1]]],
		["buy factory", [["atleast", "money",20],], [["add", "money", -20], ["add", "factory", 1]]],
		["sell factory", [["atleast", "factory",1],],[["add", "money", 10], ["add", "factory", -1]]],
	],

	"always" : [
		["ship income", [], [["addMultiply", "money", "ship", 3],]],
		["factory income", [], [["addMultiply", "money", "factory", 5],]],
	],

	"score": ["get", "money"]
},

{
	"name": "Asymmetric Complex",

	"difficulty": "hard",

	"steps": 50,

	"start": {
		"money": 5,
	},

	"oneof" : [
		#["do nothing", [],[]],
		["manual click", [],[["add", "money",1],]],
		["buy ship", [["atleast", "money",10],], [["add", "money", -10], ["add", "ship", 1]]],
		["sell ship", [["atleast", "ship",1],],[["add", "money", 5], ["add", "ship", -1]]],
		["buy factory", [["atleast", "money",20],], [["add", "money", -20], ["add", "factory", 1]]],
		["sell factory", [["atleast", "factory",1],],[["add", "money", 10], ["add", "factory", -1]]],
		["buy workshop", [["atleast", "money",35],], [["add", "money", -35], ["add", "workshop", 1]]],
		["sell workshop", [["atleast", "workshop",1],],[["add", "money", 15], ["add", "workshop", -1]]],
		["buy bank", [["atleast", "money",60],], [["add", "money", -60], ["add", "bank", 1]]],
		["sell bank", [["atleast", "bank",1],],[["add", "money", 30], ["add", "bank", -1]]],
	],

	"always" : [
		["ship income", [], [["addMultiply", "money", "ship", 3],]],
		["factory income", [], [["addMultiply", "money", "factory", 5],]],
		["workshop income", [], [["addMultiply", "money", "workshop", 9],]],
		["bank income", [], [["addMultiply", "money", "bank", 15],]],
	],

	"score": ["get", "money"]
},

{
	"name": "Expendable Boosters",

	"difficulty": "hard",

	"steps": 40,

	"start": {
		"money": 5,
	},

	"oneof" : [
		#["do nothing", [],[]],
		["manual click", [],[["add", "money",1],]],
		["buy ship", [["atleast", "money",10],], [["add", "money", -10], ["add", "ship", 1]]],
		["sell ship", [["atleast", "ship",1],],[["add", "money", 5], ["add", "ship", -1]]],
		["buy factory", [["atleast", "money",20],], [["add", "money", -20], ["add", "factory", 1]]],
		["sell factory", [["atleast", "factory",1],],[["add", "money", 10], ["add", "factory", -1]]],
		["buy workshop", [["atleast", "money",35],], [["add", "money", -35], ["add", "workshop", 1]]],
		["sell workshop", [["atleast", "workshop",1],],[["add", "money", 15], ["add", "workshop", -1]]],
		["buy booster", [["atleast", "money",60],["equal", "booster", 0],], [["add", "money", -60], ["add", "booster", 1], ["setkey", "boostertimer", 3]]],
	],

	"always" : [
		["income zero", [], [["setkey", "income", 0]]],
		["ship income", [], [["addMultiply", "income", "ship", 3],]],
		["factory income", [], [["addMultiply", "income", "factory", 5],]],
		["workshop income", [], [["addMultiply", "income", "workshop", 9],]],
		["unboosted income", [["equal", "booster", 0]], [["addMultiply", "money", "income", 1]]],
		["income booster", [["atleast", "booster", 1]], [["addMultiply", "money", "income", 2]]],
		["boostertimer decrease", [["atleast", "boostertimer", 1]], [["add", "boostertimer", -1],]],
		["booster kill", [["equal", "boostertimer", 0]], [["setkey", "booster", 0]]],
	],

	"score": ["get", "money"]
},

{
	"name": "Linear Increasing Costs (No sell)",

	"difficulty": "medium",

	"steps": 35,

	"start": {
		"money": 50,
		"shipcost": 10,
		"factorycost": 30,
		"workshopcost": 50,
	},

	"oneof" : [
		#["do nothing", [],[]],
		["manual click", [],[["add", "money",1],]],
		["buy ship", [["atleastkey", "money","shipcost"],], [["addMultiply", "money", "shipcost", -1], ["add", "ship", 1]]],
		["buy factory", [["atleastkey", "money","factorycost"],], [["addMultiply", "money", "factorycost", -1], ["add", "factory", 1]]],
		["buy workshop", [["atleastkey", "money","workshopcost"],], [["addMultiply", "money", "workshopcost", -1], ["add", "workshop", 1]]],
	],

	"always" : [
		["ship cost increase", [], [["add", "shipcost", 1]]],
		["factory cost increase", [], [["add", "factorycost", 1]]],
		["workshop cost increase", [], [["add", "workshopcost", 1]]],
		["ship income", [], [["addMultiply", "money", "ship", 3],]],
		["factory income", [], [["addMultiply", "money", "factory", 5],]],
		["workshop income", [], [["addMultiply", "money", "workshop", 9],]],
	],

	"score": ["get", "money"]
},

{
	"name": "Exponentially Increasing Costs (No sell)",

	"difficulty": "medium",

	"steps": 35,

	"start": {
		"money": 50,
		"shipcost": 10,
		"factorycost": 30,
		"workshopcost": 50,
	},

	"oneof" : [
		#["do nothing", [],[]],
		["manual click", [],[["add", "money",1],]],
		["buy ship", [["atleastkey", "money","shipcost"],], [["addMultiply", "money", "shipcost", -1], ["add", "ship", 1]]],
		["buy factory", [["atleastkey", "money","factorycost"],], [["addMultiply", "money", "factorycost", -1], ["add", "factory", 1]]],
		["buy workshop", [["atleastkey", "money","workshopcost"],], [["addMultiply", "money", "workshopcost", -1], ["add", "workshop", 1]]],
	],

	"always" : [
		["ship cost increase", [], [["addMultiply", "shipcost", "shipcost", 0.05]]],
		["factory cost increase", [], [["addMultiply", "factorycost", "factorycost", 0.05]]],
		["workshop cost increase", [], [["addMultiply", "workshopcost", "workshopcost", 0.05]]],
		["ship income", [], [["addMultiply", "money", "ship", 3],]],
		["factory income", [], [["addMultiply", "money", "factory", 5],]],
		["workshop income", [], [["addMultiply", "money", "workshop", 9],]],
	],

	"score": ["get", "money"]
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
		#["do nothing", [],[]],
		["manual click", [],[["addMultiply", "money","clickincome",1],]],
		["buy level 1 boost", [["atleastkey", "money","l1cost"],], [["addMultiply", "money", "l1cost", -1], ["add", "clickincome", 1]]],
		["buy level 2 boost", [["atleastkey", "money","l2cost"],], [["addMultiply", "money", "l2cost", -1], ["add", "clickincome", 3]]],
		["buy level 3 boost", [["atleastkey", "money","l3cost"],], [["addMultiply", "money", "l3cost", -1], ["add", "clickincome", 5]]],
	],

	"always" : [
	],

	"score": ["get", "money"]
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
		#["do nothing", [],[]],
		["click A", [],[["addMultiply", "A","clickincome",1],]],
		["click B", [],[["addMultiply", "B","clickincome",1],]],
		["buy level 1 boost", [["atleastkey", "A","l1cost"],], [["addMultiply", "A", "l1cost", -1], ["add", "clickincome", 1]]],
		["buy level 2 boost", [["atleastkey", "B","l2cost"],], [["addMultiply", "B", "l2cost", -1], ["add", "clickincome", 3]]],
		["buy level 3 boost", [["atleastkey", "A","l3cost"],["atleastkey", "B","l3cost"],], [["addMultiply", "A", "l3cost", -1], ["addMultiply", "B", "l3cost", -1], ["add", "clickincome", 5]]],
	],

	"always" : [
	],

	"score": ["multiply", "A", "B"]
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
		["click A", [],[["setMultiply", "A", "A", 2],]],
		["click B", [],[["setMultiply", "B", "B", 2],]],
		["click C", [],[["setMultiply", "C", "C", 2],]],
	],

	"always" : [
		["da", [["atleast", "A", 1]], [["add", "A", -1]]],
		["db", [["atleast", "B", 1]], [["add", "B", -1]]],
		["dc", [["atleast", "C", 1]], [["add", "C", -1]]],
	],

	"score": ["multiplyMany", "A", "B", "C"]
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
		["click A", [],[["setMultiply", "A", "A", 2],]],
		["click B", [],[["setMultiply", "B", "B", 2],]],
		["click C", [],[["setMultiply", "C", "C", 2],]],
	],

	"always" : [
		["da", [], [["add", "A", -1]]],
		["db", [], [["add", "B", -1]]],
		["dc", [], [["add", "C", -1]]],
	],

	"score": ["multiplyMany", "A", "B", "C"]
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
		["A = A + 1", [],[["add", "A", 1],]],
		["A = A * 2", [],[["setMultiply", "A", "A", 2],]],
		["A = A / 3", [],[["setMultiply", "A", "A", 1/3],]],
		["rotate A,B,C", [],[["rotate", "A", "B", "C"],]],
	],

	"always" : [
		["value = (A/B)^C", [], [["AdivBtoC", "value", "A", "B", "C"]]],
	],

	"score": ["absoluteDifference", "value", 3.141592653589793]
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
		["do nothing", [],[]],
		["increase thrust", [],[["add", "thrust", 1],]],
		["decrease thrust", [],[["add", "thrust", -1],]],
	],

	"always" : [
		["gravity acceleration", [], [["addkey", "acceleration", "gravity"], ["addkey", "acceleration", "thrust"], ["addkey", "velocity", "acceleration"], ["addkey", "height", "velocity"]]],
		["crash", [["atmost", "height", -1]], [["setkey", "height", -1000000]]]
	],

	"score": ["absoluteDifference", "height", 0]
},

{
	"name": "Crafting Table and Cooked Fish",

	"difficulty": "easy",

	"steps": 70,

	"start": {
	},

	"oneof" : [
		["collect logs", [],[["add", "logs", 1],]],
		["craft planks", [["atleast", "logs", 1]], [["add", "logs", -1], ["add", "planks", 4]]],
		["craft sticks", [["atleast", "planks", 2]],[["add", "planks", -2], ["add", "sticks", 4],]],
		["craft wooden pickaxe", [["atleast", "sticks", 2], ["atleast", "planks", 3]], [["add", "sticks", -2], ["add", "planks", -3], ["add", "pickaxe", 5],]],
		["mine cobblestone", [["atleast", "pickaxe", 1]], [["add", "pickaxe", -1], ["add", "cobblestone", 1],]],
		["craft oven", [["atleast", "cobblestone", 8]], [["add", "cobblestone", -1], ["add", "oven", 1]]],
		["craft stone pickaxe", [["atleast", "sticks", 2], ["atleast", "cobblestone", 3]], [["add", "sticks", -2], ["add", "cobblestone", -3], ["add", "pickaxe", 10],]],
		["mine coal", [["atleast", "pickaxe", 2]], [["add", "pickaxe", -2], ["add", "coal", 1],]],
		["craft stone sword", [["atleast", "sticks", 1], ["atleast", "cobblestone", 2]], [["add", "sticks", -1], ["add", "cobblestone", -2], ["add", "sword", 5],]],
		["kill spider", [["atleast", "sword", 1],], [["add", "sword", -1], ["add", "string", 1],]],
		["fishing rod", [["atleast", "sticks", 3], ["atleast", "string", 2]], [["add", "sticks", -1], ["add", "string", -2], ["add", "fishing rod", 3]]],
		["fish", [["atleast", "fishing rod", 1],], [["add", "fishing rod", -1], ["add", "fish", 1],]],
		["cook fish", [["atleast", "coal", 1], ["atleast", "fish", 1], ["atleast", "oven", 1]], [["add", "coal", -1], ["add", "fish", -1], ["add", "cooked fish", 1]]]
	],

	"always" : [
	],

	"score": ["get", "cooked fish"]
},

]
