# This file is meant to store any special effects.
# These can be some images or transforms.

image yuri dragon2:
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat

image blood splatter1:
    size (1, 1)
    truecenter
    Blood("blood_particle",dripTime=0.5, burstSize=150, burstSpeedX=400.0, burstSpeedY=400.0, numSquirts=15, squirtPower=400, squirtTime=2.0).sm


image k_rects_eyes1:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (580, 270)
    size (20, 25)
    8.0

image k_rects_eyes2:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (652, 264)
    size (20, 25)
    8.0

image natsuki mas_ghost:
    "natsuki ghost2"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
image mujina:
    "mod_assets/other/mujina.png"
    zoom 1.25
    parallel:
        easeout 0.5 zoom 4.5 yoffset 1200
    0.5


transform k_scare:
    tinstant(640)
    ease 1.0 zoom 2.0

transform otei_appear(a=0.70,time=1.0):
    i11
    alpha 0.0
    linear time alpha a
