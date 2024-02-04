# Token Graphs

## Environment

This project utilizes [SageMath](https://www.sagemath.org/) for various tasks. To get started, it's essential to ensure that all the necessary dependencies are installed. Below, we'll guide you through the installation process using [Anaconda 3](https://www.anaconda.com/) and [Mamba](https://mamba.readthedocs.io/en/latest/).

### Installing Dependencies

1. **Anaconda 3:**
   - Download and install Anaconda 3 from [this link](https://www.anaconda.com/).
   - Follow the instructions on the download page for the appropriate installation based on your operating system.

2. **Mamba:**

   To install Mamba, you can run the following command in your terminal:
     ```
     curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh
     sh Mambaforge-$(uname)-$(uname -m).sh
     ```
     Follow the on-screen instructions to complete the installation.

#### **Environment Setup:**

   After resolving the dependencies, it's time to create the environment. Execute the following command in your terminal:

     ```
     mamba create -p /home/{youruser}/anaconda3/envs/sage sage sage python=3.11
     ```

#### **Activate the Environment:**

   Once the environment is created, activate it using the following command:

     ```
     conda activate /home/{youruser}/anaconda3/envs/sage
     ```
#### **Verify SageMath Installation:**
   
   You can check that SageMath is installed in the environment with the following command:
   
     ```
     sage --version
     ```

Make sure you use the created Sage environment as you interpret it.
