def Hanoi(n, Start, Other, End):
	if n == 1:
		print("Move disk", n, "from", Start, "to", End)
	else:
		Hanoi(n - 1, Start, End, Other)
		print("Move disk", n, "from", Start, "to", End)
		Hanoi(n - 1, Other, Start, End)


Hanoi(4, "Left Tower", "Middle Tower", "Right Tower")
