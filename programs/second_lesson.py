from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
while True:
    pos = mc.player.getTilePos()
    mc.postToChat('x=' + str(pos.x) + ' y=' + str(pos.y) + ' z=' + str(pos.z))
    time.sleep(1)
