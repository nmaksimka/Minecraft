from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
x1 = 443
x2 = 450
z1 = 792
z2 = 800
score = 10
mc.player.setPos(444.527, 80, 799.440)
while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x >= x1 and pos.x <= x2 and pos.z >= z1 and pos.z <= z2:
        score -= 1
        mc.postToChat('score =' + ' ' + str(score))
    if score == 0:
        mc.postToChat('you lose')
        break