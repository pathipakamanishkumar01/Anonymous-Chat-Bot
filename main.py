from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()
messages = []

@app.get("/", response_class=HTMLResponse)
def form():
    return """
    <form method="post" action="/send">
      <textarea name="msg" placeholder="Type an anonymous message..."></textarea>
      <br>
      <button type="submit">Send Message</button>
    </form>
    """

@app.post("/send")
def send(msg: str = Form(...)):
    messages.append(msg)
    return {"status": "Message sent anonymously!"}

@app.get("/inbox")
def inbox():
    return {"messages": messages}
