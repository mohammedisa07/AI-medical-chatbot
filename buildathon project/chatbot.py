import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a healthcare expert"}]

medical_keywords = ["symptoms", "diagnosis", "treatment", "medication", "health","prevent","cure","advice","facing","doctor","nurse","pain","medicine","first aid","Abdomen", "Abdominal aorta", "Abdominal cavity","composition","medical composition" ,"Abdominal pain", "Abrasion", "Abscess", "Abstinence", "ACE inhibitors", "Achalasia", "Acidosis", "Acne", "Acupuncture", "Acute", "Addiction", "Adenoids", "Adhesion", "Adrenal glands", "Aerobic exercise", "Aerosol", "Agonist", "AIDS", "Airway", "Alcoholism", "Allergen", "Allergic reaction", "Allergy", "Alzheimer's disease", "Amniocentesis", "Amputation", "Analgesic", "Anaphylaxis", "Anemia", "Anesthesia", "Aneurysm", "Angioplasty", "Anorexia", "Antibiotic", "Antidepressant", "Antigen", "Antihistamine", "Antioxidant", "Antiviral", "Anxiety", "Aorta", "Aortic valve", "Apnea", "Arrhythmia", "Artery", "Arthritis", "Aspirin", "Asthma", "Atherectomy", "Atherosclerosis", "Atrophy", "Auscultation", "Autoimmune", "Autopsy", "Avulsion", "Bacteria", "Benign", "Beta blocker", "Biopsy", "Bipolar disorder", "Bladder", "Blood clot", "Blood pressure", "Bone marrow", "Brachial artery", "Bronchitis", "Bronchodilator", "Cancer", "Carcinogen", "Cardiac arrest", "Cardiologist", "Cardiology", "Cardiovascular", "Cataract", "Catheter", "Cellulitis", "Cerebral", "Cerebral palsy", "Cervix", "Chemotherapy", "Cholesterol", "Chronic", "Circulation", "Cirrhosis", "Clot", "Coccyx", "Colon", "Colostomy", "Coma", "Common cold", "Computed tomography", "Concussion", "Congenital", "Congestion", "Constipation", "Contagious", "Contraception", "Cornea", "Coronary", "Cough", "Cyst", "Cystic fibrosis", "Cytology", "Dehydration", "Dementia", "Dental", "Depression", "Diabetes", "Diagnosis", "Dialysis", "Diaphragm", "Diarrhea", "Dietician", "Dilation", "Disability", "Dislocation", "Diuretic", "Diverticulitis", "DNA", "Doctor", "Dopamine", "Down syndrome", "Drug", "Dyspnea", "Eardrum", "Ebola", "Echocardiogram", "Eczema", "Edema", "Electrocardiogram", "Embolism", "Emergency", "Emphysema", "Endocrine", "Endoscopy", "Epidermis", "Epiglottis", "Epilepsy", "Erythrocyte", "Esophagus", "Etiology", "Euthanasia", "Exacerbation", "Excision", "Exercise", "Fever", "Fibrillation", "Fibromyalgia", "Flu", "Fracture", "Gallbladder", "Gastroenterology", "Gene", "Genetic", "Genital", "Geriatrics", "Germ", "Glaucoma", "Gonorrhea", "Gynecologist", "Hallucination", "Hay fever", "Headache", "Hearing", "Heart attack", "Heart failure", "Heartburn", "Hematoma", "Hematuria", "Hemoglobin", "Hemophilia", "Hemorrhage", "Hepatitis", "Hereditary", "Hernia", "Herpes", "Hormone", "Human papillomavirus", "Hypertension", "Hyperventilation", "Hypothermia", "Hypoxia", "Immune", "Immunization", "Impotence", "Incontinence", "Infarction", "Infertility", "Inflammation", "Influenza", "Inhalation", "Insomnia", "Intensive care", "Intestine", "Jaundice", "Joint", "Kidney", "Laboratory", "Larynx", "Lesion", "Leukemia", "Ligament", "Liver", "Lung", "Lymph nodes", "Malaria", "Mammogram", "Mastectomy", "Measles", "Melanoma", "Meningitis", "Menopause", "Mental health", "Migraine", "Mitochondria", "Mucus", "Multiple sclerosis", "Muscle", "Narcotic", "Nausea", "Nephrologist", "Nephron", "Neurologist", "Neurology", "Neuron", "Neurosurgery", "Nodule", "Noninvasive", "Nurse", "Nutrition", "Obesity", "Obstetrics", "Oncologist", "Oncology", "Ophthalmologist", "Optometrist", "Organ", "Orthopedic", "Osteoporosis", "Ovary", "Pacemaker", "Pain", "Palliative", "Pancreas", "Panic disorder", "Paralysis", "Parasite", "Pathogen", "Pathology", "Pneumonia", "Polyp", "Pregnancy", "Prescription", "Prognosis", "Prostate", "Psychiatrist", "Psychology", "Radiation", "Radiology", "Rehabilitation", "Respiration", "Rheumatologist", "Rheumatology", "Saliva", "Schizophrenia", "Seizure", "Sepsis", "Surgery", "Symptoms", "Syndrome", "Tendon", "Therapy", "Thyroid", "Tissue", "Toxic", "Toxin", "Transplant", "Tumor", "Ulcer", "Umbilical cord", "Urethra", "Urologist", "Uterus", "Vaccination", "Virus", "Vital signs", "Vitamins", "Wart", "Weight loss", "Wound", "X-ray","Abdomen", "Abdominal pain", "Acidity", "Ache", "Allergies", "Appointment", "Bleeding", "Body ache", "BP (Blood Pressure)", "Chest pain", "Cold", "Cough", "Diabetes", "Diet", "Doctor", "Fever", "Headache", "Heartbeat", "Infection", "Injection", "Medicine", "Nausea", "Pain", "Prescription", "Stomachache", "Surgery", "Swelling", "Test", "Throat", "Vomit","Back", "Chest", "Eyes", "Face", "Feet", "Hands", "Legs", "Neck", "Stomach","Cardiologist", "Dentist", "Dermatologist", "ENT Specialist", "Gynecologist", "Neurologist", "Orthopedic", "Pediatrician", "Psychiatrist", "Surgeon","Antibiotics", "Antacids", "Cough syrup", "Painkillers", "Tablet", "Medicine","Blood test", "CT scan", "MRI", "X-ray""Acne", "Constipation", "Diarrhea", "Dizziness", "Fainting", "Indigestion", "Insomnia", "Itching", "Numbness", "Rash", "Shortness of breath", "Sore throat", "Vomiting","Appointment", "Emergency", "Health", "Hospital", "Insurance", "Patient", "Pharmacy", "Treatment", "Weight","sneezing","itching","ulser","poison","food","saliva","hair loss","running nose","nose","mouth","stomach","sweating","liver","buldge","yellow","red","eyes","ears","pink","White","ceptic","Blocked","mole","breathing","throat","down","slip","well","neck","sprain","skin","color","loss","digest","motion","sick","tumour","pimples","darkspots","fungus","dark","dry","wet","hygenic","genetics","nerves","veins","foot","chicken pocks","nausea","trauma","fire","burn","mental","physical","brain","touch","feel","smell","bite","sense","bug","pocks","bee","ulcer","dehydration","drink","sleep","laziness","tired","peace","dullness","weak","fat","thin","obesity","starve","starvation","scratch","pressure","smoking","drinking","overthinking","depression","hallucination","hallucinate","food","foods","minerals","protein","carbohydrates","snoring","nail","headache","head pain","prostrate cancer","wheezing","stroke","Oncology", "Tumor", "Malignant", "Benign", "Metastasis", "Chemotherapy", "Radiation", "Biopsy", "Carcinoma", "Sarcoma", "Leukemia", "Lymphoma", "Melanoma", "Genetic Mutation", "Cancerous", "Oncogene", "Tumor Marker", "Remission", "Palliative Care", "Screening","Cardiovascular", "Coronary Artery Disease", "Heart Attack", "Myocardial Infarction", "Arrhythmia", "Atherosclerosis", "Hypertension", "Congestive Heart Failure", "Valvular Disease", "Angina", "Stent", "Bypass Surgery", "Pacemaker", "Echocardiogram", "EKG/ECG", "Cardiologist", "Cholesterol", "Catheterization", "Risk Factor","Dermatology", "Eczema", "Psoriasis", "Acne", "Melanoma", "Dermatitis", "Rosacea", "Hives", "Warts", "Skin Cancer", "Vitiligo", "Scabies", "Ringworm", "Moles", "Fungal Infection", "Sunburn", "Lupus", "Pruritus", "Pigmentation","Pulmonology", "Asthma", "Chronic Obstructive Pulmonary Disease (COPD)", "Lung Cancer", "Pneumonia", "Bronchitis", "Emphysema", "Fibrosis", "Respiratory Distress Syndrome", "Tuberculosis", "Pulmonary Function Test", "Bronchoscopy", "Oxygen Therapy", "Smoking Cessation", "Lung Transplant", "Spirometry", "Cough", "Wheezing","Endocrinology", "Diabetes", "Thyroid Disorders", "Hyperthyroidism", "Hypothyroidism", "Adrenal Insufficiency", "Polycystic Ovary Syndrome (PCOS)", "Cushing's Syndrome", "Graves' Disease", "Hormone Replacement Therapy (HRT)", "Insulin", "Pituitary Gland", "Hormone Imbalance", "Growth Hormone Deficiency", "Metabolism", "Androgen", "Estrogen", "Progesterone","Sleep Medicine", "Insomnia", "Sleep Apnea", "Narcolepsy", "Restless Leg Syndrome", "Circadian Rhythm Disorder", "Parasomnia", "Snoring", "Sleep Deprivation", "Polysomnography", "Melatonin", "CPAP (Continuous Positive Airway Pressure)", "Sleep Hygiene", "Sleep Cycle", "REM Sleep", "Sleep Disorder Clinic", "Sleep Study", "Sleeping Pills","Chemical Exposure", "Toxicity", "Chemical Sensitivity", "Occupational Disease", "Environmental Illness", "Chemical Allergy", "Chemical Burn", "Poisoning", "Carcinogenic", "Chemical Hazard", "Chemical Intoxication", "Chemical Contaminant"

]

def is_safe(text):
    # Check if the text contains any medical keywords
    for keyword in medical_keywords:
        if keyword in text.lower():
            return True
    return False

def CustomChatGPT(Queries):
    if not is_safe(Queries):
        return "I'm sorry, but I can only provide medical information."
    
    messages.append({"role": "user", "content": Queries})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    
    if not is_safe(ChatGPT_reply):
        return "I'm sorry, but I can only provide medical information."
    
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

def clear_messages():
    global messages
    messages = [{"role": "system", "content": "You are a AI doctor"}]

interface = gradio.Interface(
    fn=CustomChatGPT,
    inputs="text",
    outputs="text",
    title="AI Healthcare Bot",  # Change the title
    layout="vertical",
    theme="huggingface",
    examples=[
        ["What are the symptoms of COVID-19?"],
        ["How can I prevent heart disease?"],
    ],
    buttons=[
        gradio.Button("Submit"),
        gradio.Button("Clear", onclick=clear_messages),
        gradio.Button("Flag"),
        gradio.Button("Share"),
    ],
    footer="Powered by OpenAI",
)

interface.launch(share=True)
