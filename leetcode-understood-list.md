`1)  3304. Find the K-th Character in String Game I `


`2) 2550. Count Collisions of Monkeys on a Polygon`

-> return (int) ((max + pow(n) - 2) % max);   
-> Adding max before taking % max ensures that the result remains non-negative;\n
-> 10^9+7 is a prime number, making it useful for modular arithmetic;\n
-> Integer.MAX_VALUE is larger (~2.1×10^9) than 1000000007;\n
-> 10^9+7 fulfills both the criteria. It is the first 10-digit prime number and fits in int data type as well. In fact, any prime number less than 2^30 will be fine in order to prevent possible overflows.\n
