# Python script to demonstrate a custom iterator

class PlusCounter:
    """
    A simple iterator that counts up from a starting number to an end number,
    incrementing it by a specified number (default = 1)

    Attributes:
        current (int): The current value in the iteration.
        end (int): The end/maximum value (inclusive) the counter should reach in the iteration.
        step (int): The specified value to increment the counter on each iteration.
    """

    def __init__(self, start, end, step=1):
        """
        Initialize the PlusCounter object/instance.

        Arguments:
            start (int): The starting value.
            end (int): The end/maximum value (inclusive) the counter should reach in the iteration.
            step (int): The specified value to increment the counter on each iteration.
        """
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            PlusCounter: The iterator object/instance.
        """
        return self

    def __next__(self):
        """
        Returns the next value in the iterator (or next number in the sequence).

        Raises:
            StopIteration: If the current value is greater than the end value.

        Returns:
            int: The next value in the iterator/sequence.
        """
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += self.step
            return self.current - 1


# Create / instantiate a PlusCounter object
my_counter = PlusCounter(1, 10)
# Iterate over the counter object
for num in my_counter:
    print(num)

print("\n")

# Create / instantiate another PlusCounter object to give the multiples of 5 from 1 - 75
my_counter_2 = PlusCounter(1, 75, 5)
for num in my_counter_2:
    print(num)
print("\n")
