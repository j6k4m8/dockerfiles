FROM ubuntu:18.04

RUN apt update
RUN DEBIAN_FRONTEND=noninteractive apt -y install git cmake build-essential xorg openbox libx11-dev sudo gawk

RUN mkdir ~/blender-git
RUN cd ~/blender-git
WORKDIR blender-git
RUN git clone https://git.blender.org/blender.git
WORKDIR blender
RUN git submodule update --init --recursive
RUN git submodule foreach git checkout master
RUN git submodule foreach git pull --rebase origin master

# No-sudo because docker doesn't know about sudo
RUN ./build_files/build_environment/install_deps.sh
RUN make
