# -*- mode: python ; coding: utf-8 -*-

block_chipher = None

add_files = [ ('ui\\012Chat.ui', '.'), ('ui\\012Chat_changename.ui', '.'), ('ui\\012Chat_emoji.ui', '.'), ('ui\\012Chat_exit.ui', '.'), ('resource\\012Chat.ico','.'), ('resource\\SEBANG Gothic.ttf','.') ]

a = Analysis(
    ['src\\main_gui.py'],
    pathex=[],
    binaries=[],
    datas=add_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    icon='C:\\Users\\Saenozu\\Documents\\Assignment\\컴네\\TP\\012Chat\\resource\\012Chat.ico',
    name='012Chat.exe',
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
)
