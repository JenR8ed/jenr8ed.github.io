from playwright.sync_api import sync_playwright
import threading
import http.server
import socketserver
import time

Handler = http.server.SimpleHTTPRequestHandler

def test_copy_to_clipboard_error():
    with socketserver.TCPServer(("", 0), Handler) as httpd:
        port = httpd.server_address[1]
        server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        server_thread.start()

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"http://localhost:{port}")

            dialog_messages = []

            def handle_dialog(dialog):
                dialog_messages.append(dialog.message)
                dialog.accept()

            page.on("dialog", handle_dialog)

            page.evaluate("""() => {
                navigator.clipboard.writeText = function() {
                    return Promise.reject(new Error('Clipboard error'));
                };

                copyToClipboard('test@example.com', null);
            }""")

            page.wait_for_timeout(500)

            assert len(dialog_messages) > 0, "Dialog was not called"
            assert "Copy email:" in dialog_messages[0], f"Expected 'Copy email:', got {dialog_messages[0]}"

            browser.close()

        httpd.shutdown()

if __name__ == "__main__":
    test_copy_to_clipboard_error()
    print("Test test_copy_to_clipboard_error passed!")
