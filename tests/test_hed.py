import torchHED


def test_hed_on_sample():
    torchHED.process_img("./images/sample.png", "./images/torchHED.png")


def test_hed_on_different_imgs():
    torchHED.process_folder("./tests/test_imgs", "./tests/tests_imgs_out")
