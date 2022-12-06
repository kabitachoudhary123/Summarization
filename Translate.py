
import streamlit as st
import requests
import base64

st.title("Translation 🤗")
lang_codes_by_name = \
    {'Arabic': 'ar_AR',
     'Czech': 'cs_CZ',
     'German': 'de_DE',
     'English': 'en_XX',
     'Spanish': 'es_XX',
     'Estonian': 'et_EE',
     'Finnish': 'fi_FI',
     'French': 'fr_XX',
     'Gujarati': 'gu_IN',
     'Hindi': 'hi_IN',
     'Italian': 'it_IT',
     'Japanese': 'ja_XX',
     'Kazakh': 'kk_KZ',
     'Korean': 'ko_KR',
     'Lithuanian': 'lt_LT',
     'Latvian': 'lv_LV',
     'Burmese': 'my_MM',
     'Nepali': 'ne_NP',
     'Dutch': 'nl_XX',
     'Romanian': 'ro_RO',
     'Russian': 'ru_RU',
     'Sinhala': 'si_LK',
     'Turkish': 'tr_TR',
     'Vietnamese': 'vi_VN',
     'Chinese': 'zh_CN',
     'Afrikaans': 'af_ZA',
     'Azerbaijani': 'az_AZ',
     'Bengali': 'bn_IN',
     'Persian': 'fa_IR',
     'Hebrew': 'he_IL',
     'Croatian': 'hr_HR',
     'Indonesian': 'id_ID',
     'Georgian': 'ka_GE',
     'Khmer': 'km_KH',
     'Macedonian': 'mk_MK',
     'Malayalam': 'ml_IN',
     'Mongolian': 'mn_MN',
     'Marathi': 'mr_IN',
     'Polish': 'pl_PL',
     'Pashto': 'ps_AF',
     'Portuguese': 'pt_XX',
     'Swedish': 'sv_SE',
     'Swahili': 'sw_KE',
     'Tamil': 'ta_IN',
     'Telugu': 'te_IN',
     'Thai': 'th_TH',
     'Tagalog': 'tl_XX',
     'Ukrainian': 'uk_UA',
     'Urdu': 'ur_PK',
     'Xhosa': 'xh_ZA',
     'Galician': 'gl_ES',
     'Slovene': 'sl_SI'}
choices = tuple(lang_codes_by_name.keys())

inp_text = st.text_area("Enter your text here.....", height=100)
source_option = st.selectbox(
    'What is the source language?', choices)
translate_option = st.selectbox(
    'What is the deatinaion language?', choices)

button = st.button("Translate")

if button:
    with st.spinner():
        response_json = requests.post("https://kabita-choudhary-translationmodel.hf.space/api/predict", json={
            "data": [
                inp_text, source_option, translate_option
            ]}).json()
        output = response_json['data'][0]

        st.text_area("Result", value=output, height=100)