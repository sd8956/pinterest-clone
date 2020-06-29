from django import template

register = template.Library()

@register.filter
def remainder(posts, board):
    i = 0
    for post in posts:
        if post.board == board:
            i += 1
    
    return i