# conditions, effects
problems = [

{
	"name": "Clickediclick",

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
]
