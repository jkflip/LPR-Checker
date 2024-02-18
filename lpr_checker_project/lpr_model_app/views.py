from django.shortcuts import render
from django.http import HttpResponse

import easyocr
import cv2
from dataclasses import dataclass, asdict
import asyncio
from .forms import ImageUploadForm


@dataclass(frozen=True)
class OcrResult:
    bbox: tuple
    license_plate: str
    confidence: float


def transform_result(result: OcrResult):
    bbox, license_plate, confidence = result
    result = OcrResult(
        bbox=bbox,
        license_plate=license_plate,
        confidence=confidence,
    )
    return result


# def predict(request, image: str):
#     reader = easyocr.Reader(["en"])

#     # Checks if the image exists
#     if not image:
#         return "No image found"
#     else:
#         with open(image, "rb") as f:
#             image = f.read()

#     ocr_result = reader.readtext(image)
#     results = list(map(transform_result, ocr_result))
#     return dataclasses.asdict(results)


def perform_prediction(image):
    reader = easyocr.Reader(["en"])

    # Checks if the image exists
    if not image:
        return "No image found"
    else:
        image = image.read()

    print("test")
    ocr_result = reader.readtext(image)
    print(f"ocr_result: {ocr_result}")
    results = list(map(transform_result, ocr_result))
    print(f"results={results}")
    # return asdict(results)  #! Some error related to asdict (feb 11)
    return [asdict(result) for result in results]


def predict(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get("image")
            result = perform_prediction(image)
            return HttpResponse("Prediction: " + str(result))
    else:
        form = ImageUploadForm()

    return render(request, "predict.html", {"form": form})
