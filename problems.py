# conditions, effects
problems = [

{
	"name": "Clickediclick",

	"steps": 25,

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
	"name": "Asymmetric Ships and Factories and Banks",

	"steps": 50,

	"oneof" : [
		#["do nothing", [],[]],
		["manual click", [],[["add", "money",1],]],
		["buy ship", [["atleast", "money",10],], [["add", "money", -10], ["add", "ship", 1]]],
		["sell ship", [["atleast", "ship",1],],[["add", "money", 5], ["add", "ship", -1]]],
		["buy factory", [["atleast", "money",20],], [["add", "money", -20], ["add", "factory", 1]]],
		["sell factory", [["atleast", "factory",1],],[["add", "money", 10], ["add", "factory", -1]]],
		["buy bank", [["atleast", "money",35],], [["add", "money", -35], ["add", "bank", 1]]],
		["sell bank", [["atleast", "factory",1],],[["add", "money", 15], ["add", "bank", -1]]],
	],

	"always" : [
		["ship income", [], [["addMultiply", "money", "ship", 3],]],
		["factory income", [], [["addMultiply", "money", "factory", 5],]],
		["bank income", [], [["addMultiply", "money", "factory", 9],]],
	],

	"score": ["get", "money"]
},
]
