from conans import ConanFile, CMake

class PocoTimerConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "Poco/1.7.2@lasote/stable"
    generators = "cmake", "gcc", "txt"
    options = {"shared": [True, False]} # Values can be True or False (number or string value is also possible)
    default_options = "shared=False", "Poco:shared=True", "OpenSSL:shared=True"

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin") # From bin to bin
        self.copy("*.dylib*", dst="bin", src="lib") # From lib to bin

    def build(self):
        cmake = CMake(self.settings)
        shared_definition = "-DSHARED=1" if self.options.shared else ""
        self.run('cmake "%s" %s %s' % (self.conanfile_directory, cmake.command_line, shared_definition))
        self.run('cmake --build . %s' % cmake.build_config)