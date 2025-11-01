pkgname = 'lean'
pkgver = '4.24.0'
_mimallocver = '3.0.10'
_cadicalver = '2.1.3'
pkgrel = 0
build_style = 'cmake'
make_cmd = 'gmake'
hostmakedepends = ['clang', 'cmake', 'gmp-devel', 'pkgconf', 'libuv-devel',
    'python', 'bash']
depends = ['gmp', 'libuv']
pkgdesc = 'Lean 4 programming language and theorem prover'
license = 'Apache-2.0'
url = 'https://lean-lang.org'
source = [
    f'https://github.com/leanprover/lean4/archive/refs/tags/v{pkgver}.tar.gz',
    f'https://github.com/microsoft/mimalloc/archive/refs/tags/v{_mimallocver}.tar.gz',
    f'https://github.com/arminbiere/cadical/archive/refs/tags/rel-{_cadicalver}.tar.gz',
]
sha256 = [
    '6e1a5dd9b541e4686b49017d871500811f33021234d5c17fb347e685839844e2',
    'ee5556a31060f2289497f00126e90bf871e90933f98e21ea13dca3578e9ccfb5',
    'abfe890aa4ccda7b8449c7ad41acb113cfb8e7e8fbf5e49369075f9b00d70465',
]

def post_extract(self):
    self.mv(self.srcdir / f'lean4-{pkgver}/*', self.srcdir, glob=True)
    self.rm(self.srcdir / f'lean4-{pkgver}', recursive=True)
    self.mv(self.srcdir / f'cadical-rel-{_cadicalver}', self.srcdir / 'cadical')
    self.mv(self.srcdir / f'mimalloc-{_mimallocver}', self.srcdir / 'mimalloc')

def post_install(self):
    self.install_license(self.srcdir / 'LICENSE')
    self.install_license(self.srcdir / 'LICENSES')
    self.uninstall('usr/src')

@subpackage("lean-static")
def _(self):
    return ["usr/lib/lean/*.a"]
