


def func(l):
    # iterate throught the list

    # keep track and update the highest repetition number -- 
    # let's call it: max_len ; set it as 0 for now

    # when a char repeats itself more than max_len times --
    # -- remember it as max_char

    # return max_char and max_len when done iterating

    rs = {}

    if not l:
        return rs 

    max_len = current_len = 1
    max_char = ''
    prev_char = ''


    for i in range(len(l)):
        if prev_char == l[i]:
            current_len += 1 
            if current_len == max_len:
               rs[l[i]] = max_len
            elif current_len > max_len:
               max_len = current_len
               max_char = l[i]
               rs = {max_char: max_len}

        else:
            current_len = 1

        prev_char = l[i]
    
    return rs  


l = "abcd"
x = func(l)

print(x)