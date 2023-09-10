from tkinter import *

root = Tk()
root.title('ABSI Calculator')
root.resizable(False, False)
# icon = PhotoImage(file='calculator_icon.png')
# root.iconphoto(False, icon)
default_prompt = '                                   Enter an equation'
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
operator = ['(', ')', '+', '-', '*', '/', '^']
equation = []
last_answer = None


def subtraction(n1, n2):
    return n1 - n2


def addition(n1, n2):
    return n2 + n1


def multiplication(n2, n1):
    return n2 * n1


def exponent(n1, n2):
    return n1 ** n2


dict_math = {"^": exponent,
             '*': multiplication,
             }


def string_to_list(string_prompt):
    number_to_be_added = ''
    for index, character in enumerate(string_prompt):
        if character in number:
            number_to_be_added += character
        if character in operator:
            if not number_to_be_added == '':
                equation.append(float(number_to_be_added))
            if character == '(':
                if len(equation) is not 0:
                    if type(equation[-1]) == float or equation[-1] == ')':
                        equation.append("*")
            equation.append(character)
            number_to_be_added = ''
    if not number_to_be_added == '':
        equation.append(float(number_to_be_added))


def correct_equation():
    for index, character in enumerate(equation):
        if character == '-':
            if not index == 0:
                if not type(equation[index - 1]) == float and not equation[index - 1] == ')':
                    if type(equation[index + 1]) == float:
                        equation.pop(index)
                        equation[index] = equation[index] * -1
            else:
                if type(equation[index + 1]) == float:
                    equation.pop(index)
                    equation[index] = equation[index] * -1

        if character == '/':
            if type(equation[index + 1]) == float:
                equation.pop(index)
                equation.insert(index, '*')
                equation[index + 1] = equation[index + 1] ** -1


def solve(given_equation):
    for operation in dict_math:
        check = False
        while not check:
            for index, character in enumerate(given_equation):
                if character == operation:
                    x = round(dict_math[operation](given_equation[index - 1], given_equation[index + 1]), 10)
                    for c in range(0, 3):
                        given_equation.pop(index - 1)
                    given_equation.insert(index - 1, x)
                    check = False
                    break
                else:
                    check = True

    check = False
    while not check:
        for index, character in enumerate(given_equation):
            if character == '+':
                x = round(addition(given_equation[index - 1], given_equation[index + 1]), 10)
                for c in range(0, 3):
                    given_equation.pop(index - 1)
                given_equation.insert(index - 1, x)
                check = False
                break
            if character == '-':
                x = round(subtraction(given_equation[index - 1], given_equation[index + 1]), 10)
                for c in range(0, 3):
                    given_equation.pop(index - 1)
                given_equation.insert(index - 1, x)
                check = False
                break
            else:
                check = True
    return given_equation[0]


def isolate_bracket():
    equation_within_brakcet = []
    left_bracket_index = 0
    right_bracket_index = 0
    list_of_bracket_index = []
    bracket_present_flag = False
    for index, character in enumerate(equation):
        if character == ')':
            right_bracket_index = index
            counter = index - 1
            while not counter < 0:
                if equation[counter] == '(' and counter not in list_of_bracket_index:
                    left_bracket_index = counter
                    list_of_bracket_index.append(counter)
                    bracket_present_flag = True
                    break
                else:
                    counter += - 1
            break
    if right_bracket_index == left_bracket_index + 1:
        raise ""
    if bracket_present_flag:
        for index in range(left_bracket_index + 1, right_bracket_index):
            equation_within_brakcet.append(equation[index])

        for index in range(left_bracket_index, right_bracket_index + 1):
            equation.pop(left_bracket_index)
        equation.insert(left_bracket_index, solve(equation_within_brakcet))
        correct_equation()
        isolate_bracket()
    else:
        solve(equation)
        if len(equation) != 1:
            raise ''


