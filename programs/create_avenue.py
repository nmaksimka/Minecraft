from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc = Minecraft.create()
pos = mc.player.getTilePos()
s = 9
x = pos.x + 2
y = pos.y
z = pos.z
def build():
    mc.setBlocks(x, y, z, x + s + 1, y + s + 10, z + s + 1, 0)
    mc.setBlocks(x - 10, y - 1, z - 10, x + s + 10, y - 10, z + s + 10, 2)
    mx = x + s / 2
    my = y + s / 2

    mc.setBlocks(x, y, z, x + s, y + s, z + s, 4)
    mc.setBlocks(x + 1, y + 1, z + 1, x + s - 1, y + s - 1, z + s - 1, 0)

    mc.setBlocks(x + 1, y, z + 1, x + s - 1, y, z + s - 1, 5)

    mc.setBlocks(mx + 1, y + 1, z, mx, y + 2, z, 0)
    time.sleep(1)
    mc.setBlocks(mx, y + 1, z, mx + 1, y + 1, z, 107)

    mc.setBlocks(mx + 2, my + 2, z, mx + 3, my + 3, z, 102)
    mc.setBlocks(mx - 1, my + 2, z, mx - 2, my + 3, z, 102)

    for i in range(6):
        mc.setBlocks(x + i - 1, y + s, z - 1, x + s - i + 1, y + s + i, z + s + 1, 5)

for j in range(10):
    build()
    x += s + 5