from random import shuffle
from random import randint
#(name, immunities, kills, alive/dead)
assassins = [
('Aaron Zou', 2, 1, 1),
('Adin Lee', 1, 0, 1),
('Amy Kim', 2, 0, 1),
('Brandon Lee', 0, 0, 1),
('Bryan Lee', 1, 1, 1),
('Chang Guo', 1, 1, 1),
('Chulsoon Hwang', 1, 1, 1),
('Clara Bae', 1, 1, 1),
('Daniel Sung', 1, 3, 1),
('Danielle Song', 2, 0, 1),
('Dawt Sung', 1, 0, 1),
('Doyoung Jung', 1, 2, 1),
('Elizabeth Oh', 1, 0, 1),
('Eric Kim', 1, 2, 1),
('Erin Lee', 1, 0, 1),
('Esther Ki', 1, 1, 1),
('Esther Ko', 2, 7, 1),
('Grace Kim', 1, 0, 1),
('Grace Oh', 1, 0, 1),
('Grace Yuan', 1, 0, 1),
('Hyunwoo Song', 1, 0, 1),
('Ivy Lee', 0, 2, 1),
('Jamie Yoon', 2, 0, 1),
('Jeffrey Liew', 1, 2, 1),
('Jennifer Kim', 0, 1, 1),
('Jennifer Suriadinata', 2, 0, 1),
('Jenny Lee', 1, 0, 1),
('Jinwon Jang', 1, 0, 1),
('Jisu Kim', 2, 1, 1),
('Joseph Kwon', 1, 0, 1),
('Josh Lee', 1, 4, 1),
('Josh Park', 1, 1, 1),
('Jungwoo Joo', 1, 0, 1),
('Kelvin Mun', 2, 0, 1),
('Kwonwoo Choi', 2, 0, 1),
('Laura Kim', 1, 0, 1),
('Michael He', 1, 3, 1),
('Michaela Kang', 1, 1, 1),
('Nathan Hoang', 1, 1, 1),
('Nick Lee', 1, 5, 1),
('Paul Lee', 1, 1, 1),
('Sam Lee', 1, 0, 1),
('Seoyon Lee', 1, 0, 1),
('Stephanie Choi', 1, 0, 1),
('Sue Jin Park', 1, 0, 1),
('Tae Kim', 2, 3, 1),
('Tae Park', 2, 0, 1),
('Tori Kim', 1, 3, 1),
('Will Kim', 0, 1, 1)
]

live_assassins = []

for assassin in assassins:
    if assassin[3] == 1:
        live_assassins.append(assassin)

def assassin_list():
    return assassins

def live_assassin_list():
    return live_assassins

def takeThird(elem):
    return int((elem[2] + 0.5*elem[3] + 0.2*elem[1])*10)

def revival_chance(elem):
    return 5*elem[2] + elem[1] + 1

def takeSecond(elem):
    return elem[1]
