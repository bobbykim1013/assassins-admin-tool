from random import shuffle
from random import randint
#(name, immunities, kills, alive/dead)
assassins = [
('Aaron Zou', 2, 1, 0),
('Adin Lee', 1, 0, 0),
('Amy Kim', 2, 0, 0),
('Brandon Lee', 0, 0, 0),
('Bryan Lee', 1, 1, 0),
('Chang Guo', 1, 1, 0),
('Chulsoon Hwang', 1, 1, 0),
('Clara Bae', 1, 1, 0),
('Daniel Sung', 1, 3, 0),
('Danielle Song', 2, 0, 0),
('Dawt Sung', 1, 0, 0),
('Doyoung Jung', 1, 2, 0),
('Elizabeth Oh', 1, 0, 0),
('Eric Kim', 1, 2, 0),
('Erin Lee', 1, 0, 0),
('Esther Ki', 1, 1, 0),
('Esther Ko', 2, 7, 1),
('Grace Kim', 1, 0, 0),
('Grace Oh', 1, 0, 0),
('Grace Yuan', 1, 0, 0),
('Hyunwoo Song', 1, 0, 0),
('Ivy Lee', 0, 2, 0),
('Jamie Yoon', 2, 0, 0),
('Jeffrey Liew', 1, 2, 0),
('Jennifer Kim', 0, 1, 0),
('Jennifer Suriadinata', 2, 0, 0),
('Jenny Lee', 1, 0, 0),
('Jinwon Jang', 1, 0, 0),
('Jisu Kim', 2, 1, 0),
('Joseph Kwon', 1, 0, 0),
('Josh Lee', 1, 4, 0),
('Josh Park', 1, 1, 0),
('Jungwoo Joo', 1, 0, 0),
('Kelvin Mun', 2, 0, 0),
('Kwonwoo Choi', 2, 0, 0),
('Laura Kim', 1, 0, 0),
('Michael He', 1, 3, 0),
('Michaela Kang', 1, 1, 0),
('Nathan Hoang', 1, 1, 0),
('Nick Lee', 1, 5, 0),
('Paul Lee', 1, 1, 0),
('Sam Lee', 1, 0, 0),
('Seoyon Lee', 1, 0, 0),
('Stephanie Choi', 1, 0, 0),
('Sue Jin Park', 1, 0, 0),
('Tae Kim', 2, 3, 0),
('Tae Park', 2, 0, 0),
('Tori Kim', 1, 3, 0),
('Will Kim', 0, 1, 0)
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
