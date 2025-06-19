# ==== 1. Library ====
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ==== 2. Konfigurasi Aplikasi ====
st.set_page_config(page_title="Jaya Jaya Institut Dropout Prediction", layout="wide")

MODEL_PATH = 'model/gboost_model.joblib'
DATA_PATH = 'X_test.csv'

# ==== 3. Load Model dan Data ====
@st.cache_resource
def load_model(path):
    try:
        return joblib.load(path)
    except FileNotFoundError:
        st.error(f"Model tidak ditemukan di: {path}")
        return None

@st.cache_data
def load_data(path):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        st.error(f"Dataset tidak ditemukan di: {path}")
        return None

model = load_model(MODEL_PATH)
df_template = load_data(DATA_PATH)

if model is None or df_template is None:
    st.stop()

if 'Status' in df_template.columns:
    df_template = df_template.drop(columns=['Status'])

# ==== 4. Mapping Dictionary ====
MARITAL_STATUS = {
    "Single": 1,
    "Married": 2,
    "Widower": 3,
    "Divorced": 4,
    "Facto Union": 5,
    "Legally Separated": 6
}

APPLICATION_MODE = {
    "1st phase - general contingent": 1,
    "Ordinance No. 612/93": 2,
    "1st phase - special contingent (Azores Island)": 5,
    "Holders of other higher courses": 7,
    "Ordinance No. 854-B/99": 10,
    "International student (bachelor)": 15,
    "1st phase - special contingent (Madeira Island)": 16,
    "2nd phase - general contingent": 17,
    "3rd phase - general contingent": 18,
    "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
    "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
    "Over 23 years old": 39,
    "Transfer": 42,
    "Change of course": 43,
    "Technological specialization diploma holders": 44,
    "Change of institution/course": 51,
    "Short cycle diploma holders": 53,
    "Change of institution/course (International)": 57
}

COURSES = {
    "Biofuel Production Technologies": 33,
    "Animation and Multimedia Design": 171,
    "Social Service (evening attendance)": 8014,
    "Agronomy": 9003,
    "Communication Design": 9070,
    "Veterinary Nursing": 9085,
    "Informatics Engineering": 9119,
    "Equinculture": 9130,
    "Management": 9147,
    "Social Service": 9238,
    "Tourism": 9254,
    "Nursing": 9500,
    "Oral Hygiene": 9556,
    "Advertising and Marketing Management": 9670,
    "Journalism and Communication": 9773,
    "Basic Education": 9853,
    "Management (evening attendance)": 9991
}

PREVIOUS_QUALIFICATION = {
    "Secondary education": 1,
    "Higher education - bachelor's degree": 2,
    "Higher education - degree": 3,
    "Higher education - master's": 4,
    "Higher education - doctorate": 5,
    "Frequency of higher education": 6,
    "12th year of schooling - not completed": 9,
    "11th year of schooling - not completed": 10,
    "Other - 11th year of schooling": 12,
    "10th year of schooling": 14,
    "10th year of schooling - not completed": 15,
    "Basic education 3rd cycle (9th/10th/11th year) or equiv.": 19,
    "Basic education 2nd cycle (6th/7th/8th year) or equiv.": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Professional higher technical course": 42,
    "Higher education - master (2nd cycle)": 43
}

NATIONALITY = {
    "Portuguese": 1,
    "German": 2,
    "Spanish": 6,
    "Italian": 11,
    "Dutch": 13,
    "English": 14,
    "Lithuanian": 17,
    "Angolan": 21,
    "Cape Verdean": 22,
    "Guinean": 24,
    "Mozambican": 25,
    "Santomean": 26,
    "Turkish": 32,
    "Brazilian": 41,
    "Romanian": 62,
    "Moldova (Republic of)": 100,
    "Mexican": 101,
    "Ukrainian": 103,
    "Russian": 105,
    "Cuban": 108,
    "Colombian": 109
}

PARENT_QUALIFICATION = {
    "Secondary Education - 12th Year of Schooling or Eq.": 1,
    "Higher Education - Bachelor's Degree": 2,
    "Higher Education - Degree": 3,
    "Higher Education - Master's": 4,
    "Higher Education - Doctorate": 5,
    "Frequency of Higher Education": 6,
    "12th Year of Schooling - Not Completed": 9,
    "11th Year of Schooling - Not Completed": 10,
    "7th Year (Old)": 11,
    "Other - 11th Year of Schooling": 12,
    "2nd year complementary high school course": 13,
    "10th Year of Schooling": 14,
    "General commerce course": 18,
    "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
    "Complementary High School Course": 20,
    "Technical-professional course": 22,
    "Complementary High School Course - not concluded": 25,
    "7th year of schooling": 26,
    "2nd cycle of the general high school course": 27,
    "9th Year of Schooling - Not Completed": 29,
    "8th year of schooling": 30,
    "General Course of Administration and Commerce": 31,
    "Supplementary Accounting and Administration": 33,
    "Unknown": 34,
    "Can't read or write": 35,
    "Can read without having a 4th year of schooling": 36,
    "Basic education 1st cycle (4th/5th year) or equiv.": 37,
    "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Specialized higher studies course": 41,
    "Professional higher technical course": 42,
    "Higher Education - Master (2nd cycle)": 43,
    "Higher Education - Doctorate (3rd cycle)": 44
}

