import subprocess
import sys


def build_remote_code():
    return r'''
import os


def rm_tree(path):
    try:
        for name in os.listdir(path):
            rm_tree(path + '/' + name)
        os.rmdir(path)
    except OSError:
        try:
            os.remove(path)
        except OSError:
            pass


rm_tree("app")
'''


def main():
    if len(sys.argv) > 1 and sys.argv[1] in {"-h", "--help"}:
        print("Usage: python clear_app.py [PORT]")
        print("Example: python clear_app.py COM3")
        return 0

    port = sys.argv[1] if len(sys.argv) > 1 else "COM3"
    cmd = ["mpremote", "connect", port, "exec", build_remote_code()]
    print(f"Clearing /app on ESP32 at port {port}...")
    subprocess.run(cmd, check=True)
    print("Finished.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
