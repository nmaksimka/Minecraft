from mcpi.minecraft import Minecraft
import mcpi.block as block
from minecraftstuff import MinecraftDrawing
import time
mc = Minecraft.create()
mcdraw = MinecraftDrawing(mc)
pos = mc.player.getTilePos()

mcdraw.drawLine(pos.x, pos.y, pos.z, pos.x, pos.y + 10, pos.z, block.PUMPKIN.id)
mcdraw.drawLine(pos.x, pos.y, pos.z, pos.x + 10, pos.y, pos.z, block.PUMPKIN.id)
mcdraw.drawLine(pos.x, pos.y + 10, pos.z, pos.x + 10, pos.y + 10, pos.z, block.PUMPKIN.id)
mcdraw.drawLine(pos.x + 10, pos.y, pos.z, pos.x + 10, pos.y + 10, pos.z, block.PUMPKIN.id)
mcdraw.drawLine(pos.x, pos.y + 10, pos.z, pos.x + 10, pos.y, pos.z, block.PUMPKIN.id)
for i in range(10):
    mcdraw.drawCircle(pos.x, pos.y, pos.z, i * (i + 1), block.WOOL.id)
    time.sleep(1)
