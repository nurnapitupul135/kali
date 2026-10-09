import socket
import os

mesin = socket.gethostname()
print(f"Worker / Nama Mesin: {mesin}")

wallet = f"prl1pjp3jd7ue653f6zyrn9ewwu7lalw538kn5w2l4lekv0g3nxqlj23qnwg6g0.{mesin}"
print(f"Mining dengan: {wallet}")

# langsung jalanin
os.system(f'/app/peakminer/peakminer --coin pearl -o pearl-eu2.luckypool.io:3360 -u {wallet}')
