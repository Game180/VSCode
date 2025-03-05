scores = [5,7,9,11]

# to access items in an array use the following
# notation

DISPLAY scores[0]

# we can do some really cool stuff with arrays!

BEGIN max_in_array(scores)

    max = 0
    item = 0
    WHILE item < LENGTH scores
        IF scores[item] > max THEN
            max = scores[item]
        END IF
        item = item + 1 # increment by 1
    END WHILE

END
max_in_array(scores)