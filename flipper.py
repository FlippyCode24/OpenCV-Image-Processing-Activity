import cv2 as cv
import numpy as np

# Global Variables
GRAYSCALE = cv.COLOR_BGR2GRAY
HSV = cv.COLOR_BGR2HSV
LAB = cv.COLOR_BGR2LAB
RGB = cv.COLOR_BGR2RGB

LOW = 25
MEDIUM = 50
HIGH = 100

def color_convert(image_path: str, type:int) -> None:
    img: cv.MatLike = cv.imread(image_path)

    img_convert = cv.cvtColor(img, type)

    img_name: str = image_path.split('/')[1].split('.')[0] + 'Converted'
    cv.imshow(img_name, img_convert)
    cv.waitKey(0)


def image_translate(image_path: str, x: int, y: int) -> None:
    img = cv.imread(image_path)

    trans_mat: np.float32 = np.float32([[1,0,x], [0,1,y]])
    dimensions: tuple[int, int] = (img.shape[1], img.shape[0])
    shifted_img = cv.warpAffine(img, trans_mat, dimensions)

    img_name: str = image_path.split('/')[1].split('.')[0] + f' {x} x-Shifted and {y} y-Shifted'
    cv.imshow(img_name, shifted_img)
    cv.waitKey(0)

def image_rotate(image_path, angle: int) -> None:
    img = cv.imread(image_path)
    (height, width) = img.shape[:2]
    rotPoint = (width//2, height//2)

    rot_mat = cv.getRotationMatrix2D(rotPoint, angle=angle, scale=1.0)
    dimensions = (width, height)
    rotated_img = cv.warpAffine(img, rot_mat, dimensions)

    img_name = image_path.split('/')[1].split('.')[0] + f' {angle} degrees Rotated'
    cv.imshow(img_name, rotated_img)
    cv.waitKey(0)

def image_blur(image_path: str, intensity: int) -> None:
    img = cv.imread(image_path)
    kernel_size: tuple[int, int] = (intensity, intensity)
    blur_img = cv.blur(img, kernel_size)

    img_name = image_path.split('/')[1].split('.')[0] + f' {intensity}% blurred'
    cv.imshow(img_name, blur_img)
    cv.waitKey(0)



