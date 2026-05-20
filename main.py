Web VPython 3.2

box(pos = vec (0,75,-45), size = vec (260,5,5), texture = textures.stucco)
box(pos = vec (0,-75,-45), size = vec (260,5,5), texture = textures.stucco)
box(pos = vec (130,0,-45), size = vec (5,155,5), texture = textures.stucco)
box(pos = vec (-130,0,-45), size = vec (5,155,5), texture = textures.stucco)
box(pos = vec (-110,60,-45), size = vec (5,25,5), texture = textures.stucco)
box(pos = vec (-110,60,-45), size = vec (5,25,5), texture = textures.stucco)
b = sphere(pos = vec (-120,55,-45), size = vec (5,5,5), color = vec (0,0,1))
while True :
    rate(100)
    k = keysdown()
    if 'd' in k and b.pos.x > -125:
      b.pos.x = b.pos.x + 0.4
    if 'a' in k and b.pos.x > -125:
      b.pos.x = b.pos.x - 0.4
    if 'w' in k and b.pos.y > 10:
      b.pos.y = b.pos.y + 0.4
    if 's' in k and b.pos.y > -70:
      b.pos.y = b.pos.y - 0.4
