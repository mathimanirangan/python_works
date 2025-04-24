# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrap_func(*user,**kwargs):
        print('checking whether user has valid')
        print(user[0]['name'])
        if user[0]['valid']:
            fn(*user,**kwargs)
        else:
            print('user is not valid')
    return wrap_func
  # code here

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)