import json, os
from http.server import BaseHTTPRequestHandler, HTTPServer

STAGES=["READ","NOTE","QUESTION","ARGUE","WRITE","FEEDBACK","REVISE","ARCHIVE"]
DATA=os.getenv("DATA_PATH","/tmp/scholar.json")

def load():
    try:
        with open(DATA,encoding="utf-8") as f:return json.load(f)
    except Exception:return {"stage":"READ","artifacts":[]}

def save(x):
    os.makedirs(os.path.dirname(DATA),exist_ok=True)
    with open(DATA,"w",encoding="utf-8") as f:json.dump(x,f,ensure_ascii=False,indent=2)

class H(BaseHTTPRequestHandler):
    def out(self,code,obj):
        b=json.dumps(obj,ensure_ascii=False).encode()
        self.send_response(code);self.send_header("Content-Type","application/json; charset=utf-8");self.send_header("Content-Length",str(len(b)));self.end_headers();self.wfile.write(b)
    def do_GET(self):
        if self.path=="/health":return self.out(200,{"ok":True,"system":"UTM-Scholar-Loop"})
        if self.path=="/state":return self.out(200,load())
        self.out(404,{"error":"not found"})
    def do_POST(self):
        if self.path!="/advance":return self.out(404,{"error":"not found"})
        try:
            n=int(self.headers.get("Content-Length","0")); p=json.loads(self.rfile.read(n) or b"{}")
            stage=p.get("stage"); artifact=str(p.get("artifact","")).strip()
            s=load()
            if stage!=s["stage"]:return self.out(409,{"error":"expected stage","expected":s["stage"]})
            if not artifact:return self.out(400,{"error":"artifact required"})
            s["artifacts"].append({"stage":stage,"artifact":artifact})
            s["stage"]=STAGES[(STAGES.index(stage)+1)%len(STAGES)]
            save(s);return self.out(200,s)
        except Exception as e:return self.out(400,{"error":str(e)})

HTTPServer(("0.0.0.0",int(os.getenv("PORT","8080"))),H).serve_forever()
