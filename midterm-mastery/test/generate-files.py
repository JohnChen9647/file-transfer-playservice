from hashlib import sha256
from pathlib import Path


output_dir = Path(__file__).parent / "generated"
output_dir.mkdir(exist_ok=True)

files = {
    "1b.txt": 1,
    "64b.txt": 64,
    "512b.txt": 512,
    "4k.txt": 4 * 1024,
    "32k.txt": 32 * 1024,
    "64k.txt": 64 * 1024,
    "128k.txt": 128 * 1024,
    "256k.txt": 256 * 1024,
    "2m.txt": 2 * 1024 * 1024,
    "4m.txt": 4 * 1024 * 1024,
}

for name, size in files.items():
    data = bytes(index % 256 for index in range(size))
    (output_dir / name).write_bytes(data)
    print(f"{name}: {size} bytes, SHA-256 {sha256(data).hexdigest()}")
