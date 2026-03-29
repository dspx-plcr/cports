pkgname = "distroshelf"
pkgver = "1.4.8"
pkgrel = 1
build_style = "meson"
configure_args = ["-Doffline=true"]
hostmakedepends = [
    "bash",
    "cargo-auditable",
    "gettext",
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = [
    "desktop-file-utils",
    "glib-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "rust-std",
    "vte-gtk4-devel"
]
depends = [ "distrobox", "libadwaita", "gtk4", "vte-gtk4" ]
pkgdesc = "Distrobox GUI"
license = "GPL-3.0-only"
url = "https://github.com/ranfdev/DistroShelf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f2f430d6924a69a21d6476e26649eddf4d074e5cf7fd43cd0dee2bb89f303ee8"
# complains about not being able to determine template linter
options = ["!lint"]

def post_extract(self):
    self.chmod(self.srcdir / "build-aux" / "dist-vendor.sh", 0o555)

    mdir = self.chroot_srcdir / self.make_dir
    vdir = mdir / "meson-dist" / f"{pkgname}-{pkgver}"
    self.mkdir(self.bldroot_path / vdir.relative_to(vdir.anchor), parents=True)
    self.do(self.chroot_srcdir / "build-aux" / "dist-vendor.sh", vdir, mdir,
        allow_network=True)

    self.mkdir(self.srcdir / ".cargo")
    with open(self.srcdir / ".cargo" / "config.toml", "w") as f:
        f.write("""
[source.crates-io]
registry = "https://github.com"
replace-with = 'vendored-sources'

[source.vendored-sources]
directory = "{}"
        """.format(vdir / "vendor"))
    return
