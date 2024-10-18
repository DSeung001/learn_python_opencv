import cv2

image = cv2.imread('like_lenna.png')
if image is not None:
    print("이미지를 읽어왔습니다.")
else:
    print("이미지를 읽어오지 못했습니다.")
print(f"변수 타입 :{type(image)}")

print(f"이미지 배열의 형태 : {image.shape}")
image_small = cv2.resize(image, (100, 100))
print(f"이미지 배열의 형태 : {image_small.shape}")
image_big = cv2.resize(image, dsize=None, fx=2, fy=2)
print(f"이미지 배열의 형태 : {image_big.shape}")
#  이거 책 내용보니깐 구글 코랩에서 지원하는 라이브러리를 무조건 쓰네
