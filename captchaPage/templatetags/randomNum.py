from random import randint

from django import template

from random import seed
seed(1)
register = template.Library()
@register.simple_tag
def randNum():
    # length=1
    # """
    # Create a random integer with given length.
    # For a length of 3 it will be between 100 and 999.
    # For a length of 4 it will be between 1000 and 9999.
    # """
    # return randint(10**(length-1), (10**(length)-1))
    
    return randint(0,8)