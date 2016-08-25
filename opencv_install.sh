#! /bin/bash
# check cv2
OPENCVPATH=`sudo find / -name cv2.so | tail -1 | sed -e 's/\/cv2.so//g'` 2>/dev/null
echo $OPENCVPATH

if [ -z "$OPENCVPATH" ]; then
    # install dependencies
    sudo apt-get update
    sudo apt-get install -y build-essential
    sudo apt-get install -y cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev unzip
    sudo apt-get install -y python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
    sudo apt-get install -y qt4-dev-tools

    sudo apt-get -qq install libopencv-dev build-essential checkinstall cmake pkg-config yasm libjpeg-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libv4l-dev python-dev python-numpy libtbb-dev libqt4-dev libgtk2.0-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils

    # download opencv-3.1.0
    mkdir opencv
    cd opencv
    wget https://github.com/Itseez/opencv/archive/3.1.0.zip -O opencv-3.1.0.zip
    unzip opencv-3.1.0.zip

    cd opencv-3.1.0
    mkdir build
    cd build
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D WITH_V4L=ON -D WITH_QT=ON -D WITH_OPENGL=ON ..
    make -j $(nproc)
    sudo make install
fi
