pkgname = 'odin'
pkgver = '2025.07'
pkgrel = 0
hostmakedepends = ['clang', 'cmake', 'gmake', 'linux-headers', 'llvm-devel']
depends = ['llvm-libs', 'odin-vendor', 'odin-vendor-static']
pkgdesc = 'Odin programming language'
license = 'BSD-3-Clause'
url = 'https://odin-lang.org'
source = 'https://github.com/odin-lang/Odin/archive/refs/tags/dev-' + \
    pkgver.replace(".", "-") + '.tar.gz'
sha256 = 'f0b59fe4aadd1003c632c6b30468730c7a6a0e90578f26f70201c9796a420531'

def build(self):
    self.do(self.chroot_srcdir / 'build_odin.sh', 'release-native')
    self.do('make', '-C', self.chroot_srcdir / 'vendor/cgltf/src')
    self.do('make', '-C', self.chroot_srcdir / 'vendor/miniaudio/src')
    self.do('make', '-C', self.chroot_srcdir / 'vendor/stb/src')

def check(self):
    self.do(self.chroot_srcdir / 'odin', 'run',
        self.chroot_srcdir / 'examples/demo', '-vet', '-strict-style', '--',
        'Hellope World')

def install(self):
    self.install_dir('usr/bin')
    self.install_dir('usr/lib/odin')
    self.install_file('odin', 'usr/lib/odin', mode=0o755)
    for d in ['base', 'core', 'shared', 'vendor']:
        self.cp(self.srcdir / d, self.destdir / f'usr/lib/odin/{d}',
            recursive=True)
    for f in [
        'usr/lib/odin/vendor/raylib/linux/*.so*',
        'usr/lib/odin/vendor/raylib/macos/*.dylib',
        'usr/lib/odin/vendor/raylib/macos-arm64/*.dylib',
        'usr/lib/odin/vendor/lua/*/linux/*.so'
    ]: self.uninstall(f, glob=True)
    self.install_link('usr/bin/odin', '../lib/odin/odin', absolute=True)
    self.install_license(self.srcdir / 'LICENSE')

@subpackage("odin-vendor")
def _(self):
    return [
        "lib:odin/vendor/darwin",
        "lib:odin/vendor/egl",
        "lib:odin/vendor/fontstash",
        "lib:odin/vendor/libc",
        "lib:odin/vendor/microui",
        "lib:odin/vendor/nanovg",
        "lib:odin/vendor/OpenGL",
        "lib:odin/vendor/vulkan",
        "lib:odin/vendor/wasm",
        "lib:odin/vendor/wgpu",
        "lib:odin/vendor/windows",
        "lib:odin/vendor/x11"
    ]

@subpackage("odin-vendor-static")
def _(self):
    return [
        "lib:odin/vendor/box2d",
        "lib:odin/vendor/cgltf",
        "lib:odin/vendor/commonmark",
        "lib:odin/vendor/compress",
        "lib:odin/vendor/directx",
        "lib:odin/vendor/ENet",
        "lib:odin/vendor/ggpo",
        "lib:odin/vendor/glfw",
        "lib:odin/vendor/lua",
        "lib:odin/vendor/miniaudio",
        "lib:odin/vendor/OpenEXRCore",
        "lib:odin/vendor/portmidi",
        "lib:odin/vendor/raylib",
        "lib:odin/vendor/sdl2",
        "lib:odin/vendor/sdl3",
        "lib:odin/vendor/stb",
        "lib:odin/vendor/zlib"
    ]
