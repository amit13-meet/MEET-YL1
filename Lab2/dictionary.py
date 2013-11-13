dic = {}
def add_obj():
    L1_name = raw_input("Name? ")
    L1_age = raw_input("Hello " + L1_name + ", how old are you? ")
    global dic
    dic[L1_name] = L1_age

add_obj()
add_obj()
add_obj()
print dic
