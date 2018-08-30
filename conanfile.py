from conans import ConanFile, CMake, tools
import os


class TacoPieConan(ConanFile):
    name = "tacopie"
    version = "3.2.0"
    license = "MIT"
    homepage = "https://github.com/Cylix/tacopie"
    description = "tacopie is a multi-platform TCP Client & Server C++11 library"
    url = "https://github.com/db4/conan-tacopie"
    settings = "os", "compiler", "build_type", "arch"
    options = {"fPIC": [True, False]}
    default_options = "fPIC=True"
    generators = "cmake"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        url = "https://github.com/Cylix/tacopie.git"
        self.run("git clone " + url)
        self.run("cd %s && git checkout %s" % (self.name, self.version))
        tools.replace_in_file("%s/CMakeLists.txt" % self.name, "project(${PROJECT} CXX)",
                              """project(${PROJECT} CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()""")

    def build(self):
        cmake = CMake(self)
        if self.settings.os != "Windows":
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.definitions["CMAKE_INSTALL_PREFIX"] = "install"
        if self.settings.compiler == "Visual Studio":
            # work around the broken logic not expecting /MTd or /MDd
            cmake.definitions["MSVC_RUNTIME_LIBRARY_CONFIG"] = "/"+str(self.settings.compiler.runtime)[:2]
        cmake.configure(source_folder=self.name)
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*", dst="include", src="install/include", keep_path=True)
        self.copy("*.lib", dst="lib", src="install", keep_path=False)
        self.copy("*.pdb", dst="bin", src="install", keep_path=False)
        self.copy("*.a", dst="lib", src="install", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [self.name]
