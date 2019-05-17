from random import choice as rchoice
# avoid importing whole modules if you only need a function
# numpy.random is much faster (2-3 times) but numpy is not in stdlib
# (although pretty much everybody has numpy, so make a decision)

BASE = {
    16: "0123456789abcdef"
}

# You could also set a simple environment variable string:
# BASE_16 = "0123456789abcdef"
# but if you use more than a few bases I suggest you set up a dictionary

def id_gen(length, base = BASE[16]):
    # """You can add a function description here to be accessed by help()"""
    # (remove the #)

    # if it is a simple problem, you can probably do it in a short list comprehension
    # it is even more readable (sometimes):

    # key is a string made of random choices from a base repeated length times
    key = ''.join([rchoice(base) for i in range(length)])

    # numpy.random counterpart for this method:
    # ''.join(numpy.random.choice(list(base), length))

    # if you decide to use numpy you can avoid creating the lists here
    # by defining the base as a list before the calling the function
    # (i.e. in the environment variables)
    # (useful if you have to repeat this many times over)

    # the method you had before is a bit inhumane:

    # key is a string made of a random selections between zero and
    # the length of elements from a base repeated length times
    # key = ''.join([base[random.randint(0, length(base))] for i in range(length)])

    return key