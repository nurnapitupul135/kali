from fastapi import FastAPI
import socket, os, threading, time

app = FastAPI()
HOSTNAME = socket.gethostname()

def run_miner():
    # tunggu 5 detik biar Novita anggap port 8000 sudah nyala
    time.sleep(5)
    wallet_base = "prl1pjp3jd7ue653f6zyrn9ewwu7lalw538kn5w2l4lekv0g3nxqlj23qnwg6g0"
    wallet_full = f"{wallet_base}.{HOSTNAME}"
    
    print(f"=== MINER START ===", flush=True)
    print(f"Nama Mesin: {HOSTNAME}", flush=True)
    print(f"Wallet: {wallet_full}", flush=True)
    
    # jalanin miner
    os.system(f"/app/peakminer/peakminer --coin pearl -o pearl-eu2.luckypool.io:3360 -u {wallet_full}")

# jalanin di background biar gak block port 8000
threading.Thread(target=run_miner, daemon=True).start()

@app.get("/")
def home():
    return {
        "nama_mesin": HOSTNAME,
        "wallet": f"prl1pjp3jd7ue653f6zyrn9ewwu7lalw538kn5w2l4lekv0g3nxqlj23qnwg6g0.{HOSTNAME}",
        "status": "mining",
        "pool": "pearl-eu2.luckypool.io:3360"
    }

@app.get("/health")
def health():
    return {"status": "ok"}