PARENT_OCCUPATION = {
    "Student": 0,
    "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
    "Specialists in Intellectual and Scientific Activities": 2,
    "Intermediate Level Technicians and Professions": 3,
    "Administrative staff": 4,
    "Personal Services, Security and Safety Workers and Sellers": 5,
    "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
    "Skilled Workers in Industry, Construction and Craftsmen": 7,
    "Installation and Machine Operators and Assembly Workers": 8,
    "Unskilled Workers": 9,
    "Armed Forces Professions": 10,
    "Other Situation": 90,
    "(blank)": 99,
    "Health professionals": 122,
    "Teachers": 123,
    "Specialists in information and communication technologies (ICT)": 125,
    "Intermediate level science and engineering technicians and professions": 131,
    "Technicians and professionals, of intermediate level of health": 132,
    "Intermediate level technicians from legal, social, sports, cultural and similar services": 134,
    "Office workers, secretaries in general and data processing operators": 141,
    "Data, accounting, statistical, financial services and registry-related operators": 143,
    "Other administrative support staff": 144,
    "Personal service workers": 151,
    "Sellers": 152,
    "Personal care workers and the like": 153,
    "Skilled construction workers and the like, except electricians": 171,
    "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like": 173,
    "Workers in food processing, woodworking, clothing and other industries and crafts": 175,
    "Cleaning workers": 191,
    "Unskilled workers in agriculture, animal production, fisheries and forestry": 192,
    "Unskilled workers in extractive industry, construction, manufacturing and transport": 193,
    "Meal preparation assistants": 194
}

# ==== 5. UI Streamlit ====
st.title("Jaya Jaya Institut: Prediksi Potensi Dropout")
st.markdown("Aplikasi ini memprediksi potensi dropout siswa berdasarkan data akademik & demografis.")

# ==== 6. Input Form ====
user_inputs = {}

with st.expander("1. Informasi Pribadi Mahasiswa", expanded=True):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        user_inputs['Marital_status'] = st.selectbox("Status Pernikahan", list(MARITAL_STATUS.keys()))
        user_inputs['Application_mode'] = st.selectbox("Jalur Pendaftaran", list(APPLICATION_MODE.keys()))
        user_inputs['Application_order'] = st.selectbox("Prodi Saat Mendaftar", list(range(0, 10)))
    with col2:
        user_inputs['Course'] = st.selectbox("Prodi yang Diambil", list(COURSES.keys()))
        user_inputs['Daytime_evening_attendance'] = st.selectbox("Kelas Siang/Malam", ["Siang", "Malam"])
        user_inputs['Previous_qualification'] = st.selectbox("Pendidikan Terakhir", list(PREVIOUS_QUALIFICATION.keys()))
    with col3:
        user_inputs['Previous_qualification_grade'] = st.number_input("Nilai Pendidikan Terakhir", 0.0, 200.0, 120.0)
        user_inputs['Nacionality'] = st.selectbox("Kewarganegaraan", list(NATIONALITY.keys()))
        user_inputs['Admission_grade'] = st.number_input("Nilai Masuk", 0.0, 200.0, 120.0)
    with col4:
        user_inputs['Gender'] = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
        user_inputs['Age_at_enrollment'] = st.number_input("Usia Saat Mendaftar", 17, 60, 20)

with st.expander("2. Informasi Keluarga"):
    col1, col2 = st.columns(2)
    with col1:
        user_inputs['Mothers_qualification'] = st.selectbox("Pendidikan Ibu", list(PARENT_QUALIFICATION.keys()))
        user_inputs['Fathers_qualification'] = st.selectbox("Pendidikan Ayah", list(PARENT_QUALIFICATION.keys()))      
    with col2:
        user_inputs['Mothers_occupation'] = st.selectbox("Pekerjaan Ibu", list(PARENT_OCCUPATION.keys()))
        user_inputs['Fathers_occupation'] = st.selectbox("Pekerjaan Ayah", list(PARENT_OCCUPATION.keys()))
        
