# Python 3.10+ code demonstrating pattern matching with match-case statements

# point is an (x, y) tuple
point = (0, 12)
match point:
	case (0, 0):
		print("Origin")
	case (0, y):
		print(f"Y={y}")
	case (x, 0):
		print(f"X={x}")
	case (x, y):
		print(f"X={x}, Y={y}")
	case _:
		raise ValueError("Not a point")

# O/p: Y=12

class Point:
	__match_args__ = ('x', 'y') # Indicates the attributes to match against in "match"-case statements only
                                # This is optional, but helps with clarity in pattern matching
	def __init__(self, x, y):
		self.x = x
		self.y = y

def where_is(point):
	match point:
		case Point(x=0, y=0):
			print("Origin")
		case Point(x=0, y=y):
			print(f"Y={y}")
		case Point(x=x, y=0):
			print(f"X={x}")
		case Point(x, y) if x == y:
			print(f"Y=X at {x}")
		case Point(x, y):
			print(f"Not on the diagonal")
		case _:
			print("Not a point")

# Example for matching lists of points
def where_are(points):
	match points:
		case []:
			print("No points")
		case [Point(0, 0)]:
			print("The origin")
		case [Point(x, y)]:
			print(f"Single point {x}, {y}")
		case [Point(0, y1), Point(0, y2)]:
			print(f"Two on the Y axis at {y1}, {y2}")
		case _:
			print("Not a recognized pattern")

where_is(Point(0, 12))
# O/p: Y=12
where_is(Point(3, 0))
# O/p: X=3
where_is(Point(5, 5))
# O/p: Y=X at 5
where_is(Point(1, 2))
# O/p: Not on the diagonal


where_are([Point(0, 0)])
# O/p: The origin
where_are([Point(0, 12)])
# O/p: Single point 0, 12
where_are([Point(0, 12), Point(0, 15)])
# O/p: Two on the Y axis at 12, 15
where_are([])
# O/p: No points
where_are([Point(1, 2), Point(3, 4)])
# O/p: Not a recognized pattern

# Subpatterns may be captured using the as keyword:
# case (Point(x1, y1), Point(x2, y2) as p2): ...