shopping_list = ['shoes','shirt']


def shopping():
    print shopping_list
    user_item= raw_input("what's next on your list?")
    if user_item in shopping_list:
        print 'Already in list.'
    else:

        shopping_list.append(user_item)
        print shopping_list

    # shopping.extend


shopping()