def equation_solver():
    global last_answer
    deleting_prompt()
    global equation
    if not e.get() is '':
        try:
            string_to_list(e.get())
            correct_equation()
            isolate_bracket()
            e.delete(0, END)
            if equation[0].is_integer():
                e.insert(0, int(equation[0]))
                last_answer = int(equation[0])
            else:
                e.insert(0, round(equation[0], 4))
                last_answer = round(equation[0], 4)
        except:
            e.delete(0, END)
            e.insert(0, 'ERROR')
        equation = []


def deleting_prompt():
    global last_answer
    if e.get() == default_prompt or e.get() == 'ERROR' or e.get() == str(last_answer):
        e.delete(0, END)
        last_answer = None


def delete():
    deleting_prompt()
    current_no = e.get()
    current_no = current_no[:len(current_no) - 1]
    e.delete(0, END)
    e.insert(0, current_no)


def enter(no):
    deleting_prompt()
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, current_number + str(no))


x_size = 20
y_size = 15
number_0 = Button(root, text='0', padx=x_size, pady=y_size, command=lambda: enter(0))
number_1 = Button(root, text='1', padx=x_size, pady=y_size, command=lambda: enter(1))
number_2 = Button(root, text='2', padx=x_size, pady=y_size, command=lambda: enter(2))
number_3 = Button(root, text='3', padx=x_size, pady=y_size, command=lambda: enter(3))
number_4 = Button(root, text='4', padx=x_size, pady=y_size, command=lambda: enter(4))
number_5 = Button(root, text='5', padx=x_size, pady=y_size, command=lambda: enter(5))
number_6 = Button(root, text='6', padx=x_size, pady=y_size, command=lambda: enter(6))
number_7 = Button(root, text='7', padx=x_size, pady=y_size, command=lambda: enter(7))
number_8 = Button(root, text='8', padx=x_size, pady=y_size, command=lambda: enter(8))
number_9 = Button(root, text='9', padx=x_size, pady=y_size, command=lambda: enter(9))

exponent = Button(root, text='^', padx=x_size, pady=y_size, command=lambda: enter('^'))
division = Button(root, text='/', padx=x_size, pady=y_size, command=lambda: enter('/'))
multiplication = Button(root, text='*', padx=x_size, pady=y_size, command=lambda: enter('*'))
add = Button(root, text='+', padx=x_size, pady=y_size, command=lambda: enter('+'))
sub = Button(root, text='-', padx=x_size, pady=y_size, command=lambda: enter('-'))

dot = Button(root, text='.', padx=x_size, pady=y_size, command=lambda: enter('.'))

parantheses_left = Button(root, text='(', padx=x_size, pady=y_size, command=lambda: enter('('))
parantheses_right = Button(root, text=')', padx=x_size, pady=y_size, command=lambda: enter(')'))

equals = Button(root, text='=', padx=x_size, pady=y_size, command=equation_solver)

d = Button(root, text='D', padx=x_size, pady=y_size, command=delete)

e = Entry(root, width=50, borderwidth=4)

e.grid(row=0, column=0, columnspan=5, padx=0.5, pady=15)
e.insert(0, default_prompt)
number_7.grid(row=1, column=0)
number_8.grid(row=1, column=1)
number_9.grid(row=1, column=2)
number_4.grid(row=2, column=0)
number_5.grid(row=2, column=1)
number_6.grid(row=2, column=2)
number_1.grid(row=3, column=0)
number_2.grid(row=3, column=1)
number_3.grid(row=3, column=2)
number_0.grid(row=4, column=0)
dot.grid(row=4, column=1)
parantheses_left.grid(row=4, column=2)
parantheses_right.grid(row=4, column=3)
equals.grid(row=4, column=4)
d.grid(row=1, column=3)
multiplication.grid(row=2, column=3)
division.grid(row=2, column=4)
add.grid(row=3, column=3)
sub.grid(row=3, column=4)
exponent.grid(row=1, column=4)

root.mainloop()
