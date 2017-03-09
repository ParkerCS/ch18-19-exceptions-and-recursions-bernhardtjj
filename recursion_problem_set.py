"""
- Personal investment
Create a single recursive function (or more if you wish), which can answer the first three questions below.
For each question, make an appropriate call to the function. (5pts each)
"""


def recursive_solve(depth, money, monthly_payment):
    if money > 0:
        if depth:
            money *= 1 + 0.2 / 12
        if depth > 1:
            return recursive_solve(depth - 1, money - monthly_payment, monthly_payment)
        else:
            return money
    else:
        return depth


# 1.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY, so MPR is APR/12).
# Assuming you make no payments for 6 months, what is your new balance?  Solve recursively.
print(recursive_solve(6, 10000, 0))

# 2.  You have $5000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).
# You make the minimum payment of $100 per month for 36 months.  What is your new balance?  Solve recursively.
print(recursive_solve(36, 5000, 100))
# 3.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).
# If you make the minimum payment of $100 per month, how many months will it take to pay it off?  Solve recursively.
exceeding = 110  # Try any number above 109 that doesn't exceed recursion depth

print("Months:", exceeding - recursive_solve(exceeding, 5000, 100))


# 4  Pyramid of Cubes - (10pts) If you stack boxes in a pyramid, the top row would have 1 box,
# the second row would have two, the third row would have 3 and so on.  Make a recursive function
# which calculates the TOTAL NUMBER OF BOXES for a pyramid of boxes n high.  For instance, a
# pyramid that is 3 high would have a total of 6 boxes.  A pyramid 4 high would have 10.

def pyramid(n_high, boxes=0):
    boxes += n_high
    if n_high > 0:
        return pyramid(n_high - 1, boxes)
    else:
        return boxes


for i in range(10):
    print("pyramid", i, "high:", pyramid(i), "boxes")


# ___________________________
# (            __             )
# (          __\_\_           )
# (        __\_\_\_\_         )
# (      __\_\_\_\_\_\_       )
# (    __\_\_\_\_\_\_\_\_     )
# (    \_\_\_\_\_\_\_\_\_\    )
# (                           )
#  ---------------------------
#   O                                  ,+*^^*+___+++_
#    O                           ,*^^^^              )
#     o                       _+*                     ^**+_
#      o                    +^       _ _++*+_+++_,         )
#               _+^^*+_    (     ,+*^ ^          \+_        )
#              {       )  (    ,(    ,_+--+--,      ^)      ^\
#             { (@)    } f   ,(  ,+-^ __*_*_  ^^\_   ^\       )
#            {:;-/    (_+*-+^^^^^+*+*<_ _++_)_    )    )      /
#           ( /  (    (        ,___    ^*+_+* )   <    <      \
#            U _/     )    *--<  ) ^\-----++__)   )    )       )
#             (      )  _(^)^^))  )  )\^^^^^))^*+/    /       /
#           (      /  (_))_^)) )  )  ))^^^^^))^^^)__/     +^^
#          (     ,/    (^))^))  )  ) ))^^^^^^^))^^)       _)
#           *+__+*       (_))^)  ) ) ))^^^^^^))^^^^^)____*^
#           \             \_)^)_)) ))^^^^^^^^^^))^^^^)
#            (_             ^\__^^^^^^^^^^^^))^^^^^^^)
#              ^\___            ^\__^^^^^^))^^^^^^^^)\\
#                   ^^^^^\uuu/^^\uuu/^^^^\^\^\^\^\^\^\^\
#                      ___) >____) >___   ^\_\_\_\_\_\_\)
#                     ^^^//\\_^^//\\_^       ^(\_\_\_\)
#                       ^^^ ^^ ^^^ ^
