import cv2
import os


def getVideoFootage(videoPath):
    video_stream = cv2.VideoCapture(videoPath)

    count = 0
    frames = []
    success, frame = video_stream.read()  # gets the first frame
    while success:
        frames.append(frame)
        success, frame = video_stream.read()  # gets every consecutive frame
        count += 1

    video_stream.release()

    return frames


if __name__ == "__main__":
    frameCount = 0

    os.chdir("D:\Documents\Andrew uni\Thesis")
    for video in os.listdir():
        if ".mp4" in video:
            frames = getVideoFootage(video)
            video = video[:-4]
            if not os.path.exists(video):
                os.mkdir(video)
            for i in range(len(frames)):
                cv2.imwrite(video + '/' + video + '_' + str(i) + ".png", frames[i])
                frameCount += 1
            print("Video " + video + " complete")
    print(str(frameCount) + " images generated")
