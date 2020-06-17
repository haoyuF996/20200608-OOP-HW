class SMS_store:

    def __init__(self, box=[]):
        self.box = box

    def add_new_arrival(self,from_number, time_arrived, text_of_SMS):
        self.box.append((False,from_number, time_arrived, text_of_SMS))
    

    def message_count(self):
        return len(self.box)

    def get_unread_indexes(self):
        unread = []
        for i,v in enumerate(self.box):
            if not v[0]:
                unread.append(i)
        return unread

    def get_message(self,i):
        if i < len(self.box):
            return self.box[i][1:]
        else:
            return None

    def delete(self,i):
        if i < len(self.box)-1:
            self.box = self.box[:i]+self.box[i+1:]
        elif i == len(self.box)-1:
            self.box = self.box[:i]
        else:
            pass
    
    def clear(self):
        self.box = []

import datetime

my_inbox = SMS_store()

for i in range(114,514):
    my_inbox.add_new_arrival(1919810+i,datetime.time(int(i/25),int(i/10),19,19),chr(int((i+810)/50)))

print(my_inbox.message_count())

print(my_inbox.get_unread_indexes())

print(my_inbox.get_message(114))

my_inbox.delete(51)
my_inbox.clear()