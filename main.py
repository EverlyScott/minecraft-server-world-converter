import anvil
import json

array = []

minChunkX = 0
maxChunkX = 16
minChunkZ = 0
maxChunkZ = 16

maxX = 16
maxY = 255
maxZ = 16

region = anvil.Region.from_file('r.0.0.mca')

for chunkX in range(maxChunkX):
  for chunkZ in range(maxChunkZ):
    if chunkX > minChunkX and chunkZ > minChunkZ:
      print('Now working on chunk '+str(chunkX)+', '+str(chunkZ))
      chunk = anvil.Chunk.from_region(region, chunkX, chunkZ)
      chunkElement = {
        "chunkX": chunkX,
        "chunkZ": chunkZ,
        "blocks": []
      }
      array.append(chunkElement)
      for x in range(maxX):
        for z in range(maxZ):
          for y in range(maxY):
            block = chunk.get_block(x, y, z)
            if block.id != 'air' and block.id != 'cave_air':
              # print(x+minChunkX, y+minChunkX, z+minChunkX)
              if minChunkX != 0:
                chunkElement['blocks'].append({
                  "x": x+minChunkX,
                  "y": y+minChunkX,
                  "z": z+minChunkX,
                  "type": block.id,
                  "prop": str(block.properties)
                })
              else:
                chunkElement['blocks'].append({
                  "x": x,
                  "y": y,
                  "z": z,
                  "type": block.id,
                  "prop": str(block.properties)
                })
      array.append(chunkElement)

print('Now writing file')
with open('world.json', 'w') as output:
  json.dump(array, output)