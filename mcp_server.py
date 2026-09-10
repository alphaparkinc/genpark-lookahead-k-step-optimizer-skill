import json
import sys
from client import LookaheadOptimizer

lh = LookaheadOptimizer()

def handle_rpc(line):
    try:
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        rid = req.get("id")
        
        if method == "tools/list":
            tools = [
                {"name": "lookahead_step", "description": "Step lookahead optimizer with fast weight"}
            ]
            return json.dumps({"jsonrpc": "2.0", "id": rid, "result": {"tools": tools}})
        elif method == "tools/call":
            tname = params.get("name")
            args = params.get("arguments", {})
            if tname == "lookahead_step":
                w = lh.step(args["fast_weight"], args.get("param_id", 0))
                return json.dumps({"jsonrpc": "2.0", "id": rid, "result": {"weight": w}})
    except Exception as e:
        return json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}})

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(handle_rpc(line.strip()), flush=True)
