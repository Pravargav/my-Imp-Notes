`1)  3304. Find the K-th Character in String Game I `


`2) 2550. Count Collisions of Monkeys on a Polygon`

-> return (int) ((max + pow(n) - 2) % max);   

-> Adding max before taking % max ensures that the result remains non-negative;

-> 10^9+7 is a prime number, making it useful for modular arithmetic;

-> Integer.MAX_VALUE is larger (~2.1×10^9) than 1000000007;

-> 10^9+7 fulfills both the criteria. It is the first 10-digit prime number and fits in int data type as well. In fact, any prime number less than 2^30 will be fine in order to prevent possible overflows.

-> 1,000,000,009 (✅ Prime)
1,000,000,033 (✅ Prime)
1,000,000,039 (✅ Prime)
1,000,000,051 (✅ Prime)
1,000,000,061 (✅ Prime)

-> 10 ^9+9=1,000,000,009 is also a frequently used prime in modular computations.

-> https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
