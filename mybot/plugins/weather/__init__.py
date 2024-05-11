from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, MessageEvent

# 创建命令处理器，响应“天气”或“weather”命令，要求消息直接对机器人
weather_cmd = on_command("weather", aliases={"天气"}, rule=to_me(), priority=5)


# 当命令触发时的处理函数
@weather_cmd.handle()
async def handle_weather_command(bot: Bot, event: MessageEvent):
    # 提取消息中的参数（城市名），这里我们简化处理，不对参数进行解析
    city = str(event.get_message()).strip()
    id = bot.self_id
    # 如果城市名为空，则询问用户
    if not city:
        await weather_cmd.finish("请问你想查询哪个城市的天气呢？")

    # 返回模拟的天气信息
    weather_info = f"{city}的天气预报是晴朗，气温25°C。"
    await weather_cmd.finish(weather_info+id)

