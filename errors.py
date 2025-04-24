while True:
    try:
        age = int(input('what is your age?: '))
        print(10/age)
        # break
        raise ValueError('hey cut it out')
    # except ValueError:
    #     print('please enter a number')
    except ZeroDivisionError:
        print('Please enter more than 0')
        break
    else:
        print('thank you!')
        break
    finally:
        print('ok, i am finally done')