# recursion
Recursion is a way of programming or coding a problem, in which a function calls itself one or more times in its body. Usually, it is returning the return value of this function call.

factorial is O(n) notation as for calculating factorial of n no we will have to move n+1 times in the series and each function have one operation of O(1) so the notation for it is O(n).

English ruler makes us to see that a call to draw_interval(c) for c>0 spans 2 calls to draw_interval(c-1) and single call to draw_line. as we know that to draw_interval(c-1) if c=0 then there would be no output for this and as one center line is printed between two such recursive call; therefore by induction no of lines is thus 2^c-1 = 1+2*(2^(c-1)-1)

binary search is O(log n) os big-Oh notation for a sorted sequence of n elements. every time the mid is taken the range is reduced as 1/2 then 1/4 then 1/8 
                  so then in general n/(2^r) < 1 
                  which implies it to be r = log n + 1 (where log n is a celing value)
                  
Disk space calculation time is O(n)

Amortization--> the idea that we can get a tighter bound on a series of operations by considering the cumulative effect,rather than assuming that each achives the worst case.eg-->file System

