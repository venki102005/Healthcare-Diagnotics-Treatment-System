import numpy as np

# Define a dictionary of diseases and their corresponding symptoms
diseases = {
    "Common Cold": ["cough", "fever", "headache", "sore throat"],
    "Flu": ["cough", "fever", "fatigue", "body aches"],
    "Malaria": ["fever", "chills", "flu-like symptoms", "vomiting"]
}

# Define a dictionary of treatments for each disease
treatments = {
    "Common Cold": "Rest, hydration, and over-the-counter medications",
    "Flu": "Antiviral medications, rest, and hydration",
    "Malaria": "Antimalarial medications, rest, and hydration"
}

def diagnose_disease(symptoms):
    """
    Diagnose potential diseases based on patient symptoms.

    Args:
        symptoms (list): List of patient symptoms

    Returns:
        list: Potential diseases
    """
    potential_diseases = []
    for disease, disease_symptoms in diseases.items():
        if any(symptom in disease_symptoms for symptom in symptoms):
            potential_diseases.append(disease)
    return potential_diseases

def suggest_treatment(disease):
    """
    Suggest treatment for a given disease.

    Args:
        disease (str): Disease name

    Returns:
        str: Recommended treatment
    """
    return treatments.get(disease, "Unknown treatment")

def main():
    print("Healthcare Diagnostics and Treatment System")
    print("-" * 50)

    # Get patient symptoms
    symptoms = input("Enter patient symptoms (comma-separated): ")
    symptoms = [symptom.strip().lower() for symptom in symptoms.split(",")]

    # Diagnose potential diseases
    potential_diseases = diagnose_disease(symptoms)
    print("\nPotential diseases:")
    for disease in potential_diseases:
        print(f"- {disease}")

    # Suggest treatment for each potential disease
    for disease in potential_diseases:
        treatment = suggest_treatment(disease)
        print(f"\nTreatment for {disease}: {treatment}")

if __name__ == "__main__":
    main()

    
     
