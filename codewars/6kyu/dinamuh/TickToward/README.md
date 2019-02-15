[Tick Toward](https://www.codewars.com/kata/54bd06539f075cece0000feb)

Define a function that generates medial values between two coordinates and returns them in an array from start to target. For example, if the starting point is `[1,1]` and the target point is `[3,2]` then the shortest route from start to target would be `[[1,1], [2,2], [3,2]]`. The route should go only through integral coordinates.

Note: you should move diagonally until the path from your current position to the target can be represented as a fully horizontal/vertical line.
###Examples:

    tick_toward((5,5), (5,7))   ==  [(5,5), (5,6), (5,7)]
    tick_toward((3,2), (4,5))   ==  [(3,2), (4,3), (4,4), (4,5)]
    tick_toward((5,1), (5,-2))  ==  [(5,1), (5,0), (5,-1), (5,-2)]

Note: tuples will be used for representing coordinates in Python.

