is_magician=False
is_expert=True

if is_magician and is_expert:
    print('You are a master magician')
elif is_magician or is_expert:
    print('atleast you are getting there.')
elif not is_magician:
    print('you need magic powers')