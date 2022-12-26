from conans import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.env import Environment
import os


class ConanCppTemplate(ConanFile):
    name = "conanCppTemplate"
    version = "0.0.1"
    license = "MIT"
    author = "yuzz"
    url = "https://github.com/yzz-ihep/conanCppTemplate.git"
    description = "conan template cpp project"
    topics = ("cpp", "conan", "template")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [
        True, False], "use_imports": [True, False]}
    default_options = {"shared": True, "fPIC": True, "use_imports": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    # 自己增加的环境变量, 将第三方依赖放在external_root
    # 在运行可执行文件时需要source setup.sh
    external_root = os.getenv('HOME')+'/conanenvs/base'
    CPLUS_INCLUDE_PATH = external_root+'/include'
    C_INCLUDE_PATH = external_root+'/include'
    LD_LIBRARY_PATH = external_root+'/lib'
    LIBRARY_PATH = external_root+'/lib'

    def requirements(self):
        self.requires("spdlog/1.11.0")
        self.requires("fmt/9.1.0")
        self.options['spdlog'].shared = True
        self.options['fmt'].shared = True

    def imports(self):
        if self.options.use_imports:
            self.copy("*", src="bin", dst=self.external_root+"/bin")
            self.copy("*", src="lib", dst=self.external_root+"/lib")
            self.copy("*", src="include", dst=self.external_root+"/include")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        if self.options.use_imports:
            # These tools are still experimental
            env = Environment()
            env.append_path("CPLUS_INCLUDE_PATH", self.CPLUS_INCLUDE_PATH)
            env.append_path("C_INCLUDE_PATH", self.C_INCLUDE_PATH)
            env.append_path("LD_LIBRARY_PATH", self.LD_LIBRARY_PATH)
            env.append_path("LIBRARY_PATH", self.LIBRARY_PATH)
            envvars = env.vars(self)
            envvars.save_script("setup.sh")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        '''Method used to retrieve the source code from any other external origin like github using'''
        pass

    def build(self):
        '''This method is used to build the source code of the recipe using the desired commands. 
        You can use your command line tools to invoke your build system or any of the build helpers provided with Conan.'''
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["hello"]  # The libs to link against
