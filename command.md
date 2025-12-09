
# partition GPUs
srun --partition=a100_long --gres=gpu:2 --time=5-00:00:00 --mem=80G --cpus-per-task=8 --pty bash


srun --partition=a100_short --gres=gpu:2 --time=2-00:00:00 --mem=80G --cpus-per-task=8 --pty bash
srun --partition=a100_short --gres=gpu:1 --time=4:00:00 --mem=80G --cpus-per-task=8 --pty bash

# activate envs  need loaded conda
module load anaconda3/gpu/2023.09 || module load anaconda3/gpu/2022.10 || module load miniconda3/gpu/4.9.2

# 已经 module load anaconda3/gpu/2023.09 之后，运行：
eval "$(conda shell.bash hook)"

# 然后再激活你的 env：
conda activate /gpfs/scratch/pans03/conda_envs/unet3d


mkdir -p /gpfs/scratch/pans03/conda_envs

# (2) Create the environment *at a path* (-p = prefix)
conda create -p /gpfs/scratch/pans03/conda_envs/unet3d python=3.9 -y

# (3) Activate it using full path
conda activate /gpfs/scratch/pans03/conda_envs/unet3d