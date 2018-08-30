from conans import ConanFile, CMake, tools
import os

class TacopieTestConan(ConanFile):
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is in "test_package"
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            with tools.chdir("bin"):
                self.run(".%stacopie_logger" % os.sep, run_environment=True)
