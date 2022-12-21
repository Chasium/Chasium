// Start a websocket server

import { WebSocketServer } from "ws";
import EvalJSScript from "./main";

const port = 1234;
const wss = new WebSocketServer({ port });

wss.on("connection", (ws) => {
  // handles new connections
  ws.on("message", (data) => {
    console.log(`received message from client: ${data}`);
    const result = EvalJSScript(`${data}`);
    var msg = JSON.stringify(result);
    ws.send(msg);
  });
  ws.send(`hello, this is server.ts!`);
});

console.log(`listening at port: ${port}...`);
