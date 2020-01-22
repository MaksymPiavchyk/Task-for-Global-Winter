import requests
from time import sleep

def fan_out_func(link: str):
  for line in requests.get(link).content.decode().splitlines():
    sleep(1.0)
    print(line)

if name == "main":
fan_out_func("https://trello-attachments.s3.amazonaws.com/5dd679bb914ca14cd8f8deb5/5e232bee8e8918566959e50f/e70dc5cb6288448b75279c64fb9323c9/fun0out.txt")
