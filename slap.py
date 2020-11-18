from __future__ import print_function
from random import choice
import hexchat

__module_name__ = 'Slap International'
__module_version__ = '2.1'
__module_description__ = 'Slaps specified users'
__author__ = 'Douglas Brunal (AKA) Frankity [internationalized by socraticDev(2020)]'

slaps = [
    'slaps {} around a bit with a large trout',
    'gives {} a clout round the head with a fresh copy of HexChat',
    'slaps {} with a large smelly trout',
    'breaks out the slapping rod and looks sternly at {}',
    'slaps {}\'s bottom and grins cheekily',
    'slaps {} a few times',
    'slaps {} and starts getting carried away',
    'would slap {}, but is not being violent today',
    'gives {} a hearty slap',
    'finds the closest large object and gives {} a slap with it',
    'likes slapping people and randomly picks {} to slap',
    'dusts off a kitchen towel and slaps it at {}',
    'gives 2 or 3 slaps to {} with a dead squirrel found on the sidewalk',
]

# /love {nickname}
loves = [
    'smiles warmly at {}',
    'gives a grandiose hug to {}',
    'kisses {}'
]

# /slapfr {nickname}
slaps_fr = [
    'prends un élan et gifle {}',
    'frappe {} avec une grosse truite humide'
]

# /lovefr {nickname}
loves_fr = [
    'donne un gros câlin à {}',
    'couvre {} de bisoux'
]

# /slaplu {nickname}
slaps_lu = [
    'schléit {} mat enger grousser Frell'
]

sentences = {
    'slap': slaps,
    'slapfr': slaps_fr,
    'slaplu': slaps_lu,
    'love': loves,
    'lovefr': loves_fr
}    

def fct_cb(word, word_eol, userdata):
    if len(word) > 1:
        nick = word[1]
        try:
            slaps_arr = sentences[word[0]]
        except:
            slaps_arr = ['command is no good' + word[0]]

        hexchat.command('me ' + choice(slaps_arr).format(nick))
    else:
        hexchat.command('help slap')
    return hexchat.EAT_ALL

def unload_cb(userdata):
    print(__module_name__, 'version', __module_version__, 'unloaded.')

hexchat.hook_command('slap', fct_cb, help='SLAP <nick>')
hexchat.hook_command('slapfr', fct_cb, help='SLAPFR <nick>')
hexchat.hook_command('slaplu', fct_cb, help='SLAPLU <nick>')
hexchat.hook_command('love', fct_cb, help='LOVE <nick>')
hexchat.hook_command('lovefr', fct_cb, help='LOVEEFR <nick>')
print(__module_name__, 'version', __module_version__, 'loaded.')
