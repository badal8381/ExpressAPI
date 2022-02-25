from PIL import Image
import img2pdf


def png2jpg(img, id):
    jpg_path = f'media/img/temp/{id}.jpg'
    img_png = Image.open(img)

    img_png.save(jpg_path)
    return jpg_path

def jpg2png(img, id):
    png_path = f'media/img/temp/{id}.png'
    img_jpg = Image.open(img)

    img_jpg.save(png_path)
    return png_path


def image2pdf(img, id):
    pdf_path = f'media/img/temp/{id}.pdf'
    
    image = Image.open(img)
    
    # converting into chunks using img2pdf
    pdf_bytes = img2pdf.convert(image.filename)
    
    # opening or creating pdf file
    file = open(pdf_path, "wb")
    
    # writing pdf files with chunks
    file.write(pdf_bytes)
    
    # closing image file
    image.close()
    
    # closing pdf file
    file.close()

    return pdf_path



