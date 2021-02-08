"""
Mykola Kryvyi
Lab 0.1
Github:
"""
def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.
    """
    file = open(path , 'r')
    contents = file.readlines()
    contents = list(map(lambda x: x.strip(),contents))
    return contents

def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    #my_list = []
    right_pivot = int(input_line[0])
    if pivot > right_pivot:
        right_pivot = pivot
    input_line = list(input_line[1:-1])
    array = [int(i) for i in input_line]
    counter = 1
    for index, elem in enumerate(array):
        check_el = False
        for i in range(index):
            if elem > array[i]:
                check_el = True
            else:
                check_el = False
                break
        if check_el == True:
            counter+=1
            #my_list.append(elem)
    if counter == right_pivot:
        return True
    return False

print(left_to_right_check("132345*", 3))

def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*',\
'4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*',\
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*',\
'423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in board:
        if '?' in i:
            return False
    return True

def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*',\
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*',\
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*',\
'423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    board = board[1:-1]
    for row in board:
        row = list(row[1:-1])
        row = [int(x) for x in row if x!='*']
        if len(row)!=len(set(row)):
            return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*',\
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*',\
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    board = board[1:-1]
    for i in board:
        if i[0]!='*':
            leftright = left_to_right_check(i,0)
            if leftright == False:
                return False
        if i[-1]!='*':
            rightleft = left_to_right_check(i[::-1],0)
            if rightleft == False:
                return False
    return True

def check_columns(board: list):
    """
    Check column-wise compliance of the board for
uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*',\
'*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    count = 0
    array = []
    for _ in board:
        columnline = ''
        for _, elem in enumerate(board):
            columnline = columnline + elem[count]
        array.append(columnline)
        count+=1
    columnscheck = check_horizontal_visibility(array)
    uniquecheck = True
    array_for_check_unique = [i[1:-1] for i in array][1:-1]
    for i in array_for_check_unique:
        lst = list(i)
        lst = [int(i) for i in lst]
        if len(lst)!=len(set(lst)):
            uniquecheck = False
            break
    return uniquecheck and columnscheck

def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """
    array = read_input(input_path)
    final = (check_not_finished_board(array) and check_uniqueness_in_rows(array) and \
check_horizontal_visibility(array) and check_columns(array))
    return final
