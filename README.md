# Assignment 8: Steganography

**Instructor:** Dr. Mukti Padhya  
**Date Assigned:** 4 Apr  
**Due Date:** 7 Apr, 23:59  
**Points:** 100  

---

## 📌 Description

Steganography is the practice of concealing a secret file, message, audio, or video inside another file format to ensure data confidentiality during transmission over insecure communication channels.  

This assignment demonstrates multiple practical approaches to steganography, including both command-line tools and custom code implementations.

---

## 🛠 Implementations

1. **Windows Commands**  
   - Using built-in Windows features to embed hidden data inside files.

2. **LSB (Least Significant Bit) Algorithm in C/Java/Python**  
   - Custom implementation of image steganography where the least significant bits of pixel data are modified to embed secret information.

3. **OpenPuff Tool**  
   - [OpenPuff Steganography Tool](https://embeddedsw.net/OpenPuff_Steganography_Home.html) for hiding and extracting data in multimedia files.

4. **Linux Environment – StegHide**  
   - [StegHide Tutorial](https://medium.com/@prem112/a-step-by-step-steganography-tutorial-with-steghide-730e5090ae57) for embedding and extracting data within image and audio files.

---

## 📂 Features

- Supports multiple platforms: **Windows** and **Linux**
- Implements both **manual coding** and **tool-based** steganography
- Capable of hiding **text**, **files**, **audio**, and **video**
- Demonstrates **LSB image steganography**
- Hands-on with **OpenPuff** and **StegHide**

---

## 🖼 Example Workflow (LSB Image Steganography in Python)

1. Choose a **cover image** (PNG/BMP recommended).  
2. Select the **secret text or file** to hide.  
3. Apply the **LSB algorithm** to modify pixel data.  
4. Save the new **stego-image**.  
5. Extract the hidden message from the stego-image.

---

## 📷 Diagram (Optional)

<p align="center">
  <img width="500" alt="Steganography Diagram" src="https://github.com/user-attachments/assets/example-image-id" />
</p>

---

## 📄 References

- [OpenPuff Official Website](https://embeddedsw.net/OpenPuff_Steganography_Home.html)  
- [StegHide Guide on Medium](https://medium.com/@prem112/a-step-by-step-steganography-tutorial-with-steghide-730e5090ae57)  
- LSB Algorithm resources from Python, Java, and C documentation

---

## 📜 License
This project is released under the MIT License.
