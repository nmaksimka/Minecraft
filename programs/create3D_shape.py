from mcpi.minecraft import Minecraft
import mcpi.block as block
from minecraftstuff import MinecraftDrawing
import time
mc = Minecraft.create()
mcdraw = MinecraftDrawing(mc)
pos = mc.player.getTilePos()
# mc.setBlocks(pos.x, pos.y, pos.z, pos.x + 5, pos.y + 20, pos.z + 10, block.DIRT.id)
# mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x + 4, pos.y + 19, pos.z + 9, 0)
# mcdraw.drawSphere(pos.x + 20, pos.y, pos.z, 50, block.NETHER_BRICK.id)
mcdraw.drawSphere(pos.x, pos.y, pos.z, 20, 0)