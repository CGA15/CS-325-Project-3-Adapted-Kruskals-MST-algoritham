# CS-325-Project-3-Adapted-Kruskals-MST-algoritham

Project Prompt:

The art exhibition organizers again!! Yes, after the successful exhibitions in Corvallis, they are
trying to organize a tour of shows now. They plan to visit n towns t1, t2, . . . , tn in this tour. They
want to start the tour from t1 and end it at t1. They have a small problem though. With the
very expensive art pieces in their truck they do not want to stop in between the towns to fill their
gas tank. In other words, they want to refill their tanks only when they are in a town. But, they
are fine taking paths that are not necessarily the shortest. For example, when going from t1 to t2,
they allow themselves to pass through other towns if needed. In order to make this trip possible
they are ready to change the tank of their trunk to have a larger capacity. But, they want to know
the smallest possible capacity with which this trip is possible. They took the time to calculate the
required gas to drive between any pair of towns. Now, they are asking us to design an algorithm
that calculates the minimum required tank capacity to finish the tour from these numbers.

Formally, they give us the number of towns, n, and the gas they need to drive between any pair
of them, gi,j for all 1 ≤i < j ≤n whenever there is a direct road between ti and tj . In the output,
they just ask for one number, the minimum capacity of the tank that allows completing the tour.
Consider the examples in the following figure. The left side one is an example with three towns, in
which the answer is 4; the optimal tour is t1 →t3 →t1 →t2 →t1. The right side one is an example
with four towns, in which the answer is 4; the optimal tour is t1 →t2 →t3 →t2 →t4 →t2 →t1.
1

![image](https://user-images.githubusercontent.com/91294372/217661831-812aaff8-9dbc-47b0-80cc-961aa6860e79.png)


•Design an algorithm to compute the minimum required capacity of the tank, for a problem
with n towns and m roads. Any algorithm with polynomial time in n and m receives the
full credit for the report part. For the implementation, we try to build test cases so that any
algorithm with O(m log n) time (with a reasonable hidden constant factor) can pass them.

•Prove that your algorithm is correct, and analyze its running time.
