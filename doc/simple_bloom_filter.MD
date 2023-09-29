 # SIMPLE BLOOM FILTER
 
 In Python, integers are variable-size and can theoretically hold an unlimited number of bits, so you can use bitwise operations to manipulate the individual bits within an integer.

- The ```bit_array``` is initialized to 0, which represents an array of all 0 bits.
- The ```add``` method sets the bit at the calculated index to 1 using the bitwise OR ```(|)``` and bitwise shift ```(<<)``` operations.
- The ```__contains__``` method checks whether the bit at the calculated index is 1 using the bitwise AND ```(&)``` and bitwise shift ```(<<)``` operations.



