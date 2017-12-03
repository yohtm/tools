import subprocess


def set_iso(iso_conf):
    sing_shot = subprocess.Popen(["gphoto2", "--set-config", "iso={}".format(iso_conf)])
    sing_shot.communicate()


def set_shutterspeed(shutter_speed_conf):
    sing_shot = subprocess.Popen(["gphoto2", "--set-config", "shutterspeed={}".format(shutter_speed_conf)])
    sing_shot.communicate()


def single_shot():
    sing_shot = subprocess.Popen(["gphoto2", "--set-config", "capturemode=0"])
    sing_shot.communicate()
    sing_shot = subprocess.Popen(["gphoto2", "--capture-image-and-download", "--no-keep"])
    sing_shot.communicate()


def burst_shot(count):
    burst = subprocess.Popen(["gphoto2", "--set-config", "burstnumber={}".format(count)])
    burst.communicate()
    burst = subprocess.Popen(["gphoto2", "--set-config", "capturemode=1"])
    burst.communicate()
    burst = subprocess.Popen(["gphoto2", "--capture-image"])
    burst.communicate()
    burst = subprocess.Popen(["gphoto2", "--get-files", "1-{}".format(count)])
    burst.communicate()
    burst = subprocess.Popen(["gphoto2", "--delete-files", "1-{}".format(count)])


class FlashMode(object):
    def __init__(self):
        pass

    def auto(self):
        flash = subprocess.Popen(["gphoto2", "--set-config", "flashmode=2"])
        flash.communicate()

    def red_eye_auto(self):
        flash = subprocess.Popen(["gphoto2", "--set-config", "flashmode=1"])
        flash.communicate()

    def off(self):
        flash = subprocess.Popen(["gphoto2", "--set-config", "flashmode=0"])
        flash.communicate()


class ImageQuality(object):
    def __init__(self):
        pass

    def JPEG_basic(self):
        qual = subprocess.Popen(["gphoto2", "--set-config", "imagequality=0"])
        qual.communicate()

    def JPEG_normal(self):
        qual = subprocess.Popen(["gphoto2", "--set-config", "imagequality=1"])
        qual.communicate()

    def JPEG_fine(self):
        qual = subprocess.Popen(["gphoto2", "--set-config", "imagequality=2"])
        qual.communicate()

    def NEF(self):
        qual = subprocess.Popen(["gphoto2", "--set-config", "imagequality=3"])
        qual.communicate()

    def NEF_and_basic(self):
        qual = subprocess.Popen(["gphoto2", "--set-config", "imagequality=4"])
        qual.communicate()


class ImageSize(object):
    def __init__(self):
        pass

    def large(self):
        size = subprocess.Popen(["gphoto2", "--set-config", "imagesize=0"])
        size.communicate()

    def medium(self):
        size = subprocess.Popen(["gphoto2", "--set-config", "imagesize=1"])
        size.communicate()

    def small(self):
        size = subprocess.Popen(["gphoto2", "--set-config", "imagesize=2"])
        size.communicate()