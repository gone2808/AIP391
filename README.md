# AIP391 - Fall 2021 - AI1503

## Group 5 - Contributors

- Ngô Quang Hải
- Lê Hoàng Phúc

### Project

- Research: We have researched several articles/documents on Automatic License Plate Recognition (ALPR) in order to find the way to solve our proplem by analyzing their approach. Here is the link to our summary and analysis on the documents we have found: [Literature review](https://docs.google.com/spreadsheets/d/1HVmVpj6bgk3F9iZ8Wj2Kq4thxJnLnx2NyqqMIDSWHoU/edit?usp=sharing)

### Parts of Project
- Detection:
    Finds potential license plate regions
- Binarization:
    Convert plate regions into black and white for better recognisation
- Character Analysis:
    Finds character-sized "blobs" in the plate regions
- Plate edges:
    Find edges/shape of license plate
- Deskew:
    Transforms the perspective to a straight-on view based on the ideal license plate size
- Chracter segmentation:
    Isolates and cleans up the characters so that they can be processed individualy
- OCR:
    Analyzes each character image and provides multiple possible letters
- Post processing:
    Creates a top n list of plate possilbilities based on OCR confidences