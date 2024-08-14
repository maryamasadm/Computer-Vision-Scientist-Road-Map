**Processoing Units

*CPU

The Central Processing Unit (CPU) is the primary component of a computer that acts as its “control center.” The CPU, also referred to as the “central” or “main” processor, is a complex set of electronic circuitry that runs the machine's operating system and apps. It responsible for carrying out the basic operations. 
CPU has small number of processing cores. 
It uses the sequential processing, it means single task or instructions is executed at a time, in a specific order or sequence. 
It is not good for parallel processing, low performance for graphic processing and matrix calculations.
It is good for computing task like browsing the web or editing the documents


*GPU

Graphics processing Units, it is a specialized processor that is designed to handel complex mathematical computations quickly. Can be used in video games, visual applications, scientific computations. 
They use thousands of processing cores
Parallel processing (execute many instructions simultaneously)
It has high speed and hi performance and efficiency
It is good for scientific computing tasks like training ML models
Main companies producing GPU are NVIDIA and AMD
There is special toolkit developed by NVIDIA called : CUDA

*CUDA

Compute Unified device architecture is a parallel computing platform and application programing interface (API) developed by Nvidia for its GPUs. To use Pytorch with CUDA you need to have NVIDIA GPU and CUDA toolkit installed on machine. Or you use google colab ! in colab you don’t have to install any GPU packages or have even the GPU, it only runs on web browsers.
But if you use other IDE, like Jupyter or Spyder, .. you need to make sure everything is there. 

How to use PyTorch on your PC ? 
1.	Install CUDA from here: https://developer.nvidia.com/cuda-downloads
2.	You can check out CUDA installation in command prompt with typing: nvidia-smi
You should see the version
3.	Install conda according to the PC, ex. For Windows 64 bit install the right package here: https://docs.anaconda.com/miniconda/
4.	In Anaconda Prompt create new conda environment : conda create –name pytorch
5.	Go to pytorch website and find the command line accordingly, ex:
conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia
6.	Add the CUDA path to ‘Environmental variable’ , system variable, path section: this path: Ex: C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6\bin


*TPU

*FPGA

