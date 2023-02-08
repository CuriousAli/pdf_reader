from pyzbar.pyzbar import decode
import cv2


# Make one method to decode the barcode
def extract_barcode_data(image, display, value=3000):
    # read the image in numpy array using cv2
    img = cv2.imread(image)

    # Decode the barcode image
    detected_barcodes = decode(img)
    data = []
    # If not detected then print the message
    if not detected_barcodes:
        return None
    else:

        # Traverse through all the detected barcodes in image
        for barcode in detected_barcodes:

            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect

            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x - 30, y - 5),
                          (x + w + 40, y + h + 5),
                          (255, 0, 0), 2)

            if barcode.data == "":
                return None

            else:
                data.append((barcode.type, barcode.data))

    if display:
        # Temporary display the image, on default displaying time is 3000 ms
        cv2.imshow("Image", img)
        cv2.waitKey(value)
        cv2.destroyAllWindows()

    return data

