import os, re, sys, time, errno, configparser
import cv2


def save_all_frames(video_path, dir_path, basename, ext='png'):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)
    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            return


def main():
    config_ini = configparser.ConfigParser()
    config_filepath = 'config.ini'
    if not os.path.exists(config_filepath):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_filepath)
    config_ini.read(config_filepath, encoding='utf-8')
    config_convert = config_ini['CONVERT_SAMPLE']

    video_path = config_convert.get('VIDEO_PATH')
    dir_path = config_convert.get('DIR_PATH')
    basename = config_convert.get('BASENAME')
    save_all_frames(video_path, dir_path, basename)


if __name__ == '__main__':
    main()
