Time Loop Logic
===============
From http://en.wikipedia.org/wiki/Novikov_self-consistency_principle#Time_loop_logic

If N is 0 or 1, abort.
Allocate a communication channel c.
Receive one prime factor, F, of N from the future on channel c.
Test that F ≠ N, that F divides N (time complexity O(log N)), and that F is prime (polynomial time; see AKS primality test).
If so, send F backwards in time on channel c.
If not, send F + 1 backwards in time on channel c. Note that this results in a paradox, as the number received in step 3 above is not the same as that sent in this step.
