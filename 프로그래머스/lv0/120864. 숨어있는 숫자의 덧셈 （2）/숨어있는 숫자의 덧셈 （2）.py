def solution(my_string):
    for i in my_string:
        if not i.isdigit():
            my_string = my_string.replace(i,' ')
    my_string = my_string.split(' ')
    return sum(int(i)for i in my_string if not i=='')