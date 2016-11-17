#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os


def get_type():
	return "LIBRARY"

def get_desc():
	return "Franhofer AAC encoder/decoder"

def get_licence():
	return "BSD-like"

def get_compagny_type():
	return "com"

def get_compagny_name():
	return "franhofer"

def get_maintainer():
	return ["Martin Storsjo <martin@martin.st>"]

def get_version():
	return [0,0,0]

def configure(target, my_module):
	my_module.add_src_path("fdk-aac/libAACdec/src/", "*.cpp")
	my_module.add_src_path("fdk-aac/libAACenc/src/", "*.cpp", recursive=True)
	my_module.add_src_path("fdk-aac/libPCMutils/src/", "*.cpp", recursive=True)
	my_module.add_src_path("fdk-aac/libFDK/src/", "*.cpp")
	my_module.add_src_path("fdk-aac/libSYS/src/", "*.cpp")
	my_module.add_src_path("fdk-aac/libMpegTPDec/src/", "*.cpp", recursive=True)
	my_module.add_src_path("fdk-aac/libMpegTPEnc/src/", "*.cpp", recursive=True)
	my_module.add_src_path("fdk-aac/libSBRdec/src/", "*.cpp")
	my_module.add_src_path("fdk-aac/libSBRenc/src/", "*.cpp", recursive=True)
	if target.get_arch() == "arm":
		my_module.add_src_path("fdk-aac/libAACdec/src/arm", "*.cpp")
		my_module.add_src_path("fdk-aac/libFDK/src/arm", "*.cpp")
		my_module.add_src_path("fdk-aac/libSBRdec/src/arm", "*.cpp")
	elif target.get_arch() == "mips":
		my_module.add_src_path("fdk-aac/libAACdec/src/mips", "*.cpp")
		my_module.add_src_path("fdk-aac/libFDK/src/mips", "*.cpp")
		my_module.add_src_path("fdk-aac/libSBRdec/src/mips", "*.cpp")
		my_module.add_src_path("fdk-aac/libSYS/src/mips", "*.cpp")
		
	
	my_module.add_flag('cpp', [
	    '-Wno-sequence-point',
	    '-Wno-extra',
	    '-Wno-#warnings',
	    '-Wno-constant-logical-operand',
	    '-Wno-self-assign'
	    ])
	my_module.add_depend([
	    'cxx',
	    'm'
	    ])
	my_module.add_path("fdk-aac/libAACdec/include/")
	my_module.add_path("fdk-aac/libAACenc/include/")
	my_module.add_path("fdk-aac/libPCMutils/include/")
	my_module.add_path("fdk-aac/libFDK/include/")
	my_module.add_path("fdk-aac/libSYS/include/")
	my_module.add_path("fdk-aac/libMpegTPDec/include/")
	my_module.add_path("fdk-aac/libMpegTPEnc/include/")
	my_module.add_path("fdk-aac/libSBRdec/include/")
	my_module.add_path("fdk-aac/libSBRenc/include/")

	my_module.add_header_path("fdk-aac/libAACdec/include/", "*.h", destination_path="fdk-aac")
	my_module.add_header_path("fdk-aac/libAACenc/include/", "*.h", destination_path="fdk-aac")
	my_module.add_header_path("fdk-aac/libPCMutils/include/", "*.h", destination_path="fdk-aac")
	my_module.add_header_path("fdk-aac/libFDK/include/", "*.h", destination_path="fdk-aac")
	my_module.add_header_path("fdk-aac/libSYS/include/", "*.h", destination_path="fdk-aac")
	my_module.add_header_path("fdk-aac/libMpegTPDec/include/", "*.h", destination_path="fdk-aac")
	my_module.add_header_path("fdk-aac/libMpegTPEnc/include/", "*.h", destination_path="fdk-aac")
	my_module.add_header_path("fdk-aac/libSBRdec/include/", "*.h", destination_path="fdk-aac")
	my_module.add_header_path("fdk-aac/libSBRenc/include/", "*.h", destination_path="fdk-aac")

	return True


