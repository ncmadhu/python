class Human(object):
    def __setattr__(self,name,value):
        if name == "gender":
            if value in ('male', 'female'):
                self.gender = value
            else:
                raise AttributeError('Gender')

if __name__ == "__main__":

    h = Human()
    h.name = 'mary'
    h.gender = 'female'
    print h.gender

