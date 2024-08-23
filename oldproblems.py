oldproblems = [

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
		["rotate A,B,C", "", "A,B,C = C,A,B"],
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
]