#******************************************************************************
# Copyright (C) 2017 by Alex Fosdick - University of Colorado
#
# Redistribution, modification or use of this software in source or binary
# forms is permitted as long as the files maintain this copyright. Users are 
# permitted to modify this and use it to learn about the field of embedded
# software. Alex Fosdick and the University of Colorado are not liable for any
# misuse of this material. 
#
#*****************************************************************************

#------------------------------------------------------------------------------
# <Put a Description Here>
#
# Use: make [TARGET] [PLATFORM-OVERRIDES]
#
# Build Targets:
#      <Put a description of the supported targets here>
#
# Platform Overrides:
#      <Put a description of the supported Overrides here
#
include sources.mk

#------------------------------------------------------------------------------
## Command to use is
##make [TARGET] [PLATFORM]


# Platform:
#      This makefile supports 2 platforms: the host linux machine, and the MSP432 microcontroller.
#      For the MSP432 the specfic linker file (msp432p401r.lds), and arcitecture are different form the host platform
#

# Architectures Specific Flags

LINKER_FILE = 
CPU = 
ARCH = 
SPECS = 

# Compiler Flags and Defines
#CC = 
#LD = 
#LDFLAGS = 
#CFLAGS = 
#CPPFLAGs = 

BASE_NAME = c1m2

# Architectures Specific Flags
ifeq ($(PLATFORM), MSP432)
	LINKER_FILE = -T ../msp432p401r.lds 
	CPU = cortex-m4
	ARCH = armv7e-m
	SPECS = nosys.specs
else
	CPU = x86_64
	ARCH:=$(shell arch)

endif 

# Compiler Flags and Defines
ifeq ($(PLATFORM), MSP432)
	CC = arm-none-eabi-gcc
	LD = arm-none-eabi-ld
	LDFLAGS = -Wl,-Map=$(BASE_NAME).map $(LINKER_FILE) 
	CFLAGS = -mcpu=$(CPU) -march=$(ARCH) --specs=$(SPECS) -mfloat-abi=hard -mfpu=fpv4-sp-d16 -mthumb -Wall -Werror -O0 -g -std=c99  
	CPPFLAGs = -M -MF test.d
	DEFINEFLAG = -DMSP432

else
	CC = gcc
	#LD = 
	LDFLAGS = -Wl,-Map=$(BASE_NAME).map
	CFLAGS = -Wall -Werror -O0 -g -std=c99
	CPPFLAGs = -M -MF test2.d
	DEFINEFLAG = -DHOST
endif

#Variables
OBJS:= $(SOURCES:.c=.o)
ASMS:= $(SOURCES:.c=.s)
PPS:= $(SOURCES:.c=.i)
MAPS:= $(SOURCES:.c=.map)
OUTS:= $(SOURCES:.c=.out)

# Target: <file>.i
# Prerequisites: the .c file
# Output: the .d as well as .i files
%.i : %.c
	$(CC) $(CPPFLAGs) $(DEFINEFLAG) $<
	$(CC) $(DEFINEFLAG) -E -o $@ $<

#--------------------------------------------------------------------------------------------------------------------------------------------- #
# Target: <file>.asm
# Prerequisites: the .c file
# Output: the .asm file whether from the .c file or the object file
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
%.asm : %.c
	$(CC) $(DEFINEFLAG) $(CFLAGS) -S $<
	objdump $(OBJS) -D


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# Target: <file>.o
# Prerequisites: the .c file
# Output: the .o file corresponding to the provided .c file
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
%.o : %.c
	$(CC) $(DEFINEFLAG) $(CFLAGS) -c $<

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# Target: compile-all
# Prerequisites: the source files
# Output: all source files are compiled but without linking and their corresponding .o files are generated
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
.PHONY: compile-all
compile-all: $(SOURCES)
#$(OBJS): $(SOURCES)
	$(CC) $(DEFINEFLAG) $(CFLAGS) -c $(SOURCES)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# Target: build
# Prerequisites: the main.out file
# Output: the final executable file after linking and a brief report regarding the application size
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
.PHONY: build
build: $(OUTS)
#main.out
# I've a question here, if I set the prerequisites to main.o instead of main.out, the process doesn't get finished ... also how can make compiles the files and generate the object files when they are not provided by user as prerequesites. How can make understand that it should generate the .o files from the .c files before proceeding?
$(OUTS): $(SOURCES)
	$(CC) $(DEFINEFLAG) $(CFLAGS) $(LDFLAGS) -o c1m2.out $^ 
	size c1m2.out

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# Target: clean
# Prerequisites: None
# Output: all generated file are removed and the directory is cleaned for a new build
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
.PHONY: clean
clean:
#rm -f $(OBJS) main.out $(ASMS) $(PPS) $(MAPS)
	rm -f *.i *.d *.map *.s *.out *.o
