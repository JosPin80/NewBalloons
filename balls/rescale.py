import cv2 as cv

img = cv.imread('read_photo/sonnik-govoryaschiy-kot.jpg')
cv.imshow('Cat', img)



def rescaleFrame(frame, scale=0.75):
    # images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)


def changeRes(width, height):
    # Live Video
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture(0)

# while True:
#     isTrue, frame = capture.read()
#
#     frame_resized = rescaleFrame(frame, scale=.2)
#
#     cv.imshow('Video', frame)
#     cv.imshow('Video Resized', frame_resized)
#
#     cv.imshow('Video', frame)
#
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
#
# capture.release()
# cv.destroyAllWindows()


cv.waitKey(0)
