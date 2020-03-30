FROM nytimes/blender:2.82-cpu-ubuntu18.04

LABEL Author="Jordan Matelsky <opensource@matelsky.com>"
LABEL Title="Blender3D with Animation Nodes"


# Download animation nodes:
RUN wget -O animation_nodes.zip https://github.com/JacquesLucke/animation_nodes/releases/download/v2.0/animation_nodes_v2_0_linux.zip

COPY _install_an.py .
# Install it:
RUN blender -b -P _install_an.py
