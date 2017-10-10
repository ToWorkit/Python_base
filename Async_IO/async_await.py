import asyncio

async def hello():
  print('Hello World')
  r = await asyncio.sleep(1)
  print('Hello Agin') 

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
