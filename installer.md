# Packages Installer for this Project

## List of the Packages
`face_recognition`
`dlib`
`numpy`
`Pillow`
`OpenCV-python`
`cmake`

## How to Install OpenCV (cv2)
Open your terminal and type:
`pip install opencv-python`

OpenCV would be downloaded.

## How to Install Cmake
Open your terminal and type:
`pip install cmake`

Your Package will be Downloaded.

## How to Install Face Recognition

To install this module, we need to have `dlib` `numpy` `Pillow`.

If you are lucky enough, then go in your terminal and type:
`pip install -r requirements.txt.`

Your packages would install.
Most of the time, people have a problem, including me.
And here is the solution.

### Step 1
You need to have a **64 Bit** Python Version. If you don't have it, you can install it from python.org/downloads.

### Step 2
You have to Download & Install Visual Studio for Windows Community Edition from here.
visualstudio.microsoft.com

### Step 3
After installing it, open the Visual Studio Installer. In the Workload Tab. Select the **Desktop Development with C++** Check the tick box and click Install.

The installation will start. I have a **Modify** option over there. Instead, you will have `Install`. As I have already installed it, I have a difference.

![Step 3](https://i.ibb.co/3zVQXsW/Step3.png)

Don't get us wrong. C++ is required to recognize the face using Python. `DLIB` library requires C++. Python is made of C++.

### Step 4

After you click Install Button, the installation starts and completes according to your Internet Speed. After the Installation, Visual Studio will be installed.

### Step 5

Open Visual Studio. The Sign-In screen will show up. You can click do it later. After that, choose your settings and preferences and click next till you get to the Splash Screen.

* After that, click `New Project` at the bottom
* Then, `Empty C++ Project` and click `Next`
* Next, Give the Project Name as `FaceRecognition.`
* After the project is done. Close Visual Studio.

### Step 6

On Desktop or somewhere, make a Folder `recognition`.

github.com/ageitgey/face_recognition/archive/refs/heads/master.zip

Download this `.zip` file and **unzip** it.

### Step 7

Now go to the **unzipped folder** and open the terminal there. 
And type:
`python setup.py install`
and hit **Enter**

* Make Sure that you install `cmake` before doing this

* Trust me, this will take much time, but it will install everything. Just wait. You can run this and go out cycling with your friends.
* Till you come back, it will be installed successfully.
<br><br>
**Help Reference**: youtu.be/xaDJ5xnc8dc

We have used this as a reference with some modifications, so it works perfectly, but you can still watch him if you face errors with us or want to give him credit.