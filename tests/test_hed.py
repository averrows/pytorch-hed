import torchHED


def test_hed_on_sample():
    torchHED.process_img("./images/sample.png", "./images/torchHED.png")
