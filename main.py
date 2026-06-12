Web VPython 3.2

box(pos = vec (0,-10,0), size = vec (260,5,60), texture = textures.stucco)
box(pos = vec (-90,0,0), size = vec (10,15,10), texture = textures.stucco)
box(pos = vec (-60,0,0), size = vec (10,25,10), texture = textures.stucco)
box(pos = vec (-30,5,0), size = vec (10,35,10), texture = textures.stucco)
box(pos = vec (0,25,0), size = vec (20,5,20), texture = textures.stucco)
box(pos = vec (60,25,0), size = vec (20,5,20), texture = textures.stucco)
box(pos = vec (90,25,0), size = vec (10,5,10), texture = textures.stucco)
box(pos = vec (120,35,0), size = vec (20,5,20), texture = textures.stucco)
box(pos = vec (90,55,0), size = vec (20,5,20), texture = textures.stucco)
box(pos = vec (10,55,0), size = vec (90,5,20), texture = textures.stucco)
cone(pos = vec (10,25,0), size = vec (60,10,10), color = vec (1,0,0))

body = sphere(pos = vec (-120,-5,0), size = vec (5,5,5), color = vec (0,0,1))

head = sphere(pos = vec (-120,-2,0), size = vec (4,4,4), color = vec (1,1,1))

eye1 = sphere(pos = vec (-119,-2,2), size = vec (1,1,1), color = vec (0,0,0))
eye2 = sphere(pos = vec (-121,-2,2), size = vec (1,1,1), color = vec (0,0,0))

player = compound([head, body, eye1, eye2])

while True :
    rate(100)
    k = keysdown()
    if 'd' in k:
      player.pos.x += 0.4
    if 'a' in k:
      player.pos.x -= 0.4
    if ' ' in k:
      player.pos.y += 0.4
    if 's' in k:
      player.pos.y -= 0.4
