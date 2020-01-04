from wiki_rnd import rndPage

greeting = "Hi user! Choose a way i could help you"
print(greeting + "\n" + "="*38)

option = {
    1: 'find random wikipedia article',
    2: 'product search on the website',
}
keys = list(option.keys())

for key in option:
    print(key, '->', option[key])

while True:
    input_ = input(": ")
    if input_ == str(keys[0]):
        rndPage()
    elif input_ == str(keys[1]):
        break
        #TODO: website search method here
    else:
        break
