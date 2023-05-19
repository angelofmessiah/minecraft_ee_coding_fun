def make_phalanx(width, length, mob):
    for x in range(width):
        for z in range(length):
            start_pos = pos(1, 0, 0)
            summon_string = 'summon ' + mob
            mobs.execute(mobs.target(NEAREST_PLAYER), positions.add(start_pos, pos(x, 0, z)), summon_string)

make_phalanx(7, 7, 'iron_golem')
