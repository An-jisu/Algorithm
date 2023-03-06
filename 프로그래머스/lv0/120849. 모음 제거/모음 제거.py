def solution(my_string):
    for i in my_string:
        if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            my_string = my_string.replace(i, '')
    return my_string