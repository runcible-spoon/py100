# The following code raises a TypeError:

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)

# What does a TypeError indicate? Try running the above code, 
# then use the resulting error message to determine exactly what is wrong. 
# (You don't have to fix this code.)

# error indicates you can't concatenate a string with an int. 
