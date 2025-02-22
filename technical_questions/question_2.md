# What is event stream and response in web browser?
When working with HTTP and real-time communication, two important concepts are event streams and HTTP responses.

## HTTP Response in a Web Browser
An HTTP response is the data sent by a server after a client (like a browser) makes a request.

Example
When you visit https://example.com, your browser:

Sends an HTTP request (GET /).
Receives an HTTP response from the server.
A typical HTTP response includes:

Status Code (e.g., 200 OK, 404 Not Found)
Headers (Metadata like Content-Type: text/html)
Body (The actual page content, JSON data, etc.)
Example Response
http
Copy
Edit
HTTP/1.1 200 OK
Content-Type: application/json

{"message": "Hello, world!"}
## Event Stream (Server-Sent Events - SSE)
An event stream is a way for a server to push updates to a browser continuously. This is useful for real-time updates like notifications, stock prices, or chat messages.

How It Works
The browser makes a persistent HTTP request to the server.
The server keeps the connection open and sends data as events occur.
The browser processes the incoming events without reloading the page.

## Example: Server-Sent Events (SSE)
SSE uses the text/event-stream content type to send updates:

🔹 Server Response (Streaming Data)
http
Copy
Edit
HTTP/1.1 200 OK
Content-Type: text/event-stream
Cache-Control: no-cache
Connection: keep-alive

data: {"message": "New notification"}
data: {"message": "Stock price updated"}
💡 The server keeps sending data as new events occur.

🔹 Browser Code (Listening to Event Stream)
js
Copy
Edit
const eventSource = new EventSource("https://example.com/stream");

eventSource.onmessage = (event) => {
    console.log("New message:", event.data);
};
This listens for new messages from the server in real-time.

## Key Differences
- Feature	HTTP Response	Event Stream (SSE)
- Type	One-time response	Continuous data stream
- Connection	Closes after response	Stays open
- Use Cases	Page loads, API requests	Real-time updates, notifications
-  Content-Type	text/html, application/json	text/event-stream

## When to Use Event Streams?
Use SSE if you need real-time updates but don’t want to constantly reload the page. Examples:

Live notifications
Chat messages
Stock price updates
Server logs
For two-way communication (e.g., chat), consider WebSockets instead.

# References
- [1] https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events