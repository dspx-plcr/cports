pkgname = "microcabal"
pkgver = "0_git20250714"
_commit = '75aab2f5dfa3bacc1876dc1da9828a7e54e01d68'
pkgrel = 0
build_style = "makefile"
make_check_target = 'test'
make_check_args = ['-j', '1']
hostmakedepends = ["microhs"]
depends = ["microhs"]
pkgdesc = "Reimplementation of a subset of Cabal"
license = "Apache-2.0"
url = "https://github.com/augustss/MicroCabal"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "b3b76178e93dfbbfb5112e9f8f29708ba2d92d7d9014197fba23a523c26b090c"

def build(self):
    self.make.invoke('bin/mcabal')

def install(self):
    self.install_license("LICENSE")
    self.install_bin(self.srcdir / 'bin/mcabal')
