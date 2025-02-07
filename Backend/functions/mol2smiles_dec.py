import os
import sys
import logging
import cv2
from rdkit import Chem, RDLogger
from DECIMER import predict_SMILES # Import SMILES prediction function from DECIMER.ai


# Suppress TensorFlow and CUDA logs (NOT WORKING AT THE MOMENT)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Reduce TensorFlow logs
logging.getLogger("tensorflow").setLevel(logging.ERROR)  # Suppress TensorFlow errors
RDLogger.DisableLog('rdApp.*')  # Suppress RDKit warnings

# Redirect stderr and stdout to silence CUDA messages (NOT WORKING AT THE MOMENT)
sys.stderr = open(os.devnull, 'w')  
sys.stdout = open(os.devnull, 'w')

def img_to_smiles_decimer(image):
    try:
        cv2.imwrite("tmp.png", image)  # Save the image
        return predict_SMILES("tmp.png")  # Predict the SMILES string
    except Exception:
        return ""

# Restore stdout to print the final result only
sys.stdout = sys.__stdout__

# Load image and print only the result
#mol2 = "strychnine_21."
#mol2 = "Englerin-A_312"
mol2 = "test2911"
img = cv2.imread("mol_images/"+mol2+".png")
if img is not None:
    print(f"\nThe SMILES code for {mol2} is:\n{img_to_smiles_decimer(img)}")
else:
    print("\nError: Image not found!")
