import fitz

from pyzbar.pyzbar import decode
import cv2

from path_holder import path


def save_pdf_file_as_image():
    '''Converting pdf file into image'''
    with fitz.open(path) as doc:
        page = doc.load_page(0)  # number of page
        zoom = 3    # zoom factor
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        output = "outfile.png"
        pix.save(output)
        return output


# Make one method to decode the barcode
def barcode_processing(image, display, value=3000):
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