with st.expander("3. Informasi Demografi"):
    col1, col2 = st.columns(2)
    with col1:
        user_inputs['Displaced'] = st.selectbox("Rantau/Tidak", ["Tidak", "Ya"])
    with col2:
        user_inputs['International'] = st.selectbox("Mahasiswa Internasional", ["Tidak", "Ya"])

with st.expander("4. Status Finansial dan Kebutuhan Khusus"):
    col1, col2 = st.columns(2)
    with col1:
        user_inputs['Debtor'] = st.selectbox("Memiliki Tunggakan", ["Tidak", "Ya"])
        user_inputs['Tuition_fees_up_to_date'] = st.selectbox("Bayar Tepat Waktu", ["Tidak", "Ya"])
    with col2:
        user_inputs['Scholarship_holder'] = st.selectbox("Penerima Beasiswa", ["Tidak", "Ya"])    
        user_inputs['Educational_special_needs'] = st.selectbox("Kebutuhan Khusus", ["Tidak", "Ya"])

with st.expander("5. Status Akademik Semester 1"):
    col1, col2, col3 = st.columns(3)
    with col1:
        user_inputs['Curricular_units_1st_sem_credited'] = st.number_input("MK Semester 1 Dikreditkan", 0, 30, 0)
        user_inputs['Curricular_units_1st_sem_enrolled'] = st.number_input("MK Semester 1 Diambil", 0, 30, 6)
    with col2:
        user_inputs['Curricular_units_1st_sem_evaluations'] = st.number_input("MK Semester 1 Dikuti ujiannya", 0, 30, 5)
        user_inputs['Curricular_units_1st_sem_approved'] = st.number_input("MK Semester 1 Lulus", 0, 30, 5)
    with col3:
        user_inputs['Curricular_units_1st_sem_grade'] = st.number_input("Nilai Rata-rata Semester 1", 0.0, 20.0, 10.0)
        user_inputs['Curricular_units_1st_sem_without_evaluations'] = st.number_input("MK Semester 1 Tanpa Evaluasi", 0, 30, 0)

with st.expander("6. Akademik Semester 2"):
    col1, col2, col3 = st.columns(3)
    with col1:
        user_inputs['Curricular_units_2nd_sem_credited'] = st.number_input("MK Semester 2 Dikreditkan", 0, 30, 0)
        user_inputs['Curricular_units_2nd_sem_enrolled'] = st.number_input("MK Semester 2 Diambil", 0, 30, 6)
    with col2:
        user_inputs['Curricular_units_2nd_sem_evaluations'] = st.number_input("MK Semester 2 Dikuti ujiannya", 0, 30, 5)
        user_inputs['Curricular_units_2nd_sem_approved'] = st.number_input("MK Semester 2 Lulus", 0, 30, 5)
    with col3:
        user_inputs['Curricular_units_2nd_sem_grade'] = st.number_input("Nilai Rata-rata Semester 2", 0.0, 20.0, 10.0)
        user_inputs['Curricular_units_2nd_sem_without_evaluations'] = st.number_input("UK Semester 2 Tanpa Evaluasi", 0, 30, 0)

with st.expander("7. Indikator Ekonomi"):
    col1, col2, col3 = st.columns(3)
    with col1:
        user_inputs['Unemployment_rate'] = st.number_input("Tingkat Pengangguran (%)", 0.0, 30.0, 7.0)
    with col2:
        user_inputs['Inflation_rate'] = st.number_input("Tingkat Inflasi (%)", 0.0, 20.0, 3.0)
    with col3:
        user_inputs['GDP'] = st.number_input("GDP", 0.0, 200000.0, 100000.0)


