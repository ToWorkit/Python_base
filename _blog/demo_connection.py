import orm, asyncio
# 从models中导入
from models import User, Blog, Comment

async def test(loop):
  # 用户名，密码，数据库名
  await orm.create_pool(loop=loop, user='www', password='www', db='awesome')
  u = User(name='Test_01', email='Test_01@db.com', password='test_01', image='about:blank')
  await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
