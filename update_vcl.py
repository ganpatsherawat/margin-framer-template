import subprocess
import os

fastly = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Fastly.CLI_Microsoft.Winget.Source_8wekyb3d8bbwe\fastly.exe")

with open(r"d:\margin-framer-template\fastly-rewrite.vcl", "r", encoding="utf-8") as f:
    vcl_content = f.read()

print("VCL to send:")
print(vcl_content)

res = subprocess.run([
    fastly,
    "service", "vcl", "snippet", "update",
    "--service-id", "x3NEHWP0web93f8CUTVstH",
    "--version", "1",
    "--name", "rewrite_path",
    "--content", vcl_content
], capture_output=True, text=True)

print("STDOUT:\n", res.stdout)
print("STDERR:\n", res.stderr)
