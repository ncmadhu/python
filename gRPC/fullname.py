import fullname_pb2

def set_name(firstname, lastname):
    
    fullname = fullname_pb2.Fullname()
    fullname.firstname = firstname
    fullname.lastname = lastname
    data = fullname.SerializeToString()
    return data

def get_name(data):

    fullname = fullname_pb2.Fullname()
    fullname.ParseFromString(data)
    firstname = fullname.firstname
    lastname = fullname.lastname
    print("Full Name: %s %s" % (firstname, lastname))


if __name__ == "__main__":
    
    data = set_name("Madhu", "Chakravarthy")
    get_name(data)
