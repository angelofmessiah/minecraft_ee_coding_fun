def make_pyramid(level, material, inversed=False):
    start_pos = player.position()
    if inversed:
        for i in range(level):
            blocks.fill(material, positions.add(start_pos, world(i*-1+3, i, i*-1)), positions.add(start_pos, world(i+3, i, i)), FillOperation.REPLACE)
    else:
        for i in range(level):
            blocks.fill(material, positions.add(start_pos, world((level-i-1)*-1+3, i, (level-i-1)*-1)), positions.add(start_pos, world((level-i-1)+3, i, level-i-1)), FillOperation.REPLACE)

def spherical_destruction(radius=5):
    start_pos = player.position()
    for x in range(radius*-1, radius):
        for y in range(radius*-1, radius):
            for z in range(radius*-1, radius):
                distance = Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2) + Math.pow(z, 2))
                if distance <= radius:
                    destination = positions.add(start_pos, world(x, y, z))
                    blocks.place(AIR, destination)

# Main process
# while True:
#     spherical_destruction(radius = 30)

# make_pyramid(3, IRON_BLOCK)
