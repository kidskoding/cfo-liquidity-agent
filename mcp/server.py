from mcp.server import MCPServer
from stripe_tools import get_pending_balance, get_merchant_id

server = MCPServer()

server.register_tool(
    name="get_pending_balance",
    fn=get_pending_balance
)

server.register_tool(
    name="get_merchant_id",
    fn=get_merchant_id
)

server.run()
