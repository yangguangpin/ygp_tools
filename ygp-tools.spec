# -*- mode: python ; coding: utf-8 -*-

import os
import sys

block_cipher = None

# 打包时包含 lib 目录下的本地 JS 库（如果存在）
lib_datas = []
lib_path = os.path.join(os.getcwd(), 'lib')
if os.path.isdir(lib_path):
    for fname in os.listdir(lib_path):
        if fname.endswith('.js'):
            lib_datas.append((os.path.join(lib_path, fname), 'lib'))

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('index.html', '.')] + lib_datas,
    hiddenimports=['webview'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='YGP工具箱',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',
)
