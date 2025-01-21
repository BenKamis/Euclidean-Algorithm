# Euclidean-Algorithm
Comparing the number of iterations the Euclidean Algorithm takes to find the GCD of two numbers and the GCD of those two numbers.

The Euclidean Algorithm is a method of finding the greatest common divisor of two integers. See here: https://en.wikipedia.org/wiki/Euclidean_algorithm
The procedure is as follows:
1) Start with integers a and b
2) Divide a and b with remainder, such that a = qb + r.
3) Replace a with b. Replace b with r.
4) Repeat process until r = 0
5) The GCD of a and b is the last non-zero remainder.

GCD Graph:
When the size of dots is proportional to the GCD, there are clear patterns emerging when a = (p/q)b, where p/q is a ratio of integers and p, q << a, b. For example, a = b is a clear line of large dots, as well as a = b/2, a = 2b/3, a = b/4, and a = 3b/4.
There are also white vertical and horizontal lines where a or b are prime: The GCD in these cases is always 1, so the dots are very small and white lines emerge.

Steps Graph:
The larger points in the GCD graph correspond to small points in the steps graph, which makes sense: When the algorithm terminates quickly, the algorithm undergoes fewer iterations and the divisors are relatively large compared to a and/or b.

When the graphs are overlain, denser regions in each graph fill less dense regions in the other.

In the GCD Graph: I am unsure of why a line of slightly larger dots emerges around b = -a + (upper bound).
