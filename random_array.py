import random


INTEGER_COUNT = 10
FLOAT_COUNT = 10
INTEGER_RANGE = (1, 100)
FLOAT_RANGE = (0.0, 1.0)


def inspect_values(name, values):
	"""Print the values, type, and observed range for a sequence."""
	print(f"{name}: {values}")
	print(f"  type: {type(values[0]).__name__}")
	print(f"  count: {len(values)}")
	print(f"  observed range: {min(values)} to {max(values)}")


def main():
	integers = [random.randint(*INTEGER_RANGE) for _ in range(INTEGER_COUNT)]
	floats = [random.uniform(*FLOAT_RANGE) for _ in range(FLOAT_COUNT)]

	print("Configured ranges:")
	print(f"  integers: {INTEGER_RANGE[0]} to {INTEGER_RANGE[1]} (inclusive)")
	print(f"  floats: {FLOAT_RANGE[0]} to {FLOAT_RANGE[1]}")
	print()

	inspect_values("Random integers", integers)
	inspect_values("Random floats", floats)


if __name__ == "__main__":
	main()
