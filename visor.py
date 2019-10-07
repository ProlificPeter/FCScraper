# visor.py -  - PRL Granlund - (c) RL Dimensions
# October 6, 2019
# v0.9
# Class designed to be an easier object to manage reading the scraped objects and provide additional
# functionality (Star Trek Reference)

class Visor:

    def __init__(self):
        self.initialText = ""
        # Need to decide how to augment this

    def find_intermediate_chars(self, text, sub1, sub2):
        pos1 = text.lower().find(sub1) + len(sub1)
        pos2 = text.lower().find(sub2)
        if pos1 > pos2 and pos2 > 0:
            return text[pos1:pos2]
        elif pos2 > pos1 and pos1 > 0:
            return text[pos2:pos1]
        elif pos1 > 0:
            return text[pos1:]
        elif pos2 > 0:
            return text[pos2:]