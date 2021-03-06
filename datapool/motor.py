import data
import function as fc

init_content = [
    ['Direction', '+'],
    ['Steps', 0],
    ['Position', 0],
    ['Status', 'Stop']
]

motorCmdDict = {
    'motor': '\x00\x02',
    'move': '\x00',
    'set_origin': '\x00',
    'auto_forward': '\x01',
    'auto_backward': '\x02',
    'step_forward': '\x03',
    'step_backward': '\x04',
    'originate': '\x05',

    'Tstop': '\x01',
    'stop': '\x00',
}

class motor_data(data.moduletype):
    def __init__(self, name, cmddicts):
        data.moduletype.__init__(self, name, cmddicts)
        self.display_content = init_content

    def work_cmd(self, cmd):
        if len(cmd) != 10:
            raise ValueError("The lenth of the data is incorrect")

        cmd = fc.CMDclean(cmd)

        direction = int((cmd[4:6]).encode('hex'), 16)
        steps = int((cmd[6:8]).encode('hex'), 16)
        motorsta = int((cmd[8:10]).encode('hex'), 16)

        if direction == 1:
            self.display_content[0][1] = '+'
            self.display_content[2][1] += steps
        else:
            self.display_content[0][1] = '-'
            self.display_content[2][1] -= steps

        self.display_content[1][1] = steps

        if motorsta == 1:
            self.display_content[3][1] = 'Moving'
        elif motorsta == 0:
            self.display_content[3][1] = 'Stopping'
        self.is_newcontent = True

config_dict = {
    'motor':{
        'head':motorCmdDict['motor'],
        'name':'motor',
        'data':motor_data('motor', motorCmdDict),
    }
}
