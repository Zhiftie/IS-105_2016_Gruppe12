'''
This includes all the arts for the boat project.
'''

class Art :
    def __init__(self):
        self.art_a = {       # Everything that include position A
            'a_with_items_person': "     A \n           O\\\n          /|\\\n  ^^-@-^^^/-\+`\_______/`",
            'a_with_items_noPerson': "     A\n\n  ^^-@-^^^---`\_______/`"
        }
        self.art_b = {       # Everything that include position A
            'b_with_items_person_noItems': "     B \n           O\\\n          /|\\\n  ^^-_-^^^/-\+`\_______/`",
            'b_with_items_person': "     B \n           O\\\n          /|\\\n  ^^-@-^^^/-\+`\_______/`",
        }

        self.art_boat = {    # everything that includes boat
            'a_boat_empty' : " `\_______/`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`",
            'a_boat_noPerson_item' : " `\____@__/`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`",
            'a_boat_onlyman_left' : "      O\n     /|\\\n  `\_/_\__/`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`",
            'b_boat_onlyman_right' : "                                             O\n                                            /|\\\n  `~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`\_/_\__/`",
            'a_boat_items_left' : "    O\n   /|\\\n `\/_\_@_/`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`",
            'a_boat_items_right' : "                                            O\n                                           /|\\\n  `~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`\/_\_@_/`",
            
            
            'a_boat_all_left' : "            O\n           /|\\\n     *     /-\`\_______/`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`",
            'a_boat_all_right' : "                                                      O\n                                                     /|\\\n  `~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`\_______/` /-\ *     ",
              
        }


if __name__ == '__main__':
    art = Art()
    print art.art_a['a_with_items_person']
    print art.art_boat['a_boat_empty']
    print art.art_boat['a_boat_all_left']
    print art.art_boat['a_boat_all_right']
    print art.art_boat['a_boat_onlyman_right']
    print art.art_boat['a_boat_onlyman_left']
    print art.art_boat['a_boat_items_left']
    print art.art_boat['a_boat_items_right']