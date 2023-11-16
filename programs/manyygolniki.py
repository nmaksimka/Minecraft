from mcpi.minecraft import Minecraft
import mcpi.block as block
from minecraftstuff import MinecraftDrawing
from mcpi.vec3 import Vec3
import time
mc = Minecraft.create()
mcdraw = MinecraftDrawing(mc)
pos = mc.player.getTilePos()
point1 = list()
point1.append(Vec3(pos.x, pos.y, pos.z))
point1.append(Vec3(pos.x + 30, pos.y, pos.z))
point1.append(Vec3(pos.x + 15, pos.y + 15, pos.z + 15))
mcdraw.drawFace(point1, True, 57)
point2 = list()
point2.append(Vec3(pos.x, pos.y, pos.z))
point2.append(Vec3(pos.x, pos.y, pos.z + 30))
point2.append(Vec3(pos.x + 15, pos.y + 15, pos.z + 15))
mcdraw.drawFace(point2, True, 57)
point3 = list()
point3.append(Vec3(pos.x + 30, pos.y, pos.z))
point3.append(Vec3(pos.x + 30, pos.y, pos.z + 30))
point3.append(Vec3(pos.x + 15, pos.y + 15, pos.z + 15))
mcdraw.drawFace(point3, True, 57)
point4 = list()
point4.append(Vec3(pos.x, pos.y, pos.z + 30))
point4.append(Vec3(pos.x + 30, pos.y, pos.z + 30))
point4.append(Vec3(pos.x + 15, pos.y + 15, pos.z + 15))
mcdraw.drawFace(point4, True, 57)