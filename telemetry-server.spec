# telemetry-server.spec
from PyInstaller.utils.hooks import collect_submodules
import sys
import os

block_cipher = None

# Make sure PyInstaller knows about any hidden imports (grpc, protobuf reflection, etc.)
hidden_imports = collect_submodules('grpc') + collect_submodules('google')

# Add any .proto files or data files if needed (example below)
datas = [
    ('protos/*.proto', 'protos')  # adjust if your .proto files are elsewhere
]

a = Analysis(
    ['server/main.py'],
    pathex=[os.path.abspath('.')],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='telemetry-server',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='telemetry-server'
)