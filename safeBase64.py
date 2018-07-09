import base64

def safe_base64_decode(s):
    print(base64.b64decode(s + b'=' * (- len(s) % 4)))

safe_base64_decode(b'YWJjZA==')
safe_base64_decode(b'YWJjZA')