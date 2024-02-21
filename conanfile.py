from conans import ConanFile, tools
import platform


class ModuleConan(ConanFile):
    name = "QtConanExample"
    description = "An example for Qt with Conan"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "cmake_find_package_multi", "cmake_paths"


    def configure(self):
        del self.settings.compiler.cppstd

    def requirements(self):
        self.requires("gtest/1.14.0")
        self.requires("sdl/2.28.5")
        self.requires("glew/2.2.0")
        self.requires("libpng/1.6.42")
        self.requires("nlohmann_json/3.11.3")
        self.requires("glm/cci.20230113")
        
    def imports(self):
        self.copy("*.dll", "./bin", "bin")
        self.copy("*.so", "./bin", "bin")