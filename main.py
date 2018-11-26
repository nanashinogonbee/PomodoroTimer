from time import sleep


def pomodoro_start(mins, secs, number):
    while True:
        time_str = f'{mins}:{secs}'
        if mins < 10:
            if secs < 10:
                print(f'0{mins}:0{secs}', end='')
            elif secs >= 10:
                print(f'0{mins}:{secs}', end='')
        elif secs < 10 and mins >= 10:
            print(f'{mins}:0{secs}', end='')
        else:
            print(f'{mins}:{secs}', end='')
        print('\b' * (len(time_str) + 2), end='', flush=True)
        if secs == 0:
            mins -= 1
        if secs == 0:
            secs = 60
        sleep(1)
        secs -= 1
        if mins == 0 and secs == 0:
            return number + 1


phs = [
        {
            'phase': 'work',
            'm': 25,
            's': 0,
        },
        {
            'phase': 'short break',
            'm': 5,
            's': 0,
        },
        {
            'phase': 'work',
            'm': 25,
            's': 0,
        },
        {
            'phase': 'long break',
            'm': 15,
            's': 0,
        },
        ]
n = 0
while True:
    input(f'''Press Enter to start a {phs[n]["m"]}-minute {phs[n]["phase"]}.
Press Ctrl+C to quit.''')
    n = pomodoro_start(phs[n]['m'], phs[n]['s'], n) % 4

