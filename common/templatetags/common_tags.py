import random
from django import template

from jokes.models import Joke

register = template.Library()

@register.inclusion_tag('common/joke.html')
def random_joke():
    count = Joke.objects.count()
    if count > 0:
        i = random.randint(0, count-1)
        joke = Joke.objects.all()[i]
        return {'joke' : joke}
    else:
        return {"question" : "What is no joke?", 
                "answer": "Our database at the moment."}