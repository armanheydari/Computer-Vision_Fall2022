import cv2
import numpy as np


criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((24*17, 3), np.float32)
objp[:, :2] = np.mgrid[0:24, 0:17].T.reshape(-1, 2)
objpoints, imgpoints = [], []


def calibrate_image(input_images, output_name, dest_image='images//img5.png', is_plot_corners=False):
    for img_path in input_images:
        objpoints.append(objp)

        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(gray_img, (24, 17), None)
        accurate_corners = cv2.cornerSubPix(gray_img, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(accurate_corners)

        if is_plot_corners:
            img = cv2.drawChessboardCorners(img, (24, 17), accurate_corners, ret)
            cv2.imwrite(output_name + '_corners.png', img)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray_img.shape[::-1], None, None)

    test_img = cv2.imread(dest_image)
    h, w = test_img.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
    dst = cv2.undistort(test_img, mtx, dist, None, newcameramtx)
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]
    cv2.imwrite(output_name+'.png', dst)


if __name__ == '__main__':
    calibrate_image(['images//img1.png'], 'calib1', is_plot_corners=True)
    calibrate_image(['images//img1.png', 'images//img2.png', 'images//img3.png', 'images//img4.png'], 'calib2')