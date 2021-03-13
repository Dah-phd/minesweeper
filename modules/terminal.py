import scoring as sc
from sys import platform, argv
import subprocess


def score_it(value, LOST):
    link = sc.highscore(
        'modules\\db.res' if platform[:3] == 'win' else 'modules/db.res', high='min'
    )
    if LOST == '0':
        if value != '0':
            print('You have WON!!!')
            print(f'Your time is {value} seconds. Well done!')
            link.name = input('Enter name: ')
        if link.name:
            link.new_score(float(value))
    else:
        print('GAME OVER!')
        print('Good luck with the next game!')
    scores = link.quarry()
    if scores:
        for pos, score in enumerate(scores):
            print(f'{pos} place: {socre[0]} with time {score[1]} seconds')


if __name__ == '__main__':
    score_it(argv[1], argv[2])
    if input('Press any key for new game or q to exit!') != 'q':
        if platform[:3] == 'win':
            cmd = 'modules\\GUI.pyw'
        else:
            cmd = 'python3 ./modules/GUI.pyw'
        subprocess.Popen(cmd, creationflags=subprocess.DETACHED_PROCESS, shell=True,
                         stdin=None, stderr=None, stdout=None, close_fds=True)
