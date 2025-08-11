from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
import json


# 注册插件
@register(name="BotDescParameter", description="BotDescParameter", version="0.1.2", author="wudao")
class BotDescParameter(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    # 当收到个人消息时触发
    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        # 输出调试信息
        query = ctx.event.query
        config = query.adapter.config
        query.set_variable("adapter_config", json.dumps(config))

    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        query = ctx.event.query
        config = query.adapter.config
        query.set_variable("adapter_config", json.dumps({"name": "Alice", "age": 25}, ensure_ascii=False))

    # 插件卸载时触发
    def __del__(self):
        pass
