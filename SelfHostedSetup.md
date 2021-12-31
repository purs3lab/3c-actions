## Setting up machine for self-hosting
The following steps are verified on `ubuntu 20.04` machine.
### Install dependencies
#### Packages
These are the packages required to build our benchmarks.
```
sudo apt-get update
sudo apt-get install libboost-all-dev git python cmake build-essential wget tar ninja-build liblzma-dev libreadline-dev libvorbis-dev libxslt1-dev
```
#### Install Bear
We use `bear` to capture the build commands. The following steps install bear from its github repo.
```
git clone https://github.com/rizsotto/Bear.git ~/bear
cd ~/bear
git pull
git checkout -f 75ff7f561652509ec9b34095881fdb6c4a56c9e0
mkdir build
cd build
cmake ..
sudo make install
```

### Setup benchmarks
In this step, we will setup the benchmarks on the machine so that our workflows will find it.
 
 Download https://github.com/mwhicks1/papers/blob/revision/checkedc-benchmarks-20211208.tar.gz to the machine.

#### Setting up benchmarks folder
```
sudo -s
# mkdir /home/github
# chmod -R 777 /home/github
# exit
```
#### Extracting benchmarks archive
```
tar -xf <downloaded tar.gz> -C /home/github/
```
 
### Installing GitHub Runner
Now you need to configure the machine to be a runner for the reporsitory workflows by follow instructions at: https://docs.github.com/en/actions/hosting-your-own-runners/adding-self-hosted-runners#adding-a-self-hosted-runner-to-a-repository

> Note: The GitHub will recognize the machine only when the `./run.sh` is running. So, it is important to ensure that the script is always running. One way to do this would be to execute using no hangup, i.e., `nohup ./run.sh > /dev/null 2>&1 &`. So that the GitHub runner will continue to run even when you logout of the machine.


Thats it. You machine is all ready and configured as self-hosted runner. You should be able to run the workflows from the repository page.
