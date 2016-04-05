import tape as t
import Art


class State:
    def __init__(self):
        self.tape = t.Database()  # create new tape for the boat project
        self.art = Art.Art()  # create an art object, to show us some graphics
        # self.tape.set_chicken('boat')
        # self.tape.set_man('right')

    def show_state(self):
        t = self.tape

        # if the man is at left, and at least 1 item are at left as well. And boat do not include any items
        if self.tape.man in 'left' and 'left' in (t.fox, t.corn, t.chicken) and 'boat' not in (
                    t.fox, t.corn, t.chicken):
            print self.art.art_boat['a_boat_all_left']

        # man left and boat has one item
        elif self.tape.man in 'left' and 'boat' in (t.fox, t.corn, t.chicken):
            print self.art.art_boat['a_boat_noPerson_item']

        # man in boat, and boat left, and 1 item inside the boat
        elif self.tape.man in 'boat' and 'boat' in (t.fox, t.corn, t.chicken) and 'left' in t.boat:
            print self.art.art_boat['a_boat_items_left']

        # man in boat, 1 item inside the boat, and the boat is right
        elif self.tape.man in 'boat' and 'boat' in (t.fox, t.corn, t.chicken) and 'right' in t.boat:
            print self.art.art_boat['a_boat_items_right']

        # man right and atleast one item right and boat has no items
        elif self.tape.man in 'right' and 'right' in (t.fox, t.corn, t.chicken) and 'boat' not in (
                    t.fox, t.corn, t.chicken):
            print self.art.art_boat['a_boat_all_right']

        # man right, and boat has one item and the right has no items
        elif self.tape.man in 'right' and 'boat' in (t.fox, t.corn, t.chicken) and 'right' not in ((t.fox, t.corn, t.chicken)):
            print self.art.art_b['b_with_items_person_noItems']

        # man right and boat has one item and right has atleast one item
        elif self.tape.man in 'right' and 'boat' in (t.fox, t.corn, t.chicken) and 'right' in ((t.fox, t.corn, t.chicken)):
            print self.art.art_b['b_with_items_person']

        # only man in boat and he is right, no items
        elif self.tape.man in 'boat' and 'right' in t.boat:
            print self.art.art_boat['b_boat_onlyman_right']

        # only man in boat and he is left, no items
        elif self.tape.man in 'boat' and 'left' in t.boat:
            print self.art.art_boat['a_boat_onlyman_left']

    def check_state(self):  # if everything is left, as it would in the start of the game.
        self.show_state()

        if self.check_lose_combo():                     # if the player left chicken and corn alone or fox and chicken
            print("player is dead")                     # print art to the player NB: not created art for it yet.
            return True                                 # break the state check

        if self.man_no_items_boat(): return None
        if self.man_in_boat(): return None              # if man is inside the boat options is delivered
        self.man_on_left()                              # if the man is at left, give options
        self.man_on_right()                             # if the man is at right, give options.

    def check_lose_combo(self):
        '''
        This will check if the current state will lead to the player to lose
        :return: True if the player is 'dead' | False if the user is not 'dead'
        '''

        # where either chicken and corn is left alone, or fox and chicken is left alone.
        if (self.tape.chicken in self.tape.fox) and (self.tape.man not in self.tape.chicken) or \
                        (self.tape.chicken in self.tape.corn) and (self.tape.man not in self.tape.chicken):
            return True                                 # return True if the player has lost the game
        return False                                    # return False if the player has not lost the game.

    def man_in_boat(self):
        if self.tape.man in 'boat':
            answer = raw_input("Do you want to go outside of the boat? or do you want to travel?: type 1, to go out "
                               "type 2 to travel: ")
            if self.tape.boat in 'left':
                if answer == '1':
                    self.tape.set_man('left')
                else:
                    self.tape.set_boat('right')
            elif self.tape.boat in 'right':
                if answer == '1':
                    self.tape.set_man('right')
                else:
                    self.tape.set_boat('left')
            return True
        return False

    def man_on_left(self):

        if self.tape.man in 'left':
            # Check if there is any items inside the boat
            if self.items_on_boat() is self.tape.chicken:
                self.man_left_item_boat(self.tape.chicken)
            elif self.items_on_boat() is self.tape.corn:
                self.man_left_item_boat(self.tape.corn)
            elif self.items_on_boat() is self.tape.fox:
                self.man_left_item_boat(self.tape.fox)
            else:
                pass  # no items inside the boat.

    def man_on_right(self):
        if self.tape.man in 'right':

            # Check if there is any items inside the boat
            if self.items_on_boat() is self.tape.chicken:
                self.man_right_item_boat(self.tape.chicken)
            elif self.items_on_boat() is self.tape.corn:
                self.man_right_item_boat(self.tape.corn)
            elif self.items_on_boat() is self.tape.fox:
                self.man_right_item_boat(self.tape.fox)
            else:
                pass  # no items inside the boat.

    def items_on_boat(self):
        '''
        Check if there is any items on the boat
        :return: the veriable of the item,
        with this veriable we can use 'is' to check witch veriable it is.
        '''
        if 'boat' in (self.tape.chicken, self.tape.fox, self.tape.corn):
            if 'boat' in self.tape.chicken:
                return self.tape.chicken

            elif 'boat' in self.tape.corn:
                return self.tape.corn

            elif 'boat' in self.tape.fox:
                return self.tape.fox
        else:
            return None

    def man_left_item_boat(self, item):
        '''
        If the man is at left, and there is items inside the boat, give the user the ability to take the item out
        or go inside the bout himself.
        :param item: the item that are inside the bout, the veriable(!)

        Also, he will write the new command that user has given the the program.
        '''
        take_out_boat = self.man_answer_items_boat_left_right(item)  # give the user ability to choose what he wants
        if take_out_boat == 1:
            self.tape.set_chicken('left')
        elif take_out_boat == 2:
            self.tape.set_corn('left')
        elif take_out_boat == 3:
            self.tape.set_fox('left')
        elif take_out_boat == 4:
            self.tape.set_man('boat')

        print take_out_boat

    def man_right_item_boat(self, item):
        '''
        If the man is at right, and there is items inside the boat, give the user the ability to take the item out
        or go inside the bout himself.
        :param item: the item that are inside the bout, the veriable(!)

        Also, he will write the new command that user has given the the program.

        '''
        take_out_boat = self.man_answer_items_boat_left_right(item)  # give the user ability to choose what he wants
        if take_out_boat == 1:
            self.tape.set_chicken('right')
        elif take_out_boat == 2:
            self.tape.set_corn('right')
        elif take_out_boat == 3:
            self.tape.set_fox('right')
        elif take_out_boat == 4:
            self.tape.set_man('boat')

    def man_answer_items_boat_left_right(self, item):
        '''
        This is a universal function for either left side or right side. This is the underfucntion to man_left_item_boat
        and man_right_item_boat.

        This will hold the veribale that is inside the boat, and check if the veriable 'is' some of the veriables on the
        tape. and will ask the user for his next move based on his current state.

        :param item: the veriable that is inside the boat.
        :return: return the answer, for what the user wants to do. Return None, if the user was not able to answer any
        of the given question. if the program return null, it would be a bug. :-(
        '''
        take_out_boat = None

        if item is self.tape.chicken:
            answer = raw_input("Do you want to take the chicken out of the boat? Y/N : ")
            answer = self.redefine_answer(answer)
            if answer: take_out_boat = 1
        elif item is self.tape.corn:
            answer = raw_input("Do you want to take the corn out of the boat? Y/N : ")
            answer = self.redefine_answer(answer)
            if answer: take_out_boat = 2
        elif item is self.tape.fox:
            answer = raw_input("Do you want to take the fox out of the boat? Y/N : ")
            answer = self.redefine_answer(answer)
            if answer: take_out_boat = 3

        # if the user has answered no on the previous question
        if take_out_boat is None:
            answer = raw_input("Do you want to go inside the boat? Y/N : ")
            answer = self.redefine_answer(answer)
            if answer: take_out_boat = 4
        return take_out_boat

    def man_no_items_boat(self):
        '''
        if the man is at left, and no items inside the boat. The man is then allowed to pick one item to inside
        his boat. Depends on location
        :return:
        '''
        if self.items_on_boat() != None: return None
        if self.tape.man in self.tape.chicken \
                and self.tape.man in self.tape.corn \
                and self.tape.man in self.tape.fox:
            answer = raw_input("Choose one: Go inside the boat type 1. Put chicken inside the boat type 2."
                               "Put corn inside the boat, type 3. Put fox inside the boat type 4: ")

            if answer == '1':
                self.tape.set_man('boat')
            elif answer == '2':
                self.tape.set_chicken('boat')
            elif answer == '3':
                self.tape.set_corn('boat')
            elif answer == '4':
                self.tape.set_fox('boat')
            else:
                pass
            return True

        elif self.tape.man in self.tape.chicken \
                and self.tape.man in self.tape.corn:
            answer = raw_input("Choose one: Go inside the boat type 1. Put chicken inside the boat type 2."
                               "Put corn inside the boat, type 3.")

            if answer == '1':
                self.tape.set_man('boat')
            elif answer == '2':
                self.tape.set_chicken('boat')
            elif answer == '3':
                self.tape.set_corn('boat')
            else:
                pass
            return True


        elif self.tape.man in self.tape.fox \
                and self.tape.man in self.tape.corn:
            answer = raw_input("Choose one: Go inside the boat type 1. Put fox inside the boat type 2."
                               "Put corn inside the boat, type 3.")
            if answer == '1':
                self.tape.set_man('boat')
            elif answer == '2':
                self.tape.set_fox('boat')
            elif answer == '3':
                self.tape.set_corn('boat')
            else:
                pass
            return True

        elif self.tape.man in self.tape.fox \
                and self.tape.man in self.tape.chicken:
            answer = raw_input("Choose one: Go inside the boat type 1. Put fox inside the boat type 2."
                               "Put chicken inside the boat, type 3.")
            if answer == '1':
                self.tape.set_man('boat')
            elif answer == '2':
                self.tape.set_fox('boat')
            elif answer == '3':
                self.tape.set_chicken('boat')
            else:
                pass
            return True

        elif self.tape.man in self.tape.chicken:
            answer = raw_input("Choose one: Go inside the boat type 1. Put chicken inside the boat type 2.")
            if answer == '1':
                self.tape.set_man('boat')
            elif answer == '2':
                self.tape.set_chicken('boat')
            else:
                pass
            return True

        elif self.tape.man in self.tape.fox:
            answer = raw_input("Choose one: Go inside the boat type 1. Put fox inside the boat type 2.")
            if answer == '1':
                self.tape.set_man('boat')
            elif answer == '2':
                self.tape.set_fox('boat')
            else:
                pass
            return True

        elif self.tape.man in self.tape.corn:
            answer = raw_input("Choose one: Go inside the boat type 1. Put corn inside the boat type 2.")
            if answer == '1':
                self.tape.set_man('boat')
            elif answer == '2':
                self.tape.set_corn('boat')
            else:
                pass
            return True

    def redefine_answer(self, answer):
        if answer == 'y':
            answer = True
        else:
            answer = False
        return answer


def test():
    state = State()
    dead = False
    while not dead:
        if state.check_state() is True:
            dead = True


test()