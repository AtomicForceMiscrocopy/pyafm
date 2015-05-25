__author__ = 'yingxu'
# coding=utf-8

import curses
# from motor import motorCmdDict
# from pid import pidCmdDict
status = "stop"
origin = 0
screen = curses.initscr()
screen.keypad(1)
dims = screen.getmaxyx()


def menu():
    screen.nodelay(0)
    screen.clear()
    selection = -1
    option = 0
    while selection < 3:
        graphics = [0] * 4
        graphics[option] = curses.A_REVERSE
        screen.addstr(dims[0] / 2, dims[1] / 2, ' ')
        screen.addstr(dims[0] / 2 + 1, dims[1] / 2 - 2, 'AFM')
        screen.addstr(dims[0] / 2 + 2, dims[1] / 2 - 2, 'motor', graphics[0])
        screen.addstr(dims[0] / 2 + 3, dims[1] / 2 - 2, 'PID', graphics[1])
        screen.addstr(dims[0] / 2 + 4, dims[1] / 2 - 6, 'Instructions', graphics[2])
        screen.addstr(dims[0] / 2 + 5, dims[1] / 2 - 2, 'Exit', graphics[3])
        screen.refresh()
        action = screen.getch()

        if action == curses.KEY_UP:
            option = (option - 1) % 4
        elif action == curses.KEY_DOWN:
            option = (option + 1) % 4
        elif action == ord('\n'):
            selection = option

        if selection == 0:
            motor()
        elif selection == 1:
            pid()
        elif selection == 2:
            instructions()

        if selection < 4:
            selection = -1


def instructions():
    screen.clear()
    screen.nodelay(0)
    toplines = ['AFM Display']
    centerlines = ['Use the software to control the AFM',
                   'including the message of PID and motor',
                   'Contact the developer',
                   'for any questions']
    bottomlines = ['press Any Key', 'to go back to menu']

    for x in range(len(toplines)):
        screen.addstr(x, (dims[1] - len(toplines[x])) / 2, toplines[x])
    for z in range(len(centerlines)):
        screen.addstr((dims[0] - len(centerlines)) / 2+z, (dims[1] - len(centerlines[z])) / 2
                      , centerlines[z])
    for r in range(len(bottomlines)):
        screen.addstr(dims[0] + r - len(bottomlines), (dims[1] - len(bottomlines[r])) / 2, bottomlines[r])

    screen.refresh()
    screen.getch()
    menu()


def motor():
    global origin, auto, sets, status
    screen.clear()
    selection = -1
    option = 0
    while selection < 8:
        screen.clear()
        graphics = [0] * 9
        graphics[option] = curses.A_REVERSE
        strings = ["Set_Origin:{0}".format(str(origin)),
                   "auto_forward:{0}".format(str(auto)),
                   "auto_backward:{0}".format(str(auto)),
                   "set_forward:{0}".format(str(sets)),
                   "set_backward:{0}".format(str(sets)),
                   "motor_status:" + status,
                   "originate",
                   "Tstop",
                   "exit"]
        for z in range(len(strings)):
            screen.addstr((dims[0] / 2 - len(strings)) / 2 + z, (dims[1] - len(strings(z))) / 2, strings(z))
        screen.refresh()
        action = screen.getch()
        if action == curses.KEY_UP:
            option = (option - 1) % 9
        elif action == curses.KEY_DOWN:
            option = (option + 1) % 9
        elif action == ord('\n'):
            selection = option

        if selection == 0:
            origin = screen.getch()
        elif selection == [1, 2]:
            auto = screen.getch()
        elif selection == [3, 4]:
            sets = screen.getch()
        elif selection == 5:
            if status == 'move':
                status = 'stop'
            elif status == 'stop':
                status = 'move'
        # elif selection == 6:
        # elif selection == 7:
        if selection < 8:
            selection = -1
    menu()


def pid():
    global status, p, i, d, sets
    screen.clear()
    selection = -1
    option = 0
    while selection < 5:
        screen.clear()
        graphics = [0] * 6
        graphics[option] = curses.A_REVERSE
        strings = ["pid_status:" + status,
                   "set_p:{0}".format(str(p)),
                   "set_I:{0}".format(str(i)),
                   "set_D:{0}".format(str(d)),
                   "set_point:{0}".format(str(sets)),
                   "exit"]
        for z in range(len(strings)):
            screen.addstr((dims[0] / 2 - len(strings)) / 2 + z, (dims[1] / 2 - len(strings(z))) / 2, strings(z))
        screen.refresh()
        action = screen.getch()
        if action == curses.KEY_UP:
            option = (option - 1) % 6
        if action == curses.KEY_DOWN:
            option = (option + 1) % 6
        if action == ord('\n'):
            selection = option

        if selection == 0:
            if status == 'run':
                status = 'stop'
            elif status == 'stop':
                status = 'run'
        elif selection == 1:
            p = screen.getch()
        elif selection == 2:
            i = screen.getch()
        elif selection == 3:
            d = screen.getch()
        elif selection == 4:
            sets = screen.getch()

        if selection < 5:
            selection = -1

    menu()

if __name__ == "__main__":
    menu()