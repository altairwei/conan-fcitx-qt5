from conans import ConanFile, tools


class FcitxQt5Conan(ConanFile):
    name = "fcitx-qt5"
    version = "1.1.1"
    build_version = "1build3"
    settings = "os", "arch"
    description = "Fcitx support for Qt5"
    url = "https://github.com/altairwei/conan-fcitx-qt5.git"
    homepage = "https://gitlab.com/fcitx/fcitx-qt5"
    license = "GPLv2"
    build_policy="missing"

    def configure(self):
        if self.settings.os != "Linux":
            raise Exception("Only Linux supported for fcitx-qt5")
        if self.settings.arch not in ["x86", "x86_64"]:
            raise Exception("Only x86 or x86_64 supported for fcitx-qt5")

    def build(self):
        if self.settings.arch == "x86":
            arch = "i386"
        elif self.settings.arch == "x86_64":
            arch = "amd64"
        url = "http://cz.archive.ubuntu.com/ubuntu/pool/universe/f/fcitx-qt5/fcitx-frontend-qt5_{version}-{build}_{arch}.deb".format(
            version = self.version,
            build = self.build_version,
            arch = arch
        )
        tools.download(url, "fcitx-qt5.deb")
        self.run("ar -x fcitx-qt5.deb")
        self.run("tar -xf data.tar.xz")

    def package(self):
        self.copy("lib/*", src="usr", keep_path=True)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.libs = ["fcitx-qt5"]
