ARG PYTORCH="1.7.0"
ARG CUDA="11.0"
ARG CUDNN="8"

FROM pytorch/pytorch:${PYTORCH}-cuda${CUDA}-cudnn${CUDNN}-devel

ENV TORCH_CUDA_ARCH_LIST="6.0 6.1 7.0+PTX"
ENV TORCH_NVCC_FLAGS="-Xfatbin -compress-all"
ENV CMAKE_PREFIX_PATH="$(dirname $(which conda))/../"

RUN apt-get update && apt-get install -y git ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Install mmsegmentation
RUN conda clean --all

RUN pip install mmcv-full==latest+torch1.7.0+cu110 -f https://download.openmmlab.com/mmcv/dist/index.html
#RUN git clone https://github.com/open-mmlab/mmsegmenation.git /mmsegmentation
#WORKDIR /mmsegmentation
#RUN pip install -r requirements/build.txt
#RUN pip install --no-cache-dir -e .
