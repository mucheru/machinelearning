{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19b5a59f-0d36-4ee8-9238-7cf967f31a40",
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip show opencv-python matplotlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "efe6ed3d-4ac1-4259-a892-9326144fc67d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "from matplotlib import pyplot as plt\n",
    "\n",
    "# Load the image\n",
    "imgfile = \"/home/steve/Downloads/Hooded_mountain_tanager_Buthraupis_montana_cucullata_Caldas-1024x683.jpg\"\n",
    "img = cv2.imread(imgfile, cv2.IMREAD_COLOR)\n",
    "\n",
    "# Convert the color channels from BGR to RGB\n",
    "img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)\n",
    "\n",
    "# Display the image using matplotlib\n",
    "plt.imshow(img_rgb)\n",
    "plt.axis('off')  # Turn off axis labels\n",
    "plt.show()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53ad7fe8-b679-4a5e-97f3-346d03cae391",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fef0c2ca-d2e9-4252-8204-ada6f4627c2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "cropped = img[y0:y1, x0:x1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "29a851a3-164a-42d5-b1e3-50bfebcbd702",
   "metadata": {},
   "outputs": [],
   "source": [
    "resized = cv2.resize(cropped, dsize=target_dim, interpolation=cv2.INTER_LINEAR)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73d894bd-0b05-4ca9-b075-c30736dc959f",
   "metadata": {},
   "outputs": [],
   "source": [
    "imgfile = \"/home/steve/Downloads/Hooded_mountain_tanager_Buthraupis_montana_cucullata_Caldas-1024x683.jpg\"\n",
    "video_dim = (1280, 720)\n",
    "fps = 25\n",
    "duration = 2.0\n",
    "start_center = (0.4, 0.6)\n",
    "end_center = (0.5, 0.5)\n",
    "start_scale = 0.7\n",
    "end_scale = 1.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7b075dcc-780f-45f3-a13e-141e03062661",
   "metadata": {},
   "outputs": [],
   "source": [
    "def crop(img, x, y, w, h):\n",
    "    x0, y0 = max(0, x-w//2), max(0, y-h//2)\n",
    "    x1, y1 = x0+w, y0+h\n",
    "    return img[y0:y1, x0:x1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b5de127-d234-4c4e-aef9-4cf5d48b777c",
   "metadata": {},
   "outputs": [],
   "source": [
    "rx = end_center[0]*alpha + start_center[0]*(1-alpha)\n",
    "ry = end_center[1]*alpha + start_center[1]*(1-alpha)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df4ca2c9-94aa-4a2f-8426-7b11e26384d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "orig_shape = img.shape[:2]\n",
    "\n",
    "if orig_shape[1]/orig_shape[0] > video_dim[0]/video_dim[1]:\n",
    "    h = int(orig_shape[0]*scale)\n",
    "    w = int(h * video_dim[0] / video_dim[1])\n",
    "else:\n",
    "    w = int(orig_shape[1]*scale)\n",
    "    h = int(w * video_dim[1] / video_dim[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ac0a72f-ffbc-4c77-9839-9f04e2685637",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "\n",
    "imgfile = \"/home/steve/Downloads/Hooded_mountain_tanager_Buthraupis_montana_cucullata_Caldas-1024x683.jpg\"\n",
    "video_dim = (1280, 720)\n",
    "fps = 25\n",
    "duration = 2.0\n",
    "start_center = (0.4, 0.6)\n",
    "end_center = (0.5, 0.5)\n",
    "start_scale = 0.7\n",
    "end_scale = 1.0\n",
    "\n",
    "img = cv2.imread(imgfile, cv2.IMREAD_COLOR)\n",
    "orig_shape = img.shape[:2]\n",
    "\n",
    "def crop(img, x, y, w, h):\n",
    "    x0, y0 = max(0, x-w//2), max(0, y-h//2)\n",
    "    x1, y1 = x0+w, y0+h\n",
    "    return img[y0:y1, x0:x1]\n",
    "\n",
    "num_frames = int(fps * duration)\n",
    "frames = []\n",
    "for alpha in np.linspace(0, 1, num_frames):\n",
    "    rx = end_center[0]*alpha + start_center[0]*(1-alpha)\n",
    "    ry = end_center[1]*alpha + start_center[1]*(1-alpha)\n",
    "    x = int(orig_shape[1]*rx)\n",
    "    y = int(orig_shape[0]*ry)\n",
    "    scale = end_scale*alpha + start_scale*(1-alpha)\n",
    "    # determined how to crop based on the aspect ratio of width/height\n",
    "    if orig_shape[1]/orig_shape[0] > video_dim[0]/video_dim[1]:\n",
    "        h = int(orig_shape[0]*scale)\n",
    "        w = int(h * video_dim[0] / video_dim[1])\n",
    "    else:\n",
    "        w = int(orig_shape[1]*scale)\n",
    "        h = int(w * video_dim[1] / video_dim[0])\n",
    "    # crop, scale to video size, and save the frame\n",
    "    cropped = crop(img, x, y, w, h)\n",
    "    scaled = cv2.resize(cropped, dsize=video_dim, interpolation=cv2.INTER_LINEAR)\n",
    "    frames.append(scaled)\n",
    "\n",
    "# write to MP4 file\n",
    "vidwriter = cv2.VideoWriter(\"output.mp4\", cv2.VideoWriter_fourcc(*\"mp4v\"), fps, video_dim)\n",
    "for frame in frames:\n",
    "    vidwriter.write(frame)\n",
    "vidwriter.release()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6cd86465-5c62-4724-84b7-340524e4716e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
