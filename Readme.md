1. sudo apt-get update 
2. sudo apt-get upgrade -Y
3. sudo apt install git
  3.1 git config --global user.name "Robotics-Ro"
  3.2 git config --global user.email ro.taehyung.180761@roivy.net
4. install chrome browser by web browser
5. deb file install
   CUI - sudo apt install ./[install_file_name]
   GUI - right click
6. sudo apt install vim
7. vscode install with web browser
8. sudo apt install terminator
9. NVIDIA GRAPHIC CARD DRIVER INSTALL (nvidia-driver:515, CUDA:11.7, cuDnn : cuDNN v8.8.1 (March 8th, 2023))
    - $sudo lshw -c display
    - $sudo ubuntu-drivers devices
    - $sudo apt install nvidia-driver-515
    - $sudo apt apt-get install dkms nvidia-modprobe
    - $sudo apt update
    - $sudo apte upgrade
    - $sudo shutdown now
    - $sudo lshw -c display
    - $nvidia-smi
    - CUDA:11.7 Download
    - $wget https://developer.download.nvidia.com/compute/cuda/11.7.0/local_installers/cuda_11.7.0_515.43.04_linux.run
    - $sudo sh cuda_11.7.0_515.43.04_linux.run
    - $sudo sh -c "echo 'export PATH=$PATH:/usr/local/cuda-11.7/bin'>> /etc/profile"
    - $sudo sh -c "echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-11.7/
    - $sudo sh -c "echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-11.7/ lib64'>> /etc/profile"sudo sh -c "echo 'export         LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-11.7/

    - $sudo sh -c "echo 'export CUDARDIR=/usr/local/cuda-11.7'>> /etc/profile"
    - $source /etc/profile
    - $nvcc -V
    - cuDNN:8.8.1 Download - Yun Jong Lee do it.
    - tar realease
     $sudo cp cuda/include/cudnn* /usr/local/cuda/include
     $sudo cp cuda/lib/libcudnn* /usr/local/cuda/lib64
     $sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*
     $sudo ln -sf /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.8.1 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_train.so.8
     $sudo ln -sf /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8.8.1 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8
     $sudo ln -sf /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8.8.1 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8
     $sudo ln -sf /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.8.1 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8
     $sudo ln -sf /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_ops_train.so.8.8.1 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_ops_train.so.8
     $sudo ln -sf /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.8.1 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8
     $sudo ln -sf /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn.so.8.8.1 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn.so.8
     $sudo ldconfig
     $ldconfig -N -v $(sed 's/:/ /' <<< $LD_LIBRARY_PATH) 2>/dev/null | grep libcudnn


10. pip install --upgrade pip
11. pip install notebook
12. pip install tensorflow
