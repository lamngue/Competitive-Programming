n = int(input())
i = 0
dic = {
    'clank': 'a',
    'bong': 'b',
    'click': 'c',
    'tap': 'd',
    'poing': 'e',
    'clonk': 'f',
    'clack': 'g',
    'ping': 'h',
    'tip': 'i',
    'cloing': 'j',
    'tic': 'k',
    'cling': 'l',
    'bing': 'm',
    'pong': 'n',
    'clang': 'o',
    'pang': 'p',
    'clong': 'q',
    'tac': 'r',
    'boing': 's',
    'boink': 't',
    'cloink': 'u',
    'rattle': 'v',
    'clock': 'w',
    'toc': 'x',
    'clink': 'y',
    'tuc': 'z'
    }
out = ''
shiftDown = True
capsDown = True
spaceBar = ' '
while i < n:
    sound = input()
    if sound not in ['whack', 'bump', 'pop', 'dink', 'thumb']:
        if shiftDown and capsDown:
            out += dic[sound]
        elif not shiftDown and not capsDown: #caps up but shift also up
            out += dic[sound]
        elif shiftDown and not capsDown: #caps up but shift down
            out += dic[sound].upper()
        elif not shiftDown and capsDown: #caps down but shift up
            out += dic[sound].upper()
    else:
        if sound == 'whack':
            out += ' '
        elif sound == 'bump':
            capsDown = not capsDown
        elif sound == 'pop':
            out = out[:-1]
        elif sound == 'dink' or sound == 'thumb':
            shiftDown = not shiftDown
    i += 1
print(out)