# ==== 7. Tombol Prediksi ====
st.markdown("---")
if st.button("Prediksi Potensi Dropout"):

    # --- Konversi String ke Nilai Numerik ---
    user_inputs['Marital_status'] = MARITAL_STATUS[user_inputs['Marital_status']]
    user_inputs['Application_mode'] = APPLICATION_MODE[user_inputs['Application_mode']]
    user_inputs['Course'] = COURSES[user_inputs['Course']]
    user_inputs['Daytime_evening_attendance'] = 1 if user_inputs['Daytime_evening_attendance'] == "Siang" else 0
    user_inputs['Previous_qualification'] = PREVIOUS_QUALIFICATION[user_inputs['Previous_qualification']]
    user_inputs['Nacionality'] = NATIONALITY[user_inputs['Nacionality']]
    user_inputs['Mothers_qualification'] = PARENT_QUALIFICATION[user_inputs['Mothers_qualification']]
    user_inputs['Fathers_qualification'] = PARENT_QUALIFICATION[user_inputs['Fathers_qualification']]
    user_inputs['Mothers_occupation'] = PARENT_OCCUPATION[user_inputs['Mothers_occupation']]
    user_inputs['Fathers_occupation'] = PARENT_OCCUPATION[user_inputs['Fathers_occupation']]
    user_inputs['Gender'] = 1 if user_inputs['Gender'] == "Laki-laki" else 0
    user_inputs['Displaced'] = 1 if user_inputs['Displaced'] == "Ya" else 0
    user_inputs['International'] = 1 if user_inputs['International'] == "Ya" else 0
    user_inputs['Educational_special_needs'] = 1 if user_inputs['Educational_special_needs'] == "Ya" else 0
    user_inputs['Debtor'] = 1 if user_inputs['Debtor'] == "Ya" else 0
    user_inputs['Tuition_fees_up_to_date'] = 1 if user_inputs['Tuition_fees_up_to_date'] == "Ya" else 0
    user_inputs['Scholarship_holder'] = 1 if user_inputs['Scholarship_holder'] == "Ya" else 0

    # --- Siapkan DataFrame untuk Prediksi ---
    input_df = pd.DataFrame(index=[0], columns=df_template.columns)

    for col in df_template.columns:
        if col in ['Gender', 'Daytime_evening_attendance', 'Displaced', 'Educational_special_needs',
                   'Debtor', 'Tuition_fees_up_to_date', 'Scholarship_holder', 'International']:
            input_df[col] = df_template[col].mode()[0]
        elif df_template[col].dtype == 'object':
            input_df[col] = df_template[col].mode()[0]
        else:
            input_df[col] = df_template[col].median()

    for key, value in user_inputs.items():
        if key in input_df.columns:
            input_df[key] = value

    # --- Fitur Rekayasa ---
    input_df['Age_Squared'] = input_df['Age_at_enrollment'] ** 2
    input_df['Academic_Performance_1st_Sem'] = (
        (input_df['Curricular_units_1st_sem_grade'] * input_df['Curricular_units_1st_sem_approved']) /
        input_df['Curricular_units_1st_sem_enrolled']
        if input_df['Curricular_units_1st_sem_enrolled'].iloc[0] > 0 else 0.0
    )
    failed_courses_1st = input_df['Curricular_units_1st_sem_enrolled'] - input_df['Curricular_units_1st_sem_approved']
    failed_courses_2nd = input_df['Curricular_units_2nd_sem_enrolled'] - input_df['Curricular_units_2nd_sem_approved']
    total_failed = failed_courses_1st + failed_courses_2nd

    input_df['Interaction_Grade_Failed_Courses'] = input_df['Admission_grade'] * total_failed
    input_df['Interaction_Mother_Father_Qual'] = input_df['Mothers_qualification'] * input_df['Fathers_qualification']
    input_df['Combined_Parents_Qual'] = input_df['Mothers_qualification'] + input_df['Fathers_qualification']

    # --- Sesuaikan urutan kolom ---
    input_data_processed = pd.DataFrame(0, index=[0], columns=df_template.columns)
    for col in input_df.columns:
        if col in input_data_processed.columns:
            input_data_processed[col] = input_df[col].iloc[0]

    input_data_processed = input_data_processed[df_template.columns]

    # --- Prediksi ---
    prediction = model.predict(input_data_processed)
    prediction_proba = model.predict_proba(input_data_processed)

    # --- Tampilkan Hasil ---
    st.subheader("Hasil Prediksi")
    if prediction[0] == 1:
        st.error(f"⚠️ Siswa ini **berpotensi DO** dengan probabilitas: **{prediction_proba[0][1]*100:.2f}%**")
        st.markdown("""
        <div style='background-color:#ffe6e6;padding:10px;border-radius:5px;border:1px solid #ffcccc'>
        🧠 **Rekomendasi**: Lakukan bimbingan akademik dan evaluasi psikososial secepat mungkin.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.success(f"✅ Siswa ini **kemungkinan besar lulus** dengan probabilitas: **{prediction_proba[0][0]*100:.2f}%**")
        st.markdown("""
        <div style='background-color:#e6ffe6;padding:10px;border-radius:5px;border:1px solid #ccffcc'>
        🟢 **Rekomendasi**: Tetap pantau perkembangan akademik siswa secara berkala.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📝 Detail Data Input")
    st.write(input_data_processed)

# ==== 8. Footer ====
st.markdown("---")
st.caption("© 2025 Jaya Jaya Institut — Sistem Prediksi Dropout Mahasiswa")
