import nonebot
from nonebot.adapters.onebot.v11 import Adapter

nonebot.init()

driver = nonebot.get_driver()

app = nonebot.get_asgi()
driver.register_adapter(Adapter)

# nonebot.load_builtin_plugins('echo')
nonebot.load_from_toml("pyproject.toml")
if __name__ == "__main__":
    nonebot.run()

