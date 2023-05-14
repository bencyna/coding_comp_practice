# n = number of out circles and r is the radius of the inner cricle 

# with above, calcultae the radius' of the outer circles so that
# all outer circles touch the inner circle and all outer circles touch 2 other circles

# return the radius of the outer circles

# circumfernece 2 pi r 

# total circumference required by outer circles 

# outer circle radious is r(i) + r(o)

# we can get the circumference of the outer circle for any r we choose

# we can also  

# if 6 circles, the radius is the same as the inner
import math
numberOfCicles, radiusOfInner = list(map(int, input().strip().split()))

circumferenceOfInner = math.pi * 2 * radiusOfInner

# total cirumference of outer == numOfCircles / (2 * math.pi * ( radiusOfInner + r(o) ))
# r(o) = C(o)/2*pi - radiusOfInner

# select random radius, and see if the circumference 

# we know how many outer circles there are

r(o) : r(i), n