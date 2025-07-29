pkgname = "microhs"
_mhs_commit = "40ea4804394973fefc5eec8e879b1b43e69dc8cb"
_mhscpp_commit = '4aa6fca96294855fc930910953bcdcca2708e991'
pkgver = "0_git20250711"
pkgrel = 0
build_style = "makefile"
make_install_target = 'oldinstall'
make_check_target = 'runtestmhs'
make_check_args = ['-j', '1']
hostmakedepends = ["clang", "gmp-devel", "git"]
depends = ["gmp"]
pkgdesc = "Implementation of an extended subset of Haskell"
license = "Apache-2.0"
url = "https://github.com/augustss/MicroHs"
source = [
    f"{url}/archive/{_mhs_commit}.tar.gz",
    "https://github.com/hackage-trustees/malcolm-wallace-universe/archive/" + \
        _mhscpp_commit + ".tar.gz",
]
sha256 = [
    "6f187d5353f46d14eab30d9347891e9dfde53efad383a9e84dbe042b1bb6db60",
    "2e08b984e57d70068ab984592503d792a07ce2b8b05d973cdd1e8f4fe67d9aec",
]

def post_extract(self):
    self.mv(self.srcdir / f'MicroHs-{_mhs_commit}/*', self.srcdir, glob=True)
    self.rm(self.srcdir / f'MicroHs-{_mhs_commit}', recursive=True)
    self.rm(self.srcdir / 'cpphssrc/malcolm-wallace-universe', recursive=True)
    self.mv(self.srcdir / f'malcolm-wallace-universe-{_mhscpp_commit}',
        self.srcdir / 'cpphssrc/malcolm-wallace-universe')

def build(self):
    self.make.invoke('bootstrap')
    self.make.invoke('bin/cpphs')
    self.make.invoke('bootstrapcpphs')

def install(self):
    self.install_license("LICENSE")
    self.make.install(args=['PREFIX='+str(self.chroot_destdir / 'usr/')])
