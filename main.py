Web VPython 3.2

box(pos = vec (0,0,-25), size = vec (20,0.1,60), texture = textures.stucco)
b = sphere(pos = vec (0,0.5,0), size = vec (1,1,1), color = vec (0,0,1))
while True :
    rate(100)
    k = keysdown()
    if 'd' in k :
      b.pos.x = b.pos.x + 0.1
    if 'a' in k :
      b.pos.x = b.pos.x - 0.1
    if 'w' in k :
      b.pos.z = b.pos.z - 0.1
    if 's' in k :
      b.pos.z = b.pos.z + 0.1
