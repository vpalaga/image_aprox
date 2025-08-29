from skimage.metrics import structural_similarity as ssim
import cv2

# Load images in grayscale
def compare(img1, img2) -> float:

    score, diff = ssim(img1, img2, full=True)
    """
    try:
        score, diff = ssim(img1, img2, full=True)
    except ValueError:  # resize only if needed
        img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
        score, diff = ssim(img1, img2_resized, full=True)
    

    if __name__ == "__main__":
        if score == 1.0:
            print("Images are identical")
        else:
            print("Images are different")
    """

    return score


if __name__ == "__main__":
    img1t = cv2.imread("input_img.jpg", cv2.IMREAD_GRAYSCALE)
    img2t = cv2.imread("input_img2.jpg", cv2.IMREAD_GRAYSCALE)
    compare(img1t, img2t)