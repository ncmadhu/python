import first_pb2
name = first_pb2.Name()
name.firstname = "Madhu"
name.lastname = "Chakravarthy"
data = name.SerializeToString()
person = first_pb2.Name()
person.ParseFromString(data)
print("First Name: %s" % person.firstname)
print("Last Name: %s" % person.lastname)
