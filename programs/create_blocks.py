from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create()
pos = mc.player.getTilePos()
for i in range(5):
    for j in range(5):
        for k in range(5):


    #mc.postToChat('AAAAAAAAAAAAAAAAAAAAAAAAAAA')
            mc.setBlock(pos.x + k, pos.y + i - 1, pos.z + j, i)

    # mc.setBlock(pos.x + 3, pos.y + 1 + i, pos.z, i)
    # mc.setBlock(pos.x + 3, pos.y + 2 + i, pos.z, i)
    # mc.setBlock(pos.x + 3, pos.y + i, pos.z + 1, i)
    # mc.setBlock(pos.x + 3, pos.y + 1 + i, pos.z + 1, i)
    # mc.setBlock(pos.x + 3, pos.y + 2 + i, pos.z + 1, i)
    # mc.setBlock(pos.x + 3, pos.y + i, pos.z + 2, i)
    # mc.setBlock(pos.x + 3, pos.y + 1 + i, pos.z + 2, i)
    # mc.setBlock(pos.x + 3, pos.y + 2 + i, pos.z + 2, i)