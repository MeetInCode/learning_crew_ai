# Setting Up a Conda Environment and Installing Dependencies

This guide provides step-by-step instructions on how to create a Conda environment and install dependencies from a `requirements.txt` file.

## Prerequisites
- Ensure that Anaconda or Miniconda is installed on your system.
- Have the `requirements.txt` file ready with the necessary dependencies.

## Steps to Create and Set Up the Conda Environment

### 1. Open Terminal or Command Prompt

### 2. Create a New Conda Environment
Run the following command to create a new Conda environment. Replace `venv` with your preferred environment path:

```sh
conda create -p venv python==3.10
```

### 3. Activate the Conda Environment

```sh
conda activate ./venv
```

### 4. Install Dependencies from `requirements.txt`

If your `requirements.txt` file contains packages to install, use the following command:

```sh
pip install -r requirements.txt
```

### 5. Verify Installation
To ensure that all dependencies are installed correctly, run:

```sh
pip list
```

### 6. Deactivating the Conda Environment
When you are done using the environment, deactivate it with:

```sh
conda deactivate
```

### 7. Removing the Conda Environment (Optional)
If you no longer need the environment, you can remove it with:

```sh
conda remove -p venv --all
```

## Additional Notes
- If you need to update dependencies, modify `requirements.txt` and re-run `pip install -r requirements.txt`.
- Always activate the environment before running your Python projects to ensure dependencies load correctly.

This completes the setup of your Conda environment!